# Homelab Setup Guide — Debian 13 (Trixie)

---

## 1. Disable the Graphical Interface

On your Debian homelab, set it to boot into terminal only:

```bash
sudo systemctl set-default multi-user.target
```

To apply immediately without rebooting:

```bash
sudo systemctl isolate multi-user.target
```

*(If you ever need the GUI back: `sudo systemctl set-default graphical.target`)*

You can also uninstall the desktop environment entirely to free up resources:

```bash
sudo apt purge task-gnome-desktop gnome* gdm3
sudo apt autoremove
```

---

## 2. SSH Configuration

### On Debian (homelab):

**Install and enable SSH server:**

```bash
sudo apt update
sudo apt install openssh-server
sudo systemctl enable --now ssh
```

**Find your homelab's IP address:**

```bash
ip addr show
```

Look for the IP under your network interface (e.g., `192.168.1.50`).

### On Fedora (main PC):

**Test the connection:**

```bash
ssh your_username@192.168.1.50
```

**Set up SSH key authentication (no password needed):**

```bash
ssh-keygen -t ed25519
ssh-copy-id your_username@192.168.1.50
```

**Create an SSH config for easy access** — edit `~/.ssh/config`:

```
Host homelab
    HostName 192.168.1.50
    User your_username
    IdentityFile ~/.ssh/id_ed25519
```

Now you can simply connect with:

```bash
ssh homelab
```

### Harden SSH on Debian (optional but recommended):

Edit `/etc/ssh/sshd_config`:

```
PermitRootLogin no
PasswordAuthentication no
```

Then restart SSH:

```bash
sudo systemctl restart ssh
```

---

## 3. Remote Power On / Off

### Turn OFF from Fedora:

Simply run:

```bash
ssh homelab sudo poweroff
```

To avoid needing a password for shutdown, on **Debian** run `sudo visudo` and add:

```
your_username ALL=(ALL) NOPASSWD: /sbin/poweroff, /sbin/reboot, /sbin/shutdown
```

Now you can do:

```bash
ssh homelab sudo poweroff    # shut down
ssh homelab sudo reboot      # reboot
```

### Turn ON from Fedora (Wake-on-LAN):

**On Debian**, find your network interface and MAC address:

```bash
ip link show
```

Example output: `link/ether aa:bb:cc:dd:ee:ff` on interface `enp1s0`.

**Enable WOL on Debian:**

```bash
sudo apt install ethtool
sudo ethtool -s enp1s0 wol g
```

To make it persistent, create `/etc/systemd/system/wol.service`:

```ini
[Unit]
Description=Enable Wake-on-LAN
After=network.target

[Service]
Type=oneshot
ExecStart=/sbin/ethtool -s enp1s0 wol g

[Install]
WantedBy=multi-user.target
```

Then enable it:

```bash
sudo systemctl enable wol.service
```

**Also enable WOL in the BIOS** (Dell Latitude 3450):
- Press **F2** at boot
- Go to **Power Management > Wake on LAN**
- Set it to **LAN Only** or **LAN with PXE Boot**

**On Fedora**, install the wake tool and power on your homelab:

```bash
sudo dnf install wol
wol aa:bb:cc:dd:ee:ff
```

Replace `aa:bb:cc:dd:ee:ff` with your Debian's actual MAC address.

You can create an alias in your `~/.bashrc` for convenience:

```bash
alias homelab-on='wol aa:bb:cc:dd:ee:ff'
alias homelab-off='ssh homelab sudo poweroff'
```

---

## 4. Open TCP Ports on Debian

Debian 13 uses `nftables` by default. You can manage it with `nft` directly or install `ufw` for simplicity.

### Option A: Using UFW (simpler)

```bash
sudo apt install ufw
```

**Allow SSH first (important — don't lock yourself out):**

```bash
sudo ufw allow ssh
```

**Open specific ports:**

```bash
sudo ufw allow 8080/tcp    # example: web server
sudo ufw allow 3000/tcp    # example: Grafana
sudo ufw allow 9090/tcp    # example: Prometheus
```

**Restrict access to your Fedora PC only:**

```bash
sudo ufw allow from 192.168.1.100 to any port 8080 proto tcp
```

**Enable the firewall:**

```bash
sudo ufw enable
sudo ufw status
```

### Option B: Using nftables directly

```bash
sudo nft add rule inet filter input tcp dport {8080, 3000, 9090} accept
```

To persist rules:

```bash
sudo nft list ruleset > /etc/nftables.conf
sudo systemctl enable nftables
```

---

## Quick Reference

| Action | Command (from Fedora) |
|---|---|
| Connect | `ssh homelab` |
| Power off | `ssh homelab sudo poweroff` |
| Reboot | `ssh homelab sudo reboot` |
| Power on | `wol aa:bb:cc:dd:ee:ff` |
| Check open ports | `ssh homelab sudo ufw status` |

---

## Recommended: Static IP for Debian

To avoid the homelab IP changing, edit `/etc/network/interfaces` on Debian:

```
auto enp1s0
iface enp1s0 inet static
    address 192.168.1.50
    netmask 255.255.255.0
    gateway 192.168.1.1
    dns-nameservers 1.1.1.1 8.8.8.8
```

Then restart networking:

```bash
sudo systemctl restart networking
```

Alternatively, you can assign a static lease on your router for the homelab's MAC address.

---

## Troubleshooting

### `ethtool: command not found` (even though it's installed)

On Debian, `ethtool` is installed at `/usr/sbin/ethtool`, which may not be in a regular user's `PATH`. Fix it by either:

**Using the full path:**

```bash
sudo /usr/sbin/ethtool -s enp1s0 wol g
```

**Or adding `/usr/sbin` to your PATH permanently:**

```bash
echo 'export PATH="$PATH:/usr/sbin"' >> ~/.bashrc
source ~/.bashrc
```

### Finding your MAC address

```bash
ip link show
```

Look for the `link/ether` line under your network interface:

```
2: enp1s0: <BROADCAST,MULTICAST,UP,LOWER_UP> ...
    link/ether aa:bb:cc:dd:ee:ff brd ff:ff:ff:ff:ff:ff
```

The `aa:bb:cc:dd:ee:ff` part is your MAC address.

### Keep running with laptop lid closed

Edit the logind config on Debian:

```bash
sudo nano /etc/systemd/logind.conf
```

Find and set (uncomment if needed):

```
HandleLidSwitch=ignore
HandleLidSwitchExternalPower=ignore
HandleLidSwitchDocked=ignore
```

Then restart the service:

```bash
sudo systemctl restart systemd-logind
```

Now closing the lid will do nothing — the system stays fully running.
