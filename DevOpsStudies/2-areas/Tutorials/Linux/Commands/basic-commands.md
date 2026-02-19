# Basic Commands

List of commands:

**uname** - show info about the computer

**sudo** - executes a command as superuser

**ls** - lists directory contents

**cd** - changes the current directory

**pwd** - displays the present working directory

**cat** - concatenates and displays files

**echo** - displays arguments to the screen

**man** - displays the online manual

**exit** - Exits the shell or your current session

**clear** - Clears the screen

**free** - show how much memory the system is using

**shutdown** - turn off the machine

## ls options

-l long listing format

### Rename many files

To remove the prefix “ok_”, execute:

```python
for file in ok_*; do mv "$file" "${file#ok_}";done;
```

### Grep command

The grep command is used to search text and strings in a given file

Examples:

```bash
grep 'word' filename.extension
```

Search man pages by using `man -k <command>`

![[linux_man_command.png]]