
## The grep command

The grep command is a powerful pattern to search files on Linux based systems. Your sintax allows you to make patterns to find some files as you want

```bash
grep [options] [pattern] [file]

Options:
-i -> ignore case sensitive
-v -> invert match (select non-matching lines)
-c -> count the occurrences
```

### Examples using grep

- Searching the keyword root into the `users-passwd.txt` file

![Untitled](Searching%20files%20and%20Pipe%20operator/Untitled.png)

Under the hood, when we use the grep command we are using something with the pipe operator and the command cat

![This command has the same effect of the previous command, as you can see](Searching%20files%20and%20Pipe%20operator/Untitled%201.png)

This command has the same effect of the previous command, as you can see

- Ignoring and not ignoring case sensitive + using the invert match pattern (searching non-matching words)

![Untitled](Searching%20files%20and%20Pipe%20operator/Untitled%202.png)

- Counting the number of occurrences of the root keyword in the `users-passwd.txt` file

![Only 1 line was found with the “root” word. Then, the -ci option returned the number 1; Otherwise, using the non-matching pattern, with the -cv option, we found 14 lines](Searching%20files%20and%20Pipe%20operator/Untitled%203.png)

Only 1 line was found with the “root” word. Then, the -ci option returned the number 1; Otherwise, using the non-matching pattern, with the -cv option, we found 14 lines

## The file command

The file command shows infos about the selected file

```bash
file [filename]
```

- Viewing the file description

![Untitled](Searching%20files%20and%20Pipe%20operator/Untitled%204.png)

Viewing the file description with the -i option

![This option -i show us the mime type of the file. In this case, text/plain](Searching%20files%20and%20Pipe%20operator/Untitled%205.png)

This option -i show us the mime type of the file. In this case, text/plain

## The cut command

This command is used to cut a word of a file using a delimiter and finding the Nth key

```bash
cut [options] [file]

-d -> delimiter
-fx,y -> the range of words to get
```

### Example of cut command

- Find the two first words in the `configs.txt` file using space as delimiter

![-d delimiter used here is ‘ ‘ to tell to the system that we want space as delimiter](Searching%20files%20and%20Pipe%20operator/Untitled%206.png)

-d delimiter used here is ‘ ‘ to tell to the system that we want space as delimiter

Let’s change the `configs.txt` file

![we have now a / character](Searching%20files%20and%20Pipe%20operator/Untitled%207.png)

we have now a / character

- Getting the last two found sentences using / as delimiter

![the line with the content author: jvictor hasn’t the delimiter / then this returns all the content of the line](Searching%20files%20and%20Pipe%20operator/Untitled%208.png)

the line with the content author: jvictor hasn’t the delimiter / then this returns all the content of the line

## The pipe operator

The pipe operator is a powerful pattern we can use to combine inputs and outputs commands

```bash
output command | input command
```

Also, is possible to use the pipe operator with more than 2 pipes

```bash
output command | output command | output command | input command
```

### Examples of using of the pipe operator

- Finding the 10 first users of the /`etc/passwd` that contains the keyword **bin**

![As we can see, there’s a lot of users with this keyword](Searching%20files%20and%20Pipe%20operator/Untitled%209.png)

As we can see, there’s a lot of users with this keyword

- Finding the 3 last users of the `/etc/passwd` that contains the keyword **bin**, getting only the first word

![Untitled](Searching%20files%20and%20Pipe%20operator/Untitled%2010.png)

- Now finding the 5 last users of the /etc/passwd file and using head as command input to get only the three first results

![We can combine as many pipes as possible](Searching%20files%20and%20Pipe%20operator/Untitled%2011.png)

We can combine as many pipes as possible