Linux has three main layers. They are:
* Hardware
* Kernel
* Processes

## Hardware

Hardware is all physical stuff on computer, such as Memory, CPU, Network Interface and so on

## Kernel

Kernel is the Operating System center. It acts as a layer between hardware and operating system processes. Kernel tells to CPU what it needs to do


## Processes

The processes are all running programs that kernel manages while user is using it

Here's a figure that represents those layers better:
![[linux_three_main_layers.png]]


### Diff between Kernel and User process

* Kernel has more privileges to run complex process. It has access to processor and main memory. 
* User processes have limitations of what they can run. They don't have free and unrestricted access to processor and main memory. 

## Main Memory

* Basically is a big collection of 0 and 1 (bits). Processes and kernel resides there.
* All inputs and outputs pass through the main memory as a bunch of bits
* In the main memory, CPU is just an operator on memory. It reads its instructions and data from the memory and writes data back out the memory
* Often use the term `state` to talk about arranging of bits. This term is used to reference to memory, kernel, processes and other parts of the computer system

## Kernel
* One of its tasks is to subdivide memory. Each process gets its own share of memory. the kernel must ensure that each process keeps to its share. Kernel manages tasks in four general system areas:
	* **Processes:** It determines which processes are allowed to use CPU
	* **Memory:** It keeps track of all memory (the kernel must know what is currently allocated to a particular process, what might be shared between processes and what is free)
	* **Device drivers:** It acts as an interface between the hardware and processes. It's usually kernel's job to operate the hardware
	* **System calls and suport:** Processes normally use system calls to comunicate with kernel

### Process Management

This concept describes states of processes such as starting, pausing, resuming and terminating of processes. In modern computers we can run many processes at the same time - for example open a web browser and a spreadsheet at the same time - but, behind the scenes, what happens, considering a one core CPU, is that a process gives the control up of the CPU. Then, this process pauses its execution and another process gives the control. The processes are always changing their states. This is known as **context switch**. The kernel is responsible for context switching