
### Copying Files

```
cp source_file destination_file -> Copy source_file to destination_file
cp src_file1 [src_fileN ...] dest_dir -> Copy source_files to destination_directory
cp -i -> Run in interactive mode
cp -r source_directory destination -> Copy src_directory recursively to destination
```

The example below show the difference between to files: `file1.txt` and `file2.txt`

![[linux_command_diff_two_files.png]]

The file1.txt has content. But the file2.txt has nothing

Now let’s copy the `file1.txt` to the `file2.txt` and get the difference between the two files again

![[linux_command_diff_files_same_content.png]]

As we can see, the two files now have the same content

Copying all the files to the `mydir` directory

![[linux_command_cp_to_dir.png]]

Copying directory command to another directory. In this case, the new directory has been created

![[linux_command_cp_recursive.png]]