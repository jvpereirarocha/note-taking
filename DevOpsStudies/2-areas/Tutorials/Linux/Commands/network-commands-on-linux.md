## IP command

1. Checking network interfaces:
```
ip link show
```
The output will be:
![[linux_ip_link_show.png]]

 2. Check IP addresses from all network interfaces
```
ip addr show
```
The output is:
![[linux_ip_addr_show.png]]


To filter by interface:
```
ip addr show <interface>
```

Example:
```
ip addr show enp3s0
```

Output will be:
![[linux_ip_addr_show_interface.png]]


3. Check or adjust ip routing table
```
ip route [subcommand] [options] [destination]
```
Available subcommands:
* `show` -> Shows the routing table
* `add` -> Adds a new route to table
* `del` -> Deletes a route from the table
* `change` -> Modifies an existing route

The `[destination]` parameter determines where the traffic is directed. Additional options help control the traffic flow further. Example:
```
ip route show | grep enp3s0
```

Output:
![[linux_ip_route_show_interface.png]]


## Dig command
This command queries Domain Name System (DNS) and finds information for DNS records. The command collects domain name information and associate records. 
Click here to learn more about DNS -> [[DNS concepts]]

Example: 
```
dig google.com
```

Output:
![[linux_dig_command_google.png]]

It is possible to provide the IP address to perform a reverse DNS lookup. To know more about DNS click on [[DNS concepts]]

Example:
```
dig -x 8.8.8.8
```

The output:
![[linux_dig_command_reverse_lookup.png]]


## Traceroute
This command tracks the route a packet take to reach a destination on a TCP/IP network. The command is used to discover routing issues and bottlenecks by showing a packet's intermediate hops while traveling from source to destination. The default trace is 30 hops with a packet size of 60 bytes for IPv4 (and 80 bytes for IPv6)

Example:
```
traceroute 8.8.8.8
```

The output:
![[linux_traceroute_google_dns.png]]

[[Linux network commands article]]


#linux/commands #network 