## RAM / Memory

- `sudo dmidecode -t memory` — Detailed info: manufacturer, speed, type (DDR4/DDR5), slots, size per stick
- `lshw -short -C memory` — Summary of memory hierarchy
- `free -h` — Current memory usage

## CPU

- `lscpu` — Model, cores, threads, cache, architecture
- `cat /proc/cpuinfo` — Per-core detailed info

## Storage / Disks

- `lsblk` — List all block devices (disks, partitions)
- `sudo fdisk -l` — Partition tables and disk sizes
- `sudo smartctl -a /dev/sda` — Disk health (needs `smartmontools`)

## USB Devices

- `lsusb` — List all connected USB devices
- `lsusb -v` — Verbose details

## PCI Devices (GPU, network cards, etc.)

- `lspci` — List all PCI devices
- `lspci -v` — Verbose (shows driver in use, memory regions)

## General Hardware Overview

- `sudo lshw -short` — Full hardware summary in a compact table
- `inxi -Fz` — User-friendly system overview (may need installing)
- `hostnamectl` — Basic system/OS info

## Input Devices (keyboard, mouse, etc.)

- `xinput list` — List input devices (X11)
- `cat /proc/bus/input/devices` — Kernel-level input devices

## Network

- `ip link` — Network interfaces
- `lspci | grep -i net` — Network hardware

## Battery / Power (laptops)

- `upower -i /org/freedesktop/UPower/devices/battery_BAT0`
