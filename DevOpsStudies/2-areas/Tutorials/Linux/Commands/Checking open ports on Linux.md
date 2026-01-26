,To check open ports on Linux, run any one of the following commands:

```
sudo lsof -i -P -n | grep LISTEN
```

The output is:
![[linux_lsof_i_p_command.png]]


```
sudo netstat -tulpn | grep LISTEN
```

Output:
![[linux_netstat_tulpn_command.png]]


```
sudo ss -tulpn | grep LISTEN
```

Output:
![[linux_ss_tulpn_command.png]]


```
sudo lsof -i:80 ## see a specific port such as 80 ##
```

Output:
![[linux_lsof_i__specific_port_command.png]]


```
sudo nmap -sTU -O <ip_address>
```

To see how to get your IP address, check this link [[Network commands on Linux#IP command|Checking IP address]]


Output:
![[linux_nmap_check_status.png]]

[[Check ports linux commands article]]

#linux/commands #network