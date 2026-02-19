#linux/mastery #february2026

## Linux Levels and Layers

Linux has three main layers. They are:
* Hardware
* Kernel
* Processes

### Hardware

Hardware is all physical stuff on computer, such as Memory, CPU, Network Interface and so on

### Kernel

Kernel is the Operating System center. It acts as a layer between hardware and operating system processes. Kernel tells to CPU what it needs to do

### Processes

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
* Often use the term `state` to talk about arrange of bits. This term is used to reference to memory, kernel, processes and other parts of the computer system
* You can describe a state as something has done or is doing right now. Example: "The process is waiting for input" or "The process is performing the stage 2 of its startup"

## Kernel
* One of its tasks is to subdivide memory. Each process gets its own share of memory. The kernel must ensure that each process keeps to its share. Kernel manages tasks in four general system areas:
	* **Processes:** It determines which processes are allowed to use CPU
	* **Memory:** It keeps track of all memory (the kernel must know what is currently allocated to a particular process, what might be shared between processes and what is free)
	* **Device drivers:** It acts as an interface between the hardware and processes. It's usually kernel's job to operate the hardware
	* **System calls and suport:** Processes normally use system calls to comunicate with kernel

### Process Management

This concept describes states of processes such as starting, pausing, resuming and terminating of processes. In modern computers we can run many processes at the same time - for example open a web browser and a spreadsheet at the same time - but, behind the scenes, what happens is that these applications don't run at exactly the same time.
Let's consider a one CPU core. What happens is:
* A process runs a task for a small fraction of seconds, then it pauses
* A second process runs a task for a small fraction of seconds as well, then finishes.
* A third process get the control up of the CPU for a fraction of seconds
Those change are called "context switch". However, these changes of context are so faster. Because of that we can't notice it. Then, it appears the processes are running at exactly the same time

#### Understanding context switching
1. Based on an internal timer, CPU interrupts the current process that it has been running, then it switches into kernel mode and hands the control back to the kernel
2. The kernel records the current state of the CPU and memory (it will be essential to resume the interrupted process later)
3. The kernel performes any tasks that might have come up during the preceding time slice
4. The kernel is ready to run another process. The kernel analyzes the list of process that are ready to run
5. The kernel prepares the memory and the CPU for the new process that will be running
6. The kernel tells to CPU how long time the time slice will take to the new process
7. The kernel switches the CPU into user mode and hands the control back of the CPU to the process

*The context switch answers the important question of when the kernel runs. The answer is that it runs between process time slices during a context switch.*

When we talk about multi CPU systems, the things are different. The kernel doesn't need to take the control back of the current CPU in order to allow a process to run in a different CPU. Furthermore, more than one process may run at a time. However, the steps described above are still used for Kernel to maximize the usage of all available CPUs

### Memory management
Kernel manages memory during the context switch. The follow conditions must hold:
* The kernel must have its own private area in memory and the user process can't access this area
* Each process needs  its own section of memory
* One user process may not access the private area in memory from another process
* User processes can share memory
* Some memory in user processes can be read-only
* The system can use more memory than it has physically present by using disk space as auxiliary

Modern CPUs have memory management unit (MMU) that enables a memory access schema called virtual memory. When using virtual memory, processes don't access directly the memory physically by its location in hardware. Instead, the kernel sets up each process to act as if it had an entire machine to itself. In other words, when using virtual memory kernel setup a machine to processes. The MMU intercepts the access and uses a memory map to translate the memory location from process point of view into physical memory location in the machine. Kernel must still initialize and continuously maintain and alter this memory address map, during a context switching, for example.

![[linux_virtual_memory_management.png]]

The implementation of a memory address map is called a page table

### Devices Drivers and Management
* Device is accessible only in Kernel mode
* Even devices do the same task, they don't have a similar programming interface. Because of that, device drivers are part of the kernel. Is a kernel's job to abstract those differences to easily present a uniform interface of devices to user processes

### System calls and support
* Tasks that user processes cannot perform alone or at all. Example: open, read and write files involves system calls (also known as *syscalls*)
* There are two important system calls. They are: `fork()` and `exec()`
* when `fork()` is called, the kernel creates almost a identical copy of this process