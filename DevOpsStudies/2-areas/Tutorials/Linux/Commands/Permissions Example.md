Let’s learn more about files permissions in Linux

When listing files with `ls -l`, you might encounter an output like
```bash
d rwx r-x ---. 1 root root  0 Jan 30 19:55 permissions
```
Here's what each part signifies:

1.  **`d`**: The file type. 
	* `d` directory, 
	* `-` regular file, 
	* `l` for a symbolic link.
	* `c` character device
	* `b` block device
	* `s` socket file
	* `p` Named pipe
2.  **`rwxr-x---.`**: File permissions, broken into three sets for owner, group, and others. `r` (read), `w` (write), `x` (execute). The trailing `.` indicates an SELinux context.
	* `rwx` Permissions for the owner
	* `r-x` Permissions for the group
	* `---` Permissions for others
3.  **`1`**: The number of hard links to the file or directory.
4.  **`root`**: The username of the file's owner.
5.  **`root`**: The group name of the file's owner.
6.  **`0`**: The size of the file in bytes (or directory entry size).
7.  **`Jan 30 19:55`**: The date and time of the last modification.
8.  **`permissions`**: The name of the file or directory.

## Permission using chmod and ugoa system

The file `hello.txt` below has only Write permission to his owner (The user)

![[linux_hello_file_initial_perms.png]]

Now, we’ll set the permission to the group with the command `chmod`

![[linux_chmod_perm_to_group.png]]

Setting execute permission to the group

Let’s remove the group permission with the same command. As we can see, this could be made with the same syntax, just changing `+` by `-`

![[linux_chmod_remove_perm_to_group.png]]
We removed execute permission to the group

We can also set many permissions at the same time

![[linux_chmod_all_perms_to_user.png]]
We added read, write and execute permissions to the user

Using the syntax with `,` it’s possible to set permissions for user, group and others in one line command

![[linux_chmod_perms_to_user_group_and_others.png]]
We did remove execute permission to user, set write permission to group and remove write permission to others

Now setting the same permission to all the users

![[linux_chmod_set_perms_to_all_users.png]]

All users now have the same permission (read, execute and permissions)

## Permission using chmod and binary

The table below shows the most commonly used permissions when we are using Octal permission based system

| Symbolic | Octal | Meaning |
| --- | --- | --- |
| -rwx - - - - - - | 700 | User can do all; Group and Others can’t do nothing |
| -rwxr-xr-x | 755 | User can do all; Group can read and execute; Others can read and execute also |
| -rw-rw-r- - | 664 | User can read and write; Group can read and write; Others can only read |
| -rw-rw- - - - | 660 | User can read and write; Group can read and write; Others can’t do nothing |
| -rw-r- -r- - | 644 | User can read and write; Group and Others can only read |