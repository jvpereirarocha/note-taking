
### Creating a Collection of Files

```
tar [-] c|x|t f tarfile [pattern]

Create, extract or list contents of a tar archive using pattern, if supplied
```

### tar Options

```
c -> Create a tar archive
x -> Extract file from the archive
t -> Display the table of contents (list).
v -> Be verbose
z -> Use compression
f file -> Use this file
```

**Creating a new tar file**

The command `tar cf`  creates a new `.tar` file
![[linux_tar_command_cf.png]]

Create a docs.tar from mydir directory

**Extracting the file to the /tmp**

The command `tar xf` extract the `docs.tar` to the myfiles-extracted directory in tmp

![[linux_tar_command_xf.png]]
**Using the verbose option**

With the `v` option, we see all the files that are being extracted

![[linux_tar_command_xvf.png]]
### Compressing Files to Save Space

```
gzip -> Compress files
gunzip -> Uncompress files
gzcat -> Concatenates compressed files
zcat -> Concatenates compressed files
```

### Disk usage

```
du -> Estimates file usage
du -k -> Displays sizes in Kilobytes
du -h -> Display sizes in human readable format
```

![[linux_du_command_kilobyte.png]]

This file2.txt has only 4 kb of size


Now, let's see the display when we're using the human readable option
![[linux_du_command_human_readable.png]]

### Compressing file

This example compress the `example` file

![[linux_gzip_command.png]]

Now unziping the file

![[linux_gunzip_command.png]]