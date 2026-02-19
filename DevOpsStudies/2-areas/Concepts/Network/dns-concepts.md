## What is DNS?
DNS is an acronym from Domain Name System. This can be defined as a translator from website addresses to IP addresses. 
Imagine if you'd need to remember all IP addresses from all websites you've been visiting. Is it possible? I don't think so. In fact, DNS exists to easily translate website addresses to IP addresses. Example:
When you type www.google.com, you're requesting access to Google server. Behind the scenes, DNS checks which IP belongs to google server checking its website address and then translate it to the IP address. In fact, what happens is:
www.google.com -> requests the server with IP 192.168.1.3 (the IP address here isn't the real IP address)

### Reverse DNS Lookup
The reverse DNS lookup does the opposite of the forward DNS: It receives an IP address and checks which domain belongs to this IP. Example:
If you run a `dig` command on your Linux terminal, passing an IP address by parameter, this command will show you what's the server name of this IP address. 
[[Network commands on Linux]] 

#network #concepts