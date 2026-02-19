# Some tips to help on linux environment
## Looking for a command without know, filtering by a keyword
```bash
man -k find
```
This command will find out all the manuals that contains the word `find`

The output will be something like:
```bash

abrt-action-find-bodhi-update
(1) - find bodhi update based on ABRT's problem dir
btrfs-find-root (8)  - filter to find btrfs root
debuginfod-find (1)  - request debuginfo-related data
dracut-initqueue.service (8) - runs the dracut main loop to find the real root
ffs (3)              - find first bit set in a word
ffsl (3)             - find first bit set in a word
ffsll (3)            - find first bit set in a word
find (1)             - search for files in a directory hierarchy
findfs (8)           - find a filesystem by label or UUID
findmnt (8)          - find a filesystem
glob (3)             - find pathnames matching a pattern, free memory from glob()
globfree (3)         - find pathnames matching a pattern, free memory from glob()
gst-typefind-1.0 (1) - print Media type of file
ippfind (1)          - find internet printing protocol printers
kfind (1)            - file find utility by KDE
lfind (3)            - linear search of an array
locate (1)           - find files by name, quickly
mysql_find_rows (1)  - extract SQL statements from files (mysql_find_rows is now a symlink to maria...
pidof (1)            - find the process ID of a running program
plocate (1)          - find files by name, quickly
Pod::Simple::Search (3pm) - find POD documents in directory trees
readtags (1)         - Find tag file entries matching specified names
sane-find-scanner (1) - find SCSI and USB scanners and their device files
systemd-delta (1)    - Find overridden configuration files
tep_find_any_field (3) - Search for a field in an event.
tep_find_common_field (3) - Search for a field in an event.
tep_find_event (3)   - Find events by given key.
tep_find_event_by_name (3) - Find events by given key.
tep_find_event_by_record (3) - Find events by given key.
tep_find_field (3)   - Search for a field in an event.
tep_find_function (3) - Find function name / start address.
tep_find_function_address (3) - Find function name / start address.
tep_find_function_info (3) - Find function name / start address.
tep_record_is_event (3) - Find events by given key.
tfind (3)            - manage a binary search tree
tracer (8)           - finds outdated running applications in your system
ts_finddev (1)       - Discover touch screen devices.
ts_setup (3)         - find, open and configure a touch screen input device
ttyslot (3)          - find the slot of the current user's terminal in some file
xdg-user-dir (1)     - Find an XDG user dir
```

### Manual sections
1. User commands
2. Kernel system calls
3. Higher-level Unix programming library documentation
4. Device interface and driver information
5. File descriptions (system configuration files)
6. Games
7. File formats, conventions, and encodings (ASCII, suffixes, and so on)
8. System commands and servers

To see a specific manual section, use the `man` command as below:
```bash
man 5 passwd
```
The command will show the passwd command's file descriptors manual
