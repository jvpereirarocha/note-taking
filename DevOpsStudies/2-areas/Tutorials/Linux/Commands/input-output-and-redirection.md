### I/O names

The input and output are represented by standard input (`stdin`), standard output (`stdout`) and standard error (`stderr`)

| I/O Name | Abbreviation | Number on files |
| --- | --- | --- |
| Standard Input | stdin | 0 |
| Standard Output | stdout | 1 |
| Standard Error | stderr | 2 |

### Redirections

There are three types of redirections: 

- >
- >>
- <

```bash
> Redirects standard output to a file
Overwrites (truncating) existing contents

>> Redirects standard output to a file
Appends to any existing contents

< Redirects input from a file to a command
```

### Common types of redirection

`&` → Used with redirection to signal that a file descriptor is being used

`2>&1` → Combine Standard Error (`stderr`) and Standard Output (`stdout`)

`2>file` → Redirect Standard Error (`stderr`) to a file

### The null device

`>/dev/null` → Redirect output to nowhere

### Examples

**Using input redirect to using a file content into a command**

![[linux_redirect_from_input_to_a_file.png]]

We have a file called `file.txt` with 3 sentences. We’ve using the command sort with input redirect to sort the `file.txt` content

Now, let’s create a new file with the sorted content

![[linux_redirect_from_input_to_a_file_then_output_to_other_file.png]]

We’ve used the same command as you can see, the difference is that now we’ve saved the content of the command into another file called `sorted-file.txt` using the output redirect

**Appending new content to a existing file**

Using the `>>` we can append new content to a existing file

![[linux_redirect_append_content_to_existing_file.png]]

We’ve appended a new phrase “Hello, World” to the `file.txt` using the redirection syntax `>>`

**Separating output and error in two different files**

in the example below we’ll try to list a file (`myfile.txt`) that doesn’t exists. Only the `file.txt` exists

![[linux_redirect_ls_not_found_files.png]]

Now let’s save the command content in two different files. A `result.txt` and `err.txt`

![[linux_redirect_separating_stdout_stderr.png]]

When using the standard output (`stdout`) I/O we can omit the `1>` syntax and use only `>` as you can see in the command `>result.txt

**Combining error and output in the same file**

Let’s create another file called `content.txt` and set the `stdout` and the `stderr` in the same file

![[linux_redirect_combine_stdout_stderr_same_file.png]]

The `stdout` and `stderr` are now in the `content.txt` file. We combined the two I/O with the syntax `>content.txt 2>&1` where` 2>&1` is used to tell to the system that we want to save `stderr(2)` and `stdout(1)` in the same file (`content.txt`)

We can use this notation to append content in the same `content.txt` file, as we can see below

![[linux_redirect_append_stdout_stderr_same_file.png]]

The old content wasn’t overrated by the I/O command

**OBS: The order matters! The command always should be 2>&1**

**Throwing away Standard Errors or Standard Outputs**

We can use the special redirection `/dev/null` to throw away a `stdout` or a `stderr`

The first example we only want to save into the file `success.txt` the `stdout` content

![[linux_redirect_throwing_away_stderr_saving_stdout.png]]

Now, in the second example, we want to save in the `fail.txt` the `stderr` content

![[linux_redirect_throwing_away_stdout_saving_stderr.png]]

As mentioned early we can omit the `1>/dev/null` in this case. The syntax `>/dev/null` would have the same effect here

**Throwing away stdout and stderr**

Let’s throw away the `stdout` and the `stderr` I/O

![[linux_redirect_throwing_away_stdout_stderr.png]]

Final example with all redirects
![[linux_redirect_final_examples.png]]