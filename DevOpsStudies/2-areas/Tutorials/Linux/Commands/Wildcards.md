
Wildcards are string of patterns used to manipulating files and folders on Linux systems. This pattern can be used with the commands `ls`, `rm`, `mv`, `cp`, etc.

## Patterns

```
* -> matchs zero or more of the used criteria

? -> matchs exactly one character

[pattern] -> used to get all patterns on the brackets.
Could be used to find only words that start with a, e, i, o or u, for example

! -> used to negative patterns

\ -> used to scape characters
```

### Default patterns

There are default patterns when we would use the wildcard syntax

```
[[:alpha:]] -> only letters
[[:alnum:]] -> only letters and numbers
[[:digit:]] -> only digits
[[:lower:]] -> only files that match the lower case name
[[:upper:]] -> only files that match the upper case name
[[:space:]] -> words that have space
```