# Commands

## Ifconfig

This command display information about network adapters such as wireless adapter and LAN adapters

![[linux_network_if_config.png]]

## Ip Addresses

To show IP addresses, we can run the command `ip -n address`

The `-n` parameter should be `4` or `6`. The 4 will display IPV4 and 6 will display IPV6

![[linux_network_ip_n.png]]

## Netstat

The netstat command print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships

![[linux_network_netstat.png]]

To show only TCP protocols, we need to run the command `netstat -t`. And to show only UDP, use `netstat -u`

![[linux_network_netstat_tcp_or_udp.png]]

## CURL

Curl is a tool for transferring data from or to a server. It supports these protocols: 
* `dict`
* `file`
* `ftp`
* `ftps` 
* `gopher` 
* `gophers` 
* `http`
* `https` 
* `imap`
* `imaps` 
* `ldap`
* `ldaps` 
* `mqtt`
* `pop3`
* `pop3s` 
* `rtmp`
* `rtmps` 
* `rtsp`
* `scp`
* `sftp` 
* `smb`
* `smbs` 
* `smtp` 
* `smtps` 
* `telnet` 
* `tftp` 
* `ws` 
* `wss`. 

The command is designed to work without user interaction

### Basic use

![[linux_network_curl_get.png]]

### Sending POST request

![[linux_network_curl_post.png]]
The `-X` option is the parameter used to inform the HTTP verb. You can use the flag `--data` to send a request body

### Getting response

Using this flag, a file will be created (in this case a file called `response`) with the response

![[linux_network_curl_response_into_file.png]]

### Getting header

Using the flag `-I` we can get all headers

![[linux_network_curl_gettin_header.png]]

## Ping

Check connectivity to a remote host

![[linux_network_ping.png]]

## Traceroute

Trace the route packets take to a network host

![[linux_network_traceroute.png]]

## IP route

Is used to manipulate entries in the kernel routing tables

![[linux_network_ip_route.png]]

## Hostname

is used to display the system’s DNS name, and to display or set its hostname or NIS domain name

![[linux_network_hostname.png]]

## Nmap

Nmap is a tool for network exploration and security auditing. It was designed to rapidly scan large networks, although it works fine against single hosts. Nmap uses raw IP packets in novel ways to determine what hosts are available on the network, what services

![[linux_network_nmap.png]]

## NsLookup

Is a program to query Internet domain name servers. Nslookup has two modes: interactive and non-interactive. Interactive mode allows the user to query name servers for information about various hosts and domains or to print a list of hosts in a domain. Non-interactive mode prints just the name and requested information for a host or domain

![[linux_network_nslookup.png]]

## DIG - DNS Lookup Utility

Is a flexible tool for interrogating DNS name servers. It performs DNS lookups and displays the answers that are returned from the name server(s) that were queried. Most DNS administrators use `dig` to troubleshoot DNS problems because of its flexibility, ease of use, and clarity of output. Other lookup tools tend to have less functionality than `dig`.

![[linux_network_dig.png]]

