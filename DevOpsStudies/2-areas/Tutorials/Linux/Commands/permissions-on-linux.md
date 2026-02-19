
# Understanding Linux Permissions

## Symbolic permissions

```bash
ls -l
-rw-rw-r-- 1 jvpr users 10400 Jun 13 23:58 test.txt
```

| Symbol | Type |
| --- | --- |
| - | Regular file |
| d | Directory |
| l | Symbolic link |
| r | Read |
| w | Write |
| x | Execute |

| Permission | File | Directory |
| --- | --- | --- |
| Read (r) | Allows a file to be read | Allows file names in the directory to be read |
| Write (w) | Allows a file to modified | Allows entries to be modified within the directory |
| Execute (x) | Allows the execution of a file | Allows access to contents and metadata for entries |

### Permission Categories

| Symbol | Category |
| --- | --- |
| u | User |
| g | Group |
| o | Other |
| a | All |

### Groups

- Every user is in at least one group
- Users can belong to many groups
- Groups are used to organize users
- The `groups` command displays a user’s groups
- You can also use `id -Gn`

![[linux_id_gn.png]]

### Secret Decoder Ring

```bash
-rw-r--r-- 1 bob users 10400 ...
```

Order:

Type: -

User: rw-

Group: r- -

Other: r - -

## Change permissions on Linux

| Item | Meaning |
| --- | --- |
| chmod | Change mode command |
| ugoa | User category: user, group, other, all |
| +-= | Add, subtract, or set permissions |
| rwx | Read, Write, Execute |

## Numeric Based Permissions

| r | w | x |  |
| --- | --- | --- | --- |
| 0 | 0 | 0 | Value for off |
| 1 | 1 | 1 | Binary value for on |
| 4 | 2 | 1 | Base 10 value for on |

| Octal | Binary | String | Description |
| --- | --- | --- | --- |
| 0 | 0 | - - - | No permissions |
| 1 | 1 | - - x | Execute Only |
| 2 | 10 | - w - | Write only |
| 3 | 11 | -wx | Write and execute (2 + 1) |
| 4 | 100 | r- - | Read only |
| 5 | 101 | r-x | Read and execute (4 + 1) |
| 6 | 110 | rw- | Read and write (4+2) |
| 7 | 111 | rwx | Read, write, and execute (4 + 2 + 1) |

Order has Meaning

|  | U | G | O |
| --- | --- | --- | --- |
| Symbolic | rwx | r-x | r - - |
| Binary | 111 | 101 | 100 |
| Decimal | 7 | 5 | 4 |

OBS: There’s no space between hifens when run the command on terminal

### Commonly Used Permissions

| Symbolic | Octal |
| --- | --- |
| -rwx - - - - - - | 700 |
| -rwxr-xr-x | 755 |
| -rw-rw-r- - | 644 |
| -rw-rw- - - - | 660 |
| -rw-r- -r- - | 644 |

[[Permissions Example]]

[[Groups permission examples]]

## Directory Permissions Revisited

- Permissions on a directory can affect the files in the directory
- If the file permissions look correct, start checking directory permissions
- Work your way up to the root

## File Creation Mask

- File creation mas determines default permissions
- If no mask were used permissions would be:
    - 777 for directories
    - 666 for files
    

## Umask command

`umask [-S] [mode]`

- Sets the file creation mask to mode, if given
- Use -S to for symbolic notation

Let’s check umask from the current directory we working on

![[linux_umask.png]]

Now let’s set to the umask 0007

![[linux_umask_0007.png]]

Now, when we create a directory, his permission will be read, write and execute to user and group but others can’t do anything

![[linux_umask_s_creating_new_dir.png]]