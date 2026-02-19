This is a "tree" with all directories of Linux

![[linux_fhs.png]]

✦ The Linux Filesystem Hierarchy Standard (FHS) defines the structure of directories and their contents in Linux and other Unix-like operating systems. It ensures that specific types of files are always found in predictable locations, making the system more organized and easier to manage.  
  
 Here's a breakdown of some of the most important directories:  
  
 Root Directory (/)  
 The top-level directory of the entire file system. All other directories branch off from here.  
  
 Essential System Directories  
  
  * `/bin` (Binaries)  
      * Contains essential command-line binaries (executables) that are required for the system to boot up and for basic system operations.  
      * Examples: ls, cp, mv, cat, bash.  
  
  * `/boot` (Boot Loader Files)  
      * Contains files required for the boot process, such as the Linux kernel, initial RAM disk (initrd), and boot loader (GRUB, LILO) configuration files.  
      * This directory is crucial for starting the system.  
  
  * `/dev` (Devices)  
      * Contains device files that represent hardware devices (e.g., hard drives, USB devices, terminals, printers). These are not actual files but interfaces to devices.  
      * Examples: /dev/sda (first SATA disk), /dev/tty0 (virtual console).  
  
  * `/etc` (Etc/Editable Text Configuration)  
      * Contains system-wide configuration files for all installed programs and services. These are typically static text files.  
      * Examples: /etc/passwd, /etc/fstab, /etc/hosts, /etc/default/grub.  
  
  * `/home` (User Home Directories)  
      * Contains personal directories for regular users. Each user usually has a subdirectory here (e.g., /home/jvictor).  
      * User-specific data, configuration, and documents are stored here.  
  
  * `/lib` (Libraries)  
      * Contains essential shared libraries needed by the executables in /bin and /sbin.  
      * /lib64 exists on 64-bit systems for 64-bit libraries.  
  
  * `/media` (Removable Media)  
      * Mount point for removable media like USB drives, CD-ROMs, and external hard drives.  
  
  * `/mnt` (Mount Point)  
      * A temporary mount point for manually mounted file systems (e.g., network file systems, partitions).  
  
  * `/opt` (Optional Application Software)  
      * Used to install optional or third-party software packages that are not part of the standard system.  
        Often, self-contained software packages are installed here.  
  
  * `/proc` (Process Information Pseudo-filesystem)  
      * A virtual file system that provides information about running processes and kernel parameters. It contains "files" that provide real-time system data.  
      * Examples: /proc/cpuinfo, /proc/meminfo, directories for each running process (e.g., /proc/1234).  
  
  * `/root` (Root User's Home Directory)  
      * The home directory for the root (administrator) user. It's separate from /home to ensure root can log in even if /home is on a separate, unmounted partition.  
  
  * `/run` (Runtime Variable Data)  
      * Stores volatile runtime data, such as process IDs (PIDs), sockets, and other temporary files needed by applications during their operation. This directory is typically a tmpfs (RAM filesystem) and is cleared on boot.  
  
  * `/sbin` (System Binaries)  
      * Similar to /bin, but contains essential system administration binaries that are usually only run by the root user or require elevated privileges.  
      * Examples: fdisk, mkfs, ifconfig (though many have moved to /usr/sbin).  
  
  * `/srv` (Service Data)  
      * Contains site-specific data served by the system, such as data for web servers (e.g., /srv/www), FTP servers, or CVS repositories.  
  
  * `/sys` (System Filesystem)  
      * A virtual file system similar to /proc, providing an interface to kernel data structures and hardware devices connected to the system. It exposes kernel objects and their properties.  
  
  * `/tmp` (Temporary Files)  
      * A directory for temporary files created by users and applications. Contents are typically cleared on system reboot or periodically.  
  
  * `/usr` (Unix System Resources)  
      * Historically stood for "Unix Software Resources" or "User System Resources." It contains the majority of user utilities and applications, documentation, libraries, and other shared resources that are not essential for system boot.  
      * `/usr/bin`: Most user commands.  
      * `/usr/lib`: Non-essential shared libraries.  
      * `/usr/local`: Locally installed software that is not managed by the distribution's package manager.  
      * `/usr/sbin`: Non-essential system administration binaries.  
      * `/usr/share`: Architecture-independent data (e.g., documentation, fonts, icons).  
  
  * `/var` (Variable Data)  
      * Contains variable data files, meaning files whose content is expected to change during normal system operation.  
      * `/var/log`: System log files (e.g., /var/log/syslog, /var/log/auth.log).  
      * `/var/mail`: User mailboxes.  
      * `/var/spool`: Spool directories for tasks like printing and mail queues.  
      * `/var/tmp`: Larger temporary files that should be preserved across reboots, unlike /tmp.  
  
 Less Common but Still Standard Directories  
  
  * `/cdrom`: (Often a symlink to /media/cdrom) Mount point for CD-ROMs.  
  * `/lost+found`: Stores recovered fragments of files after a file system check (e.g., fsck). Each partition has its own lost+found directory.  
  
 This hierarchical structure is fundamental to how Linux systems operate and helps maintain order and consistency across different distributions.