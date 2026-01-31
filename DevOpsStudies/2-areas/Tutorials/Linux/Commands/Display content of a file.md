# Display content of a file

```
cat file -> Display the contents of file
more file -> Browse through a text file
less file -> More features than more
head file -> Output the beginning (or top) portion of file
tail file -> Output ending (or bottom) portion of file
```

## Head and Tail

- Displays only 10 lines by default
- Change this behavior with `-n`
    - n = number of lines
    - `tail -15 file.txt`

## Viewing files in real time

```
tail -f file -> Follow the file
```

Displays data as it is being written to the file

### Cat command

The cat command shows all the file content

![[linux_cat_command.png]]

### Head command

The head command, by default, shows only the first 10 lines of a file

![[linux_head_command.png]]

But you can specify how many lines you want to see. In this case we want to see 3 lines only

![[linux_head_command_with_filter.png]]

### Tail command

It works like the head command, but the difference is the tail command shows the last 10 lines if you don’t specify how much lines do you want to see

![[linux_tail_command.png]]

This example below show only the last 2 lines of the file

![[linux_tail_command_with_filter.png]]
### More command

The more command split the file in pages. As we can see below, the script has 81% of its content in the first page. To change to the first page, press `space bar` key or `arrow down`

![[linux_more_command.png]]

To go to the next line, press `Enter`. 

To quit outside from the file, press the key `Q`

### Less command

The less command works similarly. The keybindings are the same of the more command

![[linux_less_command.png]]