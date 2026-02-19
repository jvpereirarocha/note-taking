
```
locate pattern
```

- List files that match pattern
- Faster than the find command
- Queries an index
- Results are not in real time
- May not be enabled on all systems

![[linux_locate_command.png]]

Using locate to get all files that contains the keyword uptime

### Understanding the index query

The index query that uses the command locate doesn’t show all the results in real time. In the example below we’ve created a new file with the extension `.rb` but, as we can see, the new file was not found with the locate command because the index was not queried by the command yet

![[linux_locate_command_index_query.png]]

The .rb pattern using the command locate didn’t show the file new-file.rb because of the command index query