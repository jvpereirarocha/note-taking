# Creating a Linux Container from Scratch on Fedora

This tutorial will guide you through the process of creating a simple container-like environment from scratch on Fedora Linux using fundamental Linux features: `namespaces` and control groups (`cgroups`). This exercise will help you understand the magic behind container technologies like Docker and Podman. We will manually create an isolated environment with its own hostname, processes, filesystem, network, and resource limits.

## Prerequisites

*   A Fedora Linux machine.
*   Root privileges (`sudo`).
*   `dnf` package manager.
*   `iproute` package installed (`sudo dnf install iproute`). This provides the `ip` command.

## Step 1: Setting up the new root filesystem

First, we need a root filesystem for our container. We'll create a directory and use `dnf` to create a minimal Fedora filesystem inside it.

```bash
# Create a directory for the container's root filesystem
sudo mkdir /new_root

# Use dnf to create a minimal Fedora filesystem
# This might take a few minutes
sudo dnf install --installroot=/new_root --releasever=$(rpm -E %fedora) dnf fedora-release bash coreutils --setopt=install_weak_deps=False
```
* `--installroot=/new_root`: Specifies the root directory for the installation.
* `--releasever=$(rpm -E %fedora)`: Ensures we are installing the same release as the host.
* `dnf fedora-release bash coreutils`: A few essential packages for a minimal system.
* `--setopt=install_weak_deps=False`: Prevents installation of recommended packages, keeping the image small.


**Checkpoint**: Verify that the new root filesystem has been created.

```bash
# List the contents of the new_root directory
ls /new_root
```

You should see a typical Linux root filesystem structure (`bin`, `etc`, `home`, `lib`, `usr`, etc.).

## Step 2: Creating a new shell process with its own namespaces

We'll use the `unshare` command to create a new shell process in new PID, Mount, UTS, and IPC namespaces.

```bash
# Spawn a new bash shell in new namespaces
sudo unshare --pid --mount-proc --ipc --uts --fork /bin/bash
```

*   `--pid`: Creates a new PID namespace.
*   `--mount-proc`: Mounts the `/proc` filesystem in the new mount namespace. This is important for the new PID namespace to work correctly.
*   `--ipc`: Creates a new IPC namespace.
*   `--uts`: Creates a new UTS namespace.
*   `--fork`: Forks a new process.

You are now in a new shell with new namespaces. Let's verify it.

### Checkpoint: Verify the new namespaces

1.  **Check the hostname (UTS Namespace)**

    ```bash
    # Check the current hostname
    hostname

    # Change the hostname inside the new namespace
    hostname my-fedora-container

    # Check the new hostname
    hostname
    ```

    You should see `my-fedora-container` as the new hostname. Now, open a **new terminal window** on your host machine (outside the container) and run `hostname`. You will see your original hostname. This shows that the UTS namespace is isolating the hostname.

2.  **Check the Process ID (PID Namespace)**

    Inside the container's shell:

    ```bash
    # Check the process ID of the current shell
    echo $$

    # List processes
    ps aux
    ```

    You will see that your shell has PID 1, which is the init process in a typical Linux system. You will also see very few processes running. From the host's perspective, your container is just a single process.

## Step 3: Changing the root filesystem

Now, let's change the root filesystem of our container to the one we created in Step 1.

```bash
# From inside the container's shell from the previous step

# Mount the new root filesystem
mount --bind /new_root /new_root

# Create a directory inside the new root to pivot into
mkdir /new_root/old_root

# Pivot the root filesystem
pivot_root /new_root /new_root/old_root

# Change to the new root directory
cd /

# Unmount the old root
umount -l /old_root
```

*   `mount --bind`: Makes a directory or file visible at another location in the directory tree.
*   `pivot_root`: Moves the root file system of the current process to the directory `put_old` and makes `new_root` the new root file system.

Now your container has its own isolated filesystem.

### Checkpoint: Verify the new root filesystem

```bash
# List the contents of the root directory
ls /
```

You should see the contents of the `/new_root` directory we created earlier.

## Step 4: Setting up an isolated Network (Network Namespace)

We will now create a dedicated network for our container.

First, **exit the container shell** from the previous step by typing `exit`. You should be back in your host's shell.

1.  **Create a new network namespace.**

    ```bash
    # Create a new network namespace called 'my-netns'
    sudo ip netns add my-netns
    ```

2.  **Create a virtual ethernet (veth) pair.**
    This will act as a virtual cable connecting the host and the container.

    ```bash
    # Create a veth pair
    sudo ip link add veth-host type veth peer name veth-container
    ```

3.  **Move one end of the veth pair to the network namespace.**

    ```bash
    # Move veth-container to the 'my-netns' network namespace
    sudo ip link set veth-container netns my-netns
    ```

4.  **Configure the IP addresses.**

    ```bash
    # Configure the host side of the veth pair
    sudo ip addr add 10.0.0.1/24 dev veth-host
    sudo ip link set veth-host up

    # Configure the container side of the veth pair
    sudo ip netns exec my-netns ip addr add 10.0.0.2/24 dev veth-container
    sudo ip netns exec my-netns ip link set veth-container up
    sudo ip netns exec my-netns ip link set lo up
    sudo ip netns exec my-netns ip route add default via 10.0.0.1
    ```

5.  **Enable IP forwarding and NAT on the host.**
    This will allow the container to access the internet. Fedora uses `firewalld`, so we will use `firewall-cmd`.

    ```bash
    # Enable IP forwarding
    sudo sysctl -w net.ipv4.ip_forward=1

    # Add a NAT rule using firewalld
    sudo firewall-cmd --zone=public --add-masquerade --permanent
    sudo firewall-cmd --reload
    ```

### Checkpoint: Verify network connectivity

```bash
# From the host, ping the container
ping -c 3 10.0.0.2

# From inside the network namespace, ping the host
sudo ip netns exec my-netns ping -c 3 10.0.0.1

# From inside the network namespace, ping an external address
sudo ip netns exec my-netns ping -c 3 8.8.8.8
```

If all pings are successful, your container has network connectivity!

## Step 5: Limiting resources with Cgroups v2

Now we'll limit the CPU and memory usage of our container using cgroups v2, which is the default in modern Fedora.

1.  **Create a new cgroup.**
    With cgroup v2, we create a directory in `/sys/fs/cgroup`.

    ```bash
    # Create a new cgroup for our container
    sudo mkdir /sys/fs/cgroup/my-container
    ```

2.  **Set resource limits.**
    In cgroup v2, we write to files directly inside the cgroup directory.

    ```bash
    # Limit to 50% of one CPU core (50000 microseconds out of 100000)
    sudo sh -c 'echo "50000 100000" > /sys/fs/cgroup/my-container/cpu.max'

    # Limit memory to 100MB
    sudo sh -c 'echo 100M > /sys/fs/cgroup/my-container/memory.max'
    ```

3.  **Move a process into the cgroup.**

    To test this, we'll run a process and add its PID to the cgroup's `cgroup.procs` file.

    ```bash
    # In one terminal, run a process in the network namespace
    sudo ip netns exec my-netns /bin/bash -c 'while true; do :; done' &
    PROC_PID=$!

    # Move the process to the cgroup
    sudo sh -c "echo $PROC_PID > /sys/fs/cgroup/my-container/cgroup.procs"

    echo "Process $PROC_PID moved to cgroup 'my-container'"
    ```

### Checkpoint: Verify resource limits

You can use monitoring tools like `top` or `htop` on the host to observe the CPU usage of the process. You will see that it doesn't exceed 50% of a single CPU core.

To check the memory limit, you could run a process inside the cgroup that consumes a lot of memory and see it being killed when it exceeds the 100MB limit.

## Conclusion

Congratulations! You have successfully created a container-like environment from scratch on Fedora. You have learned how namespaces provide isolation and how cgroups limit resources, using Fedora-specific tools and the modern cgroup v2 interface.

To clean up the resources created:

```bash
# Kill the process running in the cgroup
sudo kill $PROC_PID

# Remove the cgroup directory
sudo rmdir /sys/fs/cgroup/my-container

# Delete the network namespace
sudo ip netns del my-netns

# Delete the veth pair
sudo ip link del v-eth1

# Remove the firewalld masquerade rule
sudo firewall-cmd --zone=public --remove-masquerade --permanent
sudo firewall-cmd --reload

# Unmount and remove the root filesystem
# Make sure you have exited from any shell that is using it
sudo umount /new_root
sudo rm -rf /new_root
```
