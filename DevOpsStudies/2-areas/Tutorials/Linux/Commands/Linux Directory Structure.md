# Linux Directory Structure

# Common Structure

- “/” root - Top of the file system hierarchy
- /root - home directory for the superuser
- /bin - binaries and other executables programs
- /lib - essential libraries shared by kernel modules
- /etc - system configuration files
- /home - home directories (like Download, Documents, Pictures)
- /opt - optional or third party software
- /tmp - temporary space typically cleared on reboot
- /usr - user related programs
- /var - variable data; most notably log files

# Comprehensive Directory Listing

- /root - the top of the file system hierarchy
- /bin - Binaries and another executable programs
- /boot - Files needed to boot the operating system
- /cdrom - mount point for CD-Roms
- /cgroup  - control group hierarchy
- /dev - Device files typically controlled by the operating system and the system administrators
- /etc - System configuration files
- /export - shared file systems
- /home - home directories (download, documents, pictures, musics)
- /lib - system libraries
- /lib64 - system libraries 64 bits
- /lost+found - used by file system to store recovered files after a file system check has been performed
- /media - used to mount removable media like CD-ROM
- /mnt - used to mount external file systems
- /opt - optional or third part software
- /proc - provides info about running processes
- /root - the home directory for the root account
- /sbin - system administration binaries
- /selinux - used to display info about SELinux
- /srv - contains data which is served by the system
- /srv/www - web server files
- /srv/ftp - FTP Files
- /sys - Used to display and sometimes to configure the devices known to the Linux Kernel
- /tmp - Temporary space typically cleared on reboot
- /usr - user related programs, libraries and docs
- /usr/bin - Binaries and others executables programs
- /usr/lib - libraries
- /usr/local - Locally installed software that is not part of the base operating systems
- /usr/sbin - system administrations binaries
- /var - variable data, most notably log files
- /var/log - log files

# Application Directory Structure

Let’s see an example of program that is not part of the base program system called crashplan

- /usr/local/crashplan/bin - path to see the binaries files of the program
- /usr/local/crashplan/etc - path to configure the crashplan behavior
- /usr/local/crashplan/lib - the program files
- /usr/local/crashplan/log - the program log

If you want to install an optional software, like AVG, the application directory structure will be something like:

- /opt/avg/bin
- /opt/avg/etc
- /opt/avg/lib
- /opt/avg/log

Another directory structure possibility is:

- /etc/opt/myapp
- /opt/myapp/bin
- /opt/myapp/lib
- /var/opt/myapp

Sometimes any softwares they’re not given their own directory structure. In this case, the directory structure is:

- /usr/local/bin/myapp
- /usr/local/etc/myapp.conf
- /usr/local/lib/libmyspp.so

Another common pattern is to use the /opt/organization name

- /opt/acme
- /opt/acme/bin
- /opt/acme/etc

Or, /opt/organization/product

- /opt/google/earth
- /opt/google/chrome