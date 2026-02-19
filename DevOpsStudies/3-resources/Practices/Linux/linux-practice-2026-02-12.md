## Examples of practices in linux terminal

Ex:
```bash
find /home/user/Documents -iname test*
```
In the example above we're searching files that starts with the word "test" and are located on /user/Documents directory. The `-iname` ignores case sensitive.

```bash
ls -l
```
This examples list all files on current directory showing details about permissions, timestamp, and so on

```bash
grep root /etc/passwd
```
The example of `grep` shows all lines or input streams that contains the word `root` on `/etc/passwd` file

```bash
grep xa /usr/share/dicts/word | tail -5
```
The command above get only words that contains `xa` with `grep` and redirects to `tail` command that shows only the last 5 words (from bottom to top of the list)

```bash
file hello.py
```
The command shows info about the specified file (in this case `hello.py`

```bash
cat /etc/passwd | grep -i root | head -1
```
This command gets the output of the `/etc/passwd` file, redirects it to `grep` command to filter by word `root` then redirects the output of `grep` to `head` command. The `head` command only shows the first line, ignoring the others

```bash
sudo useradd -M [username] -g [group]
```
This command needs to be run as superuser. You must to replace the username with the username you want and the group with an existing group name
