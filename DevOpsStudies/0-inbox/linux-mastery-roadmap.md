#linux/mastery #roadmap #february2026

# Linux Mastery Roadmap

A step-by-step roadmap to reach advanced Linux knowledge. This roadmap has **two tracks**:

- **Track A — Linux Deep Knowledge** (Phases 1-12): a progressive path to master Linux internals
- **Track B — DevOps Practical Path**: a hands-on path to start building with containers, CI/CD, and orchestration

You do NOT need to finish all 12 phases before starting Track B. Complete the **Linux Pre-Requirements for DevOps** section below, then follow both tracks in parallel — the DevOps labs will reinforce your Linux learning.

Topics you already have notes on are marked with ~~strikethrough~~.

---

# Track B — DevOps Practical Path

## Linux Pre-Requirements for DevOps Labs

Complete these before starting the DevOps path. These are the minimum Linux skills you need to not get stuck.

### Already covered
- [x] ~~Basic commands (ls, mv, pwd, cp, cat, head, tail, find)~~
- [x] ~~File permissions (chmod, chown)~~
- [x] ~~Linux Filesystem Hierarchy (/boot, /etc, /dev, /tmp)~~
- [x] ~~Process inspection and signals (ps, kill)~~
- [x] ~~VIM basics (normal, insert, command-line modes)~~

### Must learn before starting
- [x] **Environment variables** — how to set, export, and persist them (`export`, `.bashrc`, `.env` files). Containers rely heavily on env vars for configuration.
- [ ] **I/O redirection and pipes** — redirect output (`>`, `>>`), pipe between commands (`|`), stderr vs stdout (`2>&1`). Essential for reading logs and building pipelines.
- [ ] **Basic shell scripting** — variables, `if/else`, `for` loops, exit codes (`$?`), `&&` and `||` chaining. CI/CD pipelines are shell scripts under the hood.
- [x] **SSH key-based authentication** — generate keys (`ssh-keygen`), copy to servers (`ssh-copy-id`), `~/.ssh/config` file. Required for Git, remote servers, and deployments.
- [ ] **Networking fundamentals** — what ports are, `localhost`, DNS basics, IP addresses, `curl` for HTTP requests. Containers expose and map ports constantly.
- [ ] **Service management basics** — `systemctl start/stop/status/enable`, checking logs with `journalctl`. You'll manage Docker daemon and other services.
- [x] **Package management** — install, update, and remove packages (`apt`/`dnf`/`pacman` depending on your distro). You'll install tools inside containers and on servers.
- [ ] **Logs and troubleshooting** — reading logs with `journalctl`, `tail -f`, and understanding where logs live (`/var/log/`). When something breaks, logs are your first stop.

### Nice to have (learn alongside DevOps)
- [x] `grep` with basic regex — filter log output, search config files
- [ ] `sed` and `awk` basics — quick text transformations in pipelines
- [ ] `tar` and file compression — container images and artifacts are often tarballs
- [ ] File ownership and groups in practice — volume mount permission issues in containers

---

## Step 1 — Containers with Docker

Start here. Docker abstracts most Linux complexity and gives you fast feedback loops.

- [x] What is a container vs a VM (conceptual understanding)
- [x] Install Docker and understand the Docker daemon
- [ ] Core commands: `docker run`, `docker ps`, `docker stop`, `docker rm`, `docker logs`
- [ ] Images: `docker pull`, `docker images`, `docker rmi`, Docker Hub
- [ ] Write a `Dockerfile` (FROM, RUN, COPY, EXPOSE, CMD, ENTRYPOINT)
- [ ] Build and tag images (`docker build -t`)
- [ ] Volumes — persist data outside containers (`-v`, named volumes, bind mounts)
- [ ] Networking — expose ports (`-p`), container-to-container communication
- [ ] Environment variables in containers (`-e`, `--env-file`)
- [ ] Multi-stage builds — smaller, production-ready images
- [x] `.dockerignore` — keep images clean
- [x] **Project**: Containerize a simple web application (e.g., a Node.js or Python API)

### Suggested resources
- Docker official "Getting Started" guide
- "Docker Deep Dive" by Nigel Poulton
- KodeKloud Docker course

---

## Step 2 — Basic Shell Scripting for Automation

You need this for CI/CD pipelines and general automation.

- [ ] Write scripts with `#!/bin/bash` shebang
- [ ] Variables, string interpolation, and quoting (`"$var"` vs `'$var'`)
- [ ] Conditionals (`if`, `elif`, `else`, test operators `-f`, `-d`, `-z`)
- [ ] Loops (`for item in list`, `while read line`)
- [ ] Exit codes and error handling (`$?`, `set -e`, `&&`, `||`)
- [ ] Functions (basic)
- [ ] Reading input and arguments (`$1`, `$2`, `$@`, `$#`)
- [ ] **Project**: Write a deployment script that builds a Docker image, tags it, and runs it

### Suggested resources
- "The Linux Command Line" by William Shotts — Chapters on scripting
- ShellCheck (shellcheck.net) — lint your scripts

---

## Step 3 — Version Control with Git (DevOps essentials)

If you already know Git basics, focus on the collaboration workflow.

- [ ] Branching strategies (feature branches, Git Flow basics)
- [x] Pull requests / merge requests workflow
- [x] Resolving merge conflicts
- [x] `.gitignore` best practices
- [ ] Tagging releases (`git tag`)
- [x] **Project**: Set up a repository with a proper branching strategy for your containerized app

---

## Step 4 — CI/CD Pipelines

Automate building, testing, and deploying your applications.

- [ ] What is CI/CD (Continuous Integration / Continuous Delivery / Continuous Deployment)
- [ ] Pick a platform: **GitHub Actions** (easiest to start), GitLab CI, or Jenkins
- [ ] Pipeline anatomy: triggers, jobs, steps, stages
- [ ] Write a pipeline that: builds a Docker image, runs tests, pushes image to a registry
- [ ] Environment variables and secrets management in CI/CD
- [ ] Artifacts and caching in pipelines
- [ ] Deploy to a server or cloud from the pipeline
- [ ] **Project**: Create a CI/CD pipeline for your containerized app (build → test → push → deploy)

### Suggested resources
- GitHub Actions official docs
- "Learning GitHub Actions" by Brent Laster
- KodeKloud CI/CD course

---

## Step 5 — Docker Compose (Multi-Container Applications)

Orchestrate multiple containers locally before moving to Kubernetes.

- [ ] `docker-compose.yml` syntax (services, networks, volumes)
- [ ] Define multi-service apps (e.g., app + database + cache)
- [ ] Environment files and variable substitution
- [ ] Depends_on, healthchecks, and restart policies
- [ ] Named volumes for database persistence
- [ ] Custom networks for service isolation
- [ ] **Project**: Build a full-stack app with Docker Compose (e.g., API + PostgreSQL + Redis)

### Suggested resources
- Docker Compose official documentation
- "Docker Deep Dive" — Compose chapters

---

## Step 6 — Container Registry and Image Management

Manage your images like a professional.

- [ ] Docker Hub — push and pull images
- [ ] Private registries (GitHub Container Registry, AWS ECR, or self-hosted)
- [ ] Image tagging strategies (semantic versioning, git SHA, `latest` pitfalls)
- [ ] Image scanning for vulnerabilities (`docker scout`, `trivy`)
- [ ] **Project**: Push your app images to a registry and pull them in your CI/CD pipeline

---

## Step 7 — Kubernetes Basics (Container Orchestration)

The industry standard for running containers at scale.

- [ ] Why Kubernetes — what problem it solves
- [ ] Architecture: control plane (API server, scheduler, etcd) and worker nodes (kubelet, kube-proxy)
- [ ] Install a local cluster: **Minikube**, Kind, or k3s
- [ ] `kubectl` basics: `get`, `describe`, `logs`, `exec`, `apply`, `delete`
- [ ] Core objects:
  - [ ] **Pods** — the smallest deployable unit
  - [ ] **Deployments** — declarative updates and rollbacks
  - [ ] **Services** — expose pods to the network (ClusterIP, NodePort, LoadBalancer)
  - [ ] **ConfigMaps** and **Secrets** — externalize configuration
  - [ ] **Namespaces** — isolate resources
- [ ] YAML manifests — writing and applying them
- [ ] Rolling updates and rollbacks
- [ ] **Project**: Deploy your Docker Compose app to a local Kubernetes cluster

### Suggested resources
- Kubernetes official tutorials (kubernetes.io/docs/tutorials)
- "Kubernetes Up & Running" by Brendan Burns, Joe Beda, Kelsey Hightower
- KodeKloud CKA course

---

## Step 8 — Kubernetes Intermediate

Go deeper once the basics click.

- [ ] **Ingress** — route external traffic to services
- [ ] **Persistent Volumes (PV)** and **Persistent Volume Claims (PVC)** — storage in K8s
- [ ] **Helm** — package manager for Kubernetes (charts, values, releases)
- [ ] **Resource limits** — CPU and memory requests/limits
- [ ] **Probes** — liveness, readiness, startup probes
- [ ] **Jobs and CronJobs** — batch and scheduled workloads
- [ ] **RBAC** — Role-Based Access Control
- [ ] Monitoring with **Prometheus** and **Grafana** (basics)
- [ ] **Project**: Deploy a production-like setup with Ingress, TLS, persistent storage, and monitoring

### Suggested resources
- Helm official docs
- "The Kubernetes Book" by Nigel Poulton

---

## Step 9 — Infrastructure as Code (IaC)

Define and version your infrastructure like application code.

- [ ] What is IaC and why it matters
- [ ] **Terraform** basics — providers, resources, variables, outputs, state
- [ ] Terraform workflow: `init`, `plan`, `apply`, `destroy`
- [ ] Manage cloud resources (VMs, networks, storage) with Terraform
- [ ] **Ansible** basics — inventory, playbooks, modules, roles
- [ ] Configuration management vs provisioning (Ansible vs Terraform)
- [ ] **Project**: Provision a cloud VM with Terraform, configure it with Ansible, deploy your app with Docker

### Suggested resources
- Terraform official tutorials (developer.hashicorp.com/terraform/tutorials)
- "Terraform Up & Running" by Yevgeniy Brikman
- Ansible official getting started guide

---

## Step 10 — Observability and Monitoring

You can't manage what you can't see.

- [ ] The three pillars: **Logs**, **Metrics**, **Traces**
- [ ] Centralized logging (ELK Stack or Loki + Grafana)
- [ ] Metrics collection with **Prometheus**
- [ ] Dashboards with **Grafana**
- [ ] Alerting basics (Prometheus Alertmanager)
- [ ] Application-level monitoring (health endpoints, custom metrics)
- [ ] **Project**: Set up a full observability stack for your Kubernetes-deployed app

### Suggested resources
- Prometheus official docs
- Grafana tutorials
- "Observability Engineering" by Charity Majors

---

## DevOps Practical Path — Summary

```
Linux Pre-Requirements
        |
        v
   Docker (Step 1)  +  Shell Scripting (Step 2)
        |
        v
   Git Workflows (Step 3)
        |
        v
   CI/CD Pipelines (Step 4)
        |
        v
   Docker Compose (Step 5)  +  Container Registry (Step 6)
        |
        v
   Kubernetes Basics (Step 7)
        |
        v
   Kubernetes Intermediate (Step 8)
        |
        v
   Infrastructure as Code (Step 9)
        |
        v
   Observability & Monitoring (Step 10)
```

> As you progress through Track B, go back to Track A phases that become relevant. Debugging a container network issue? Study Phase 7 (Advanced Networking). Permission errors on volume mounts? Revisit Phase 3 (Users & Access Control). The two tracks feed each other.

---

# Track A — Linux Deep Knowledge

## Phase 1 — Solidify the Fundamentals (you are here)
> *Complete this phase, then start Track B (DevOps) while continuing with Phase 2+*

You already have most of this covered. Fill in the gaps and make sure everything is second nature.

- [x] ~~Basic commands (ls, cd, mkdir, rm, cp, mv)~~
- [x] ~~File display (cat, head, tail, less, more)~~
- [x] ~~File searching (find, locate, grep)~~
- [x] ~~Wildcards and globbing~~
- [x] ~~I/O redirection and pipes~~
- [x] ~~File permissions (chmod, chown, chgrp, umask)~~
- [x] ~~Linux directory structure (FHS)~~
- [x] ~~Compressing and extracting files (tar, gzip, zip)~~
- [x] ~~Sorting and manipulating file content (sort, cut, awk, sed basics)~~
- [x] ~~Shell prompt customization~~
- [x] ~~VIM basics~~
- [x] ~~Basic networking commands (ping, curl, dig, netstat, nmap, traceroute)~~
- [x] ~~File transfer over the network (scp, rsync)~~
- [ ] Environment variables and shell configuration (.bashrc, .bash_profile, .zshrc)
- [ ] Aliases and shell functions
- [ ] Man pages, info pages, and `--help` — mastering self-learning from the terminal

### Suggested resources
- "How Linux Works" by Brian Ward — Chapters 1-3 (you already started this)
- Linux Journey (linuxjourney.com)

---

## Phase 2 — Process Management and Job Control

Understand how Linux manages everything that runs.

- [ ] Viewing processes (`ps`, `top`, `htop`, `pstree`)
- [ ] Process states (running, sleeping, stopped, zombie)
- [ ] Foreground vs background processes (`&`, `fg`, `bg`, `jobs`)
- [ ] Signals and killing processes (`kill`, `killall`, `pkill`, signals like SIGTERM, SIGKILL, SIGHUP)
- [ ] Process priority and niceness (`nice`, `renice`)
- [ ] `/proc` filesystem — inspecting live process info
- [ ] Daemons — what they are and how they work
- [ ] `lsof` — listing open files and sockets by process
- [ ] `strace` — tracing system calls of a process

### Suggested resources
- "How Linux Works" — Chapter 8 (Processes and Resource Utilization)
- `man 7 signal`

---

## Phase 3 — Users, Groups, and Access Control (Deep Dive)

Go beyond basic permissions into real-world administration.

- [ ] User management (`useradd`, `usermod`, `userdel`, `passwd`)
- [ ] Group management (`groupadd`, `groupmod`, `groupdel`)
- [ ] `/etc/passwd`, `/etc/shadow`, `/etc/group` — understanding the files
- [ ] `su` vs `sudo` — privilege escalation
- [ ] Sudoers file (`/etc/sudoers`, `visudo`)
- [ ] Special permissions: SUID, SGID, sticky bit
- [ ] ACLs (Access Control Lists) with `getfacl` and `setfacl`
- [ ] PAM (Pluggable Authentication Modules) — overview

### Suggested resources
- "How Linux Works" — Chapter 7
- `man sudoers`

---

## Phase 4 — Systemd and Service Management

The modern Linux init system — essential for any sysadmin or DevOps engineer.

- [ ] The Linux boot process (BIOS/UEFI → bootloader → kernel → init/systemd)
- [ ] Systemd architecture (units, targets, dependencies)
- [ ] Managing services (`systemctl start/stop/restart/enable/disable/status`)
- [ ] Writing custom systemd unit files
- [ ] Timers (systemd alternative to cron)
- [ ] Journalctl — querying and filtering logs
- [ ] Boot targets (multi-user, graphical, rescue, emergency)
- [ ] Analyzing boot performance (`systemd-analyze`)
- [ ] Understanding `init` vs `systemd` (historical context)
- [ ] Cron jobs and `at` scheduling

### Suggested resources
- Arch Wiki: systemd
- "How Linux Works" — Chapter 6
- `man systemd.unit`, `man systemd.service`

---

## Phase 5 — Storage, Filesystems, and Disk Management

Master how Linux handles storage from raw disks to mounted filesystems.

- [ ] Block devices and disk identification (`lsblk`, `blkid`, `fdisk -l`)
- [ ] Partitioning (MBR vs GPT, `fdisk`, `parted`, `gdisk`)
- [ ] Filesystems (ext4, xfs, btrfs) — creating and formatting (`mkfs`)
- [ ] Mounting and unmounting (`mount`, `umount`, `/etc/fstab`)
- [ ] Swap space (swap partition vs swap file)
- [ ] LVM (Logical Volume Manager) — PV, VG, LV concepts and commands
- [ ] RAID basics (RAID 0, 1, 5, 10 with `mdadm`)
- [ ] Disk usage analysis (`df`, `du`, `ncdu`)
- [ ] Inodes — what they are and when you run out
- [ ] `dd` command — disk cloning and image creation
- [ ] Smart monitoring (`smartctl`)

### Suggested resources
- "How Linux Works" — Chapter 4
- Arch Wiki: LVM, File systems

---

## Phase 6 — Advanced Shell Scripting

Level up from basic scripts to production-grade automation.

- [ ] Variables, quoting rules, and parameter expansion (`${var:-default}`, `${var%%pattern}`)
- [ ] Conditionals in depth (`[[ ]]` vs `[ ]`, `-f`, `-d`, `-z`, `-n`, regex matching)
- [ ] Loops (`for`, `while`, `until`, loop over files, loop over command output)
- [ ] Functions (local variables, return values, passing arguments)
- [ ] Error handling (`set -euo pipefail`, `trap`)
- [ ] Here documents and here strings
- [ ] Advanced `awk` and `sed` (multi-line, in-place editing, field processing)
- [ ] `xargs` — building commands from stdin
- [ ] Process substitution (`<()` and `>()`)
- [ ] Arrays and associative arrays in Bash
- [ ] Debugging scripts (`set -x`, `bash -x`, `shellcheck`)
- [ ] Writing portable POSIX shell vs Bash-specific features

### Suggested resources
- "The Linux Command Line" by William Shotts (free online)
- ShellCheck (shellcheck.net)
- Google Shell Style Guide

---

## Phase 7 — Networking (Advanced)

Go from running commands to truly understanding Linux networking.

- [ ] TCP/IP stack fundamentals (OSI model, TCP vs UDP, handshake)
- [ ] Network interfaces and IP configuration (`ip addr`, `ip link`, `ip route`)
- [ ] DNS resolution in depth (`/etc/resolv.conf`, `/etc/hosts`, `systemd-resolved`)
- [ ] Firewall management with `iptables` / `nftables`
- [ ] Firewall frontends (`firewalld`, `ufw`)
- [ ] Network namespaces
- [ ] Bridging, bonding, and VLANs
- [ ] SSH deep dive (key-based auth, config file, tunneling, port forwarding, ProxyJump)
- [ ] TCP dump and packet analysis (`tcpdump`, Wireshark basics)
- [ ] Socket programming concepts (what is a socket, `ss` command)
- [ ] Network troubleshooting methodology (layer-by-layer approach)

### Suggested resources
- "How Linux Works" — Chapter 9-10
- Arch Wiki: Network configuration
- `man ip`, `man iptables`

---

## Phase 8 — Kernel Internals and the Linux Architecture

Understand the engine under the hood.

- [ ] Kernel space vs user space (revisit with deeper understanding)
- [ ] System calls — the interface between user programs and kernel
- [ ] Kernel modules (`lsmod`, `modprobe`, `modinfo`, `rmmod`)
- [ ] `/proc` and `/sys` filesystems — kernel tuning at runtime
- [ ] `sysctl` — modifying kernel parameters
- [ ] Device drivers overview (character vs block devices)
- [ ] Udev — dynamic device management
- [ ] D-Bus and IPC (Inter-Process Communication)
- [ ] Kernel compilation basics (configuring, building, installing a custom kernel)
- [ ] Kernel logs (`dmesg`, `journalctl -k`)

### Suggested resources
- "How Linux Works" — Chapters 3-4
- "Linux Kernel Development" by Robert Love (for deeper study)
- Kernel Newbies (kernelnewbies.org)

---

## Phase 9 — Containers and Namespaces (From the Inside)

You already started exploring containers from scratch — go deeper.

- [ ] Linux namespaces (PID, NET, MNT, UTS, IPC, USER, CGROUP)
- [ ] Cgroups v1 and v2 (resource limits: CPU, memory, I/O)
- [ ] `unshare` and `nsenter` commands
- [ ] Chroot vs pivot_root
- [ ] Building a container from scratch (expand your existing notes)
- [ ] Overlay filesystems (how container images work)
- [ ] Seccomp — system call filtering
- [ ] Capabilities — fine-grained privilege control
- [ ] How Docker/Podman use these primitives under the hood

### Suggested resources
- Your existing notes on creating containers from scratch
- "Containers from Scratch" by Liz Rice (talk and code)
- `man namespaces`, `man cgroups`

---

## Phase 10 — Security and Hardening

Protect and audit Linux systems.

- [ ] SELinux fundamentals (modes, contexts, booleans, troubleshooting with `ausearch`)
- [ ] AppArmor fundamentals (profiles, enforcement modes)
- [ ] Firewall hardening (minimal open ports, default deny)
- [ ] SSH hardening (disable root login, key-only auth, fail2ban)
- [ ] File integrity monitoring (`aide`, `tripwire`)
- [ ] Audit framework (`auditd`, `auditctl`, `ausearch`, `aureport`)
- [ ] Encrypted filesystems (LUKS)
- [ ] Rootkit detection (`rkhunter`, `chkrootkit`)
- [ ] CIS Benchmarks — industry standard hardening guides
- [ ] Security updates and patch management strategies

### Suggested resources
- Red Hat Security Guide
- CIS Benchmarks (cisecurity.org)
- "Linux Security Cookbook" by Daniel Barrett

---

## Phase 11 — Performance Monitoring and Tuning

Diagnose bottlenecks and optimize systems.

- [ ] The USE method (Utilization, Saturation, Errors) by Brendan Gregg
- [ ] CPU analysis (`top`, `htop`, `mpstat`, `pidstat`, CPU scheduling)
- [ ] Memory analysis (`free`, `vmstat`, `/proc/meminfo`, OOM killer)
- [ ] Disk I/O analysis (`iostat`, `iotop`, I/O schedulers)
- [ ] Network performance (`iperf3`, `ss`, `netstat`)
- [ ] System-wide tracing (`perf`, `bpftrace`, `ftrace`)
- [ ] eBPF — the modern observability framework
- [ ] Tuning kernel parameters with `sysctl` for performance
- [ ] Understanding load average and CPU saturation
- [ ] Log aggregation and analysis at scale

### Suggested resources
- "Systems Performance" by Brendan Gregg
- Brendan Gregg's Linux performance tools diagram
- Netflix Tech Blog (performance-related posts)

---

## Phase 12 — Infrastructure and Real-World Practice

Tie everything together with hands-on practice.

- [ ] Automate a full server setup with shell scripts
- [ ] Set up a home lab (VMs with VirtualBox/KVM or cloud free tier)
- [ ] Configure a LAMP/LEMP stack from scratch
- [ ] Set up centralized logging (rsyslog or journald remote)
- [ ] Implement backup strategies (`rsync`, `borgbackup`, snapshots)
- [ ] Practice troubleshooting broken systems (intentionally break and fix)
- [ ] Contribute to an open source project that touches Linux internals
- [ ] Take a certification exam (optional but validates knowledge):
  - **LPIC-1 / LPIC-2** (Linux Professional Institute)
  - **RHCSA / RHCE** (Red Hat — highly valued in the industry)
  - **LFCS / LFCE** (Linux Foundation)

### Suggested resources
- KodeKloud Linux Labs
- OverTheWire: Bandit (wargames for command-line practice)
- SadServers (sadservers.com) — fix broken Linux servers

---

## Recommended Books (Full Reading Order)

1. **"How Linux Works"** by Brian Ward — you are already reading this
2. **"The Linux Command Line"** by William Shotts — great for scripting mastery
3. **"UNIX and Linux System Administration Handbook"** by Evi Nemeth — the sysadmin bible
4. **"Linux Kernel Development"** by Robert Love — when ready for kernel internals
5. **"Systems Performance"** by Brendan Gregg — when ready for performance tuning

---

## How to Use This Roadmap

1. **Finish Phase 1** (Track A) and the **Linux Pre-Requirements** (Track B) first
2. **Start both tracks in parallel** — do Docker (Track B Step 1) while studying Phase 2+ (Track A)
3. **Take notes** — add new files to this vault as you learn each topic
4. **Practice daily** — even 30 minutes of hands-on terminal work compounds fast
5. **Let Track B reveal your Track A gaps** — when a DevOps lab exposes a Linux knowledge gap, go study that specific Phase
6. **Break things on purpose** — set up VMs and intentionally cause failures to debug
7. **Build projects** — every DevOps step has a project suggestion. Do them. Theory without practice fades.

> "The only way to learn Linux is to use Linux." — Every sysadmin ever
> "The only way to learn DevOps is to deploy things and watch them break." — Also every sysadmin
