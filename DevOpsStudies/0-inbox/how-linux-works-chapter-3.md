## Device files  
- The kernel presents many of device I/O as files  
- These devices files are called device nodes  
- Some devices are also accessible by standard programs like `cat`  
- Device files are on `/dev` directory  
- When you do `echo blabla > /dev/null`, behind the scenes, the kernel accepts the input and throw it away. The `/dev/null` is known as `the black hole`  
- Running the command `ls -l /dev` whe can see files types and its permissions. If the first character is `b`, `c`, `p` or `s`, the file is a device  
- `b` stands for `block`; `c` stands for `character`; `p` stands for `pipe`; `s` stands for socket;  
  
### Block device  
- Programs access data from a block device in chunks, because a block device has fixed size.  
  
#### Examples of block devices  
- SSD  
- HDD  
  
### Character device  
- Works with data streams.  
- It can only read from or write to other character devices.  
- They don't have a size.  
- The kernel performs a read or write operation when you read from or write to one character  
device.  
  
### Examples of characters devices  
- Printers  
- Keyboard  
  
## Pipe device  
- It works like character device, but usually performs another process at the other end of the I/O stream instead of a kernel driver  
  
## Socket device  
- Interfaces used frequently for interprocesses communication  
- They're often found outside of the `/dev` directory  
- It represents Unix Domain Sockets  
  
## More about devices  
- In block and character devices, when you run `ls -l /dev`, the numbers before the date represents the major and minor device numbers that kernel uses to identify devices  
- Similar devices have the same major numbers  
  
## Sysfs device path  
- It provides a uniform view for attached devices based on their actual hardware attributes  
- It is located on the path `/sys/devices`  
- Files on this directory are meant to be read primarly by programs rather than humans  
  
### Example of Output in sysfs  
```bash  
```  
  
## dd and devices  
- The dd program function is read from a input file or stream and write to an output file or stream  
- Useful when we're working with block and character devices  
- dd copies data in blocks of a fixed size  
  
### Example of dd command  
```bash  
sudo dd if=debian-13.3.0-amd64-netinst.iso of=/dev/sdc bs=4M status=progress oflag=sync  
```  
This command creates a bootable device, reading the debian iso (`if=debian-13.3.0...` parameter) and writing into `/dev/sdc` block device (`of=/dev/sdc` parameter).  
The block size is 4M  
  
### dd command parameters  
- `if=file` -> The input file. The default is the standard input  
- `of=file` -> The output file. The default is the standard output  
- `bs=size` -> The block size. `dd` reads and writes this many bytes of data at a time. To abbreviate large chunks of data, we can use `b` or `k` to 512 andd 1024 bytes respectively.  
Therefore, we can pass `bs=1k` instead of `bs=1024` as parameter  
- `ibs=size`, `obs=size` -> The input and output block sizes. We can use different sizes for input and output blocks, but if we use the same size, we use the parameter `bs`  
- `count=num` -> Total number of blocks to copy  
- `skip=num` -> Skip past the first num blocks in the input file or stream, and do not copy them to output

#### Example of `dd` usage
Let's pretend we have a file called `myfile.txt` with the follow content:
```bash
This is myfile content. All phrases here are random and don't matter. It's only a test
```

Then, we run the command:
```bash

sudo dd if=myfile.txt of=anotherfile.txt ibs=1 obs=2 count=10 skip=2
```

The content of `anotherfile.txt` will be:
```bash
 is myfile content.
```