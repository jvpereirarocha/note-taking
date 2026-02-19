# Practices in linux terminal - 13/02/2026

## Symbolic links
It redirects a link to another place, using symbolic links. Ex:
```bash
ln -s hello.py /home/user/myscript
```
The command creates a symbolic link of hello.py file into /home/user root directory, creating a file called myscript. Then, when we run the command `ls -l` into `/home/user` directory, we can see something like:
```bash
myscript -> /path/hello.py
```
It indicates the file myscript points to hello.py

## Archiving and Compressing files
### Gzip

The GZIP (GNU Zip) is a compress file archive. To use it, we can do:
```bash
gzip file
```
This command will compress the file, in the current directory, adding `.gz` as extension. This command won't create another file. It only changes the extension of the target file

To unzip the file, we should run:
```bash
gunzip file.gz
```
This will uncompress the file into current directory, back it to the original name

### Tar
The tar command is another compress files option. The GZIP command doesn't create another file. The tar command do that. To create a tar file, we can run:
```bash
tar -cvf newfile.tar file1 file2 file3 ...
```
This command creates a file called `newfile.tar` adding inside the files 1, 2, 3 and so on.
> The option `c` indicates creation of a new file
> The option `v` indicates verbose. It shows what's happening while the command is running
> The option `f` indicates the file(s) you want to pass to `.tar` new file. You can pass a list of files

To list all files inside of a `.tar` file we can use the command below:
```bash
tar -tvf newfile.tar
```
> The option `-t` indicates to show the list of contents of a `.tar` archive
> The option `-v` indicates verbose
> The option `-f` indicates the `.tar` file we want to see the content

### Checking disk space
The command `df -h /etc /home` checks the disk space and more informations about the directories `home` and `etc`
```bash
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda4       431G  282G  127G  69% /
/dev/sdb1       458G  132G  303G  31% /home
```

### Checking file space
To estimate file space usage, we can use the command below
```bash
du -h /home/jvictor/Documents/personal | tail -5
```
> Checking all files spaces usage with the `du` command and redirecting it to show only the last 5 lines using the command `tail`

The output will be:
```bash
504K	/home/jvictor/Documents/personal/company/extratos_contabeis
1.2M	/home/jvictor/Documents/personal/company/NFEs
208K	/home/jvictor/Documents/personal/company/invoices
3.6M	/home/jvictor/Documents/personal/company
7.1M	/home/jvictor/Documents/personal
```

### Checking active services with systemctl command from systemd
```bash
systemctl list-units --type=service --state=running
```

The output will be:
```bash
  UNIT                                         LOAD   ACTIVE SUB     DESCRIPTION
  abrt-journal-core.service                    loaded active running ABRT coredumpctl message creator
  abrt-oops.service                            loaded active running ABRT kernel log watcher
  abrt-xorg.service                            loaded active running ABRT Xorg log watcher
  abrtd.service                                loaded active running ABRT Daemon
  accounts-daemon.service                      loaded active running Accounts Service
  alsa-state.service                           loaded active running Manage Sound Card State (restore and store)
  atd.service                                  loaded active running Deferred execution scheduler
  auditd.service                               loaded active running Security Audit Logging Service
  avahi-daemon.service                         loaded active running Avahi mDNS/DNS-SD Stack
  chronyd.service                              loaded active running NTP client/server
  containerd.service                           loaded active running containerd container runtime
  crond.service                                loaded active running Command Scheduler
  cups.service                                 loaded active running CUPS Scheduler
  dbus-:1.3-org.freedesktop.problems@0.service loaded active running dbus-:1.3-org.freedesktop.problems@0.service
  dbus-broker.service                          loaded active running D-Bus System Message Bus
  docker.service                               loaded active running Docker Application Container Engine
  firewalld.service                            loaded active running firewalld - dynamic firewall daemon
  gssproxy.service                             loaded active running GSSAPI Proxy Daemon
  httpd.service                                loaded active running The Apache HTTP Server
  irqbalance.service                           loaded active running irqbalance daemon
  memcached.service                            loaded active running memcached daemon
  ModemManager.service                         loaded active running Modem Manager
  NetworkManager.service                       loaded active running Network Manager
  pcscd.service                                loaded active running PC/SC Smart Card Daemon
  polkit.service                               loaded active running Authorization Manager
  rsyslog.service                              loaded active running System Logging Service
  rtkit-daemon.service                         loaded active running RealtimeKit Scheduling Policy Service
  sddm.service                                 loaded active running Simple Desktop Display Manager
  smartd.service                               loaded active running Self Monitoring and Reporting Technology (SMART) Daemon
  snap.lxd.daemon.service                      loaded active running Service for snap application lxd.daemon
  snapd.service                                loaded active running Snap Daemon
  switcheroo-control.service                   loaded active running Switcheroo Control Proxy service
  systemd-homed.service                        loaded active running Home Area Manager
  systemd-journald.service                     loaded active running Journal Service
  systemd-logind.service                       loaded active running User Login Management
  systemd-machined.service                     loaded active running Virtual Machine and Container Registration Service
  systemd-oomd.service                         loaded active running Userspace Out-Of-Memory (OOM) Killer
  systemd-resolved.service                     loaded active running Network Name Resolution
  systemd-udevd.service                        loaded active running Rule-based Manager for Device Events and Files
  systemd-userdbd.service                      loaded active running User Database Manager
  tuned-ppd.service                            loaded active running PPD-to-TuneD API Translation Daemon
  tuned.service                                loaded active running Dynamic System Tuning Daemon
  udisks2.service                              loaded active running Disk Manager
  upower.service                               loaded active running Daemon for power management
  uresourced.service                           loaded active running User resource assignment daemon
  user@1000.service                            loaded active running User Manager for UID 1000

Legend: LOAD   → Reflects whether the unit definition was properly loaded.
        ACTIVE → The high-level unit activation state, i.e. generalization of SUB.
        SUB    → The low-level unit activation state, values depend on unit type.

46 loaded units listed.
```

