
## The command find

Recursively finds files in path that match the expression. If no arguments are supplied, it finds all files in the current directory

```
find [path...] [expression]
```

```
-name pattern -> Find files and directories that match pattern
-iname pattern -> Like -name, but ignores case.
-ls -> Performs an ls on each of the found items
-mtime days -> Finds files that are days old.
-size num -> Finds file that are of size num
-newer file -> Finds file that are newer than file
-exec command {} \; -> Run command against all the files that are found
```

## Examples

This example below shows how the case sensitive matters in Linux commands

![[linux_find_command_case_sensitive.png]]

With the command `find -name networkmanager` nothing was found but, ignoring the sensitive case with the command `find -iname networkmanager` we can see there’s a result

### Matching files with the command find and *

The example below show us how to find a file with some letter 

using the directive `-name[-iname] ‘*’`

![[linux_find_command_wildcard.png]]

We have 3 files and, when we find using ‘*n’ nothing was found because we don’t have any file that contains the letter n. But we have one file that starts with this letter then we get a result searching by the directive ‘n*’, as we can see

### Matching files by -mtime

Let’s search files in the directory `/usr/bin` between 3 and 5 days

![[linux_find_command_mtime.png]]

All this file were created at least 3 days ago and less than 5 days

### Matching files using -ls

We can use multiple directives to find a file. We can use something like that to find some files that contains the letter g, created between 3 and 10 days ago and get them details using -`ls`

![[linux_find_command_with_ls.png]]

All these files are found searching by the command specified

### Matching files by size

Let’s search files that contains more than 5 MB in the Downloads directory

![[linux_find_command_by_size.png]]

Now searching by all the files that have more than 1GB in the work folder

![[linux_find_command_gte_1_giga.png]]

### Matching files by -newer directive

In this example we will find files in the `Downloads` directory that are newer than the file `steam_latest.deb`

![[linux_find_command_newer_directive.png]]

### Executing a command with find option

The example below executes all the files in the directory if we don’t specify anything and shows what each file represents

![[linux_find_command_executing_another.png]]