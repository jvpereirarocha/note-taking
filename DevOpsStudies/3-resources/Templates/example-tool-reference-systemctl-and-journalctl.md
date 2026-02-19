#reference #systemd #linux #february2026

# systemctl and journalctl — Quick Reference

## What is it?
`systemctl` is the main command to manage services (daemons) on modern Linux systems that use systemd. `journalctl` is its companion for reading logs. Together, they're how you start/stop services and figure out why things broke.

## Installation
Pre-installed on virtually all modern Linux distributions (Fedora, Ubuntu 16+, Debian 8+, RHEL 7+, Arch).

```bash
# verify systemd is running
systemctl --version
```

## Core commands

### Managing services

```bash
# check if a service is running
systemctl status docker

# start a service
sudo systemctl start docker

# stop a service
sudo systemctl stop docker

# restart a service (stop + start)
sudo systemctl restart docker

# reload config without full restart (not all services support this)
sudo systemctl reload nginx

# enable a service to start automatically on boot
sudo systemctl enable docker

# disable auto-start on boot
sudo systemctl disable docker

# enable AND start in one command
sudo systemctl enable --now docker
```

### Checking service state

```bash
# is the service currently running?
systemctl is-active docker
# output: active / inactive

# is the service enabled on boot?
systemctl is-enabled docker
# output: enabled / disabled

# did the service fail?
systemctl is-failed docker
# output: active / failed

# show detailed status (PID, memory, recent logs)
systemctl status docker
```

### Listing services

```bash
# list all running services
systemctl list-units --type=service --state=running

# list all services (including inactive)
systemctl list-units --type=service --all

# list failed services (quick health check)
systemctl --failed
```

### Reading logs with journalctl

```bash
# show all logs for a service
journalctl -u docker

# show only the most recent logs (tail)
journalctl -u docker -n 50

# follow logs in real-time (like tail -f)
journalctl -u docker -f

# show logs since last boot
journalctl -u docker -b

# show logs from a specific time range
journalctl -u docker --since "2026-02-06 10:00" --until "2026-02-06 12:00"

# show logs since a relative time
journalctl -u docker --since "1 hour ago"

# show only error-level and above
journalctl -u docker -p err

# show kernel messages (like dmesg but with timestamps)
journalctl -k
```

### System-wide commands

```bash
# reboot the machine
sudo systemctl reboot

# shut down the machine
sudo systemctl poweroff

# see the boot time breakdown (which services are slow)
systemd-analyze

# see a detailed timeline of service startup
systemd-analyze blame

# see the dependency tree of a service
systemctl list-dependencies docker
```

## Config files

- `/etc/systemd/system/` — custom unit files and overrides (highest priority)
- `/lib/systemd/system/` (or `/usr/lib/systemd/system/`) — unit files installed by packages (don't edit these directly)
- `/etc/systemd/journald.conf` — log storage configuration

To override a package-provided service without editing the original file:

```bash
# creates an override file at /etc/systemd/system/docker.service.d/override.conf
sudo systemctl edit docker

# after editing, always reload the daemon
sudo systemctl daemon-reload
```

## Common patterns

### "I installed something and it's not running"

```bash
# typical post-install workflow
sudo systemctl start <service>     # start it now
sudo systemctl enable <service>    # make it start on boot
systemctl status <service>         # verify it's running
```

### "A service won't start — why?"

```bash
# check status for error hints
systemctl status <service>

# read the full logs
journalctl -u <service> -n 100 --no-pager

# check if it's a dependency issue
systemctl list-dependencies <service>
```

### "I changed a config file but the service didn't pick it up"

```bash
# some services support reload (re-reads config without stopping)
sudo systemctl reload <service>

# if reload isn't supported, restart
sudo systemctl restart <service>

# if you edited a systemd unit file itself, reload the daemon first
sudo systemctl daemon-reload
sudo systemctl restart <service>
```

### DevOps context: managing Docker daemon

```bash
# start Docker and enable on boot
sudo systemctl enable --now docker

# check if Docker is healthy
systemctl status docker

# Docker daemon logs (useful when containers won't start)
journalctl -u docker -f

# restart Docker (warning: stops all running containers)
sudo systemctl restart docker
```

## Gotchas

- **`systemctl enable` does NOT start the service**. It only configures it to start on next boot. Use `enable --now` to do both.
- **`systemctl restart` kills the process**. For web servers with active connections, prefer `systemctl reload` when supported (e.g., Nginx supports it, but not all services do).
- **Editing files in `/lib/systemd/system/` directly gets overwritten on package updates**. Always use `systemctl edit <service>` for overrides.
- **After editing any `.service` file, you must run `systemctl daemon-reload`**. Otherwise systemd keeps using the old version from memory.
- **`journalctl` output disappears on reboot by default on some distros**. To persist logs across reboots, ensure `/var/log/journal/` exists: `sudo mkdir -p /var/log/journal && sudo systemctl restart systemd-journald`.
- **Log priority levels** from most to least severe: `emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`. Use `-p err` to filter noise when troubleshooting.
