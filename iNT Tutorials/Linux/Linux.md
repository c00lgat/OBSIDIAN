- Good Linux tutorial for beginners [https://ryanstutorials.net/linuxtutorial/](https://ryanstutorials.net/linuxtutorial/)
- Linux comprehensive book for beginners [https://tldp.org/LDP/Bash-Beginners-Guide/Bash-Beginners-Guide.pdf](https://tldp.org/LDP/Bash-Beginners-Guide/Bash-Beginners-Guide.pdf)
- Advanced Linux and Bash scripting [https://tldp.org/LDP/abs/abs-guide.pdf](https://tldp.org/LDP/abs/abs-guide.pdf)

###### Terminal Shortcuts
| Key or key combination          | Function                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Ctrl+A or Home key              | Move cursor to the *beginning* of the command line.                                                                |
| Ctrl+D                          | *Log out* of the current shell session, equal to typing the `exit` or `logout` commands                            |
| Ctrl+E or End key               | Move cursor to the *end* of the command line.                                                                      |
| Ctrl+L                          | *Clear* this terminal, equivalent to the `clear` command                                                           |
| Ctrl+R                          | *Search* command history                                                                                           |
| ArrowUp and ArrowDown           | *Browse* history. Go to the line that you want to repeat, edit details if necessary, and press Enter to save time. |
| Shift+PageUp and Shift+PageDown | *Browse* terminal buffer                                                                                           |
| Tab                             | Command or filename completion                                                                                     |
| Tab Tab                         | Shows file or command completion possibilities.                                                                    |

###### File System
There are a number of types of filesystems out there. A system might host a number of different filesystems.
Common filesystems:
- ext4 - Linux's most common
- NTFS and FAT - Windows
- HFS+ - MacOS

To check what filesystem the system is currently running, run `df`.

Virtual File System (VFS) - the bridge/layer between the filesystem and the applications.

Journaling - the ability of fault tolerance through logs. In case a system goes down while dealing with files, the system will be able to figure out where it left off if the filesystem supports journaling, since it had logged the last thing it was doing before the system went down. 

Here are a few common types in Linux OS:

| Symbol | Meaning      |
| ------ | ------------ |
| -      | Regular file |
| d      | Directory    |
| l      | Link         |
| c      | Special file |
| s      | Socket       |
| p      | Named pipe   |
| b      | Block device |


![[Pasted image 20240315185006.png]]

Another important feature of the Linux filesystem: filenames are Case sensitive, and files have no extensions. Use the `file` command to figure out the content type of a file:
```SHELL
myuser@hostname:~$ touch file1.png
myuser@hostname:~$ echo "hi" > file1.png
myuser@hostname:~$ ls
	file1.png
...
myuser@hostname:~$ file file1.png
	file1.png: ASCII text
myuser@hostname:~$ file File1.png
	File1: ERROR: cannot open 'File1.png' (No such file or directory)
```

In the above example, we used the `touch` command to create an empty file called `file1.png`, and the text "hi" was written into it (this command uses the `>` operator which will be discussed later on). Then we use the `file` command to inspect the type of the file. We can see that even though the file extension is `.png` (which is known for images), linux recognizes the file type as a regular text file, which is the correct type. In linux OS, file extensions are meaningless.

###### Important Directories
|Directory|Meaning|
|---|---|
|`/bin`|Common programs, shared by the system, the system administrator and the users.|
|`/dev`|Contains references to all the CPU peripheral hardware, which are represented as files with special properties.|
|`/etc`|Most important system configuration files are in `/etc`, this directory contains data similar to those in the Control Panel in Windows|
|`/home`|Home directories of the common users.|
|`/lib`|Library files, includes files for all kinds of programs needed by the system and the users.|
|`/proc`|A virtual file system containing information about system resources.|
|`/root`|The administrative user's home directory. Mind the difference between `/`, the root directory and `/root`, the home directory of the _root_ user.|
|`/tmp`|Temporary space for use by the system, cleaned upon reboot.|
|`/usr`|Programs, libraries, documentation etc. for all user-related programs.|
|`/var`|Storage for all variable files and temporary files created by users, such as log files, space for temporary storage of files downloaded from the Internet.|

###### Block Storage
The standard Linux file systems organize storage on hard disk drives. 
Disks are usually accessed in physical blocks rather than a byte (8 bits) at a time. Block sizes may range from 512 bytes to 4000 or larger.

A file is represented by an *inode*, a kind of serial number containing information about the data that makes up the file: to whom this file belongs and where is it located on the hard disk.

###### Block devices and standards streams
Let's take a closer look on the `/dev` directory:
```BASH
myuser@hostname:~$ ls -l /dev
brw-rw----  1 root disk    	8,   0 Apr  1 18:30 sda
brw-rw----  1 root disk    	8,   1 Apr  1 18:30 sda1
brw-rw----  1 root disk    	8,   2 Apr  1 18:30 sda2
…
lrwxrwxrwx  1 root root     	15 Apr  1 18:29 stderr -> /proc/self/fd/2
lrwxrwxrwx  1 root root      	15 Apr  1 18:29 stdin -> /proc/self/fd/0
lrwxrwxrwx  1 root root       	15 Apr  1 18:29 stdout -> /proc/self/fd/1
```

We will discuss some important files - block devices.

Note the files `sda`, `sda1`, `sda2`. Those are block device file type (the first dash is `b`).

Device files do not contain data in the same way that regular files, or even directories. Instead, the job of a device node is to act as an interface to a particular device driver within the kernel.

When a user writes to a device node, the device node transfers the information to the appropriate device driver in the kernel. When a user would like to collect information from a particular device, they read from that device's associated device node, just as reading from a file.

Block devices are devices that read and write information a chunk ("block") at a time. Block devices customarily allow random access, meaning that a block of data could be read from anywhere on the device, in any order.

In Linux, "sda," "sda1," and "sda2" are devices that refer to different **partitions** of a storage device, such as a hard drive or SSD.

The "sda" device refers to the entire storage device, while "sda1" and "sda2" are partitions of that device.

- "sda1" is the first partition on the "sda" device
- "sda2" is the second partition on the "sda" device
- etc...

```BASH
myuser@hostname:~$ lsblk
sda                   	8:0	0 465.8G  0 disk  
├─sda1                	8:1	0   487M  0 part  /boot
└─sda2                	8:5	0 465.3G  0 part
```

We will now discuss other important files: `stdin`, `stdout`, `stderr`.

Those are the standard input/output streams that are used by programs to read input (from your keyboard) and write output (to your screen).

Here's what each stream does:

1. **Standard Input (stdin)**: This is the stream that carries input to a program. By default, it is associated with the keyboard, so when a user types something into the terminal, it is sent to the program via the standard input file.
2. **Standard Output (stdout)**: This is the stream that carries normal output from a program. By default, it is associated with the terminal, so when a program prints something to the console, it is sent to the standard output file.
3. **Standard Error (stderr)**: This is the stream that carries error messages and other diagnostic output from a program. By default, it is also associated with the terminal, so when a program encounters an error or warning, it prints a message to standard error.

By default, these streams are connected to the terminal, but they can be redirected to files or other streams as well. This is a powerful feature of the Unix shell that allows programs to be combined and orchestrated in powerful ways.

Do you see how **"On a Linux system, everything is a file"**. Keep in mind this statement, it'll help you to understand Linux's behavior.


###### inode
Inodes (index node) are data structures in a filesystem that store metadata about files, such as file permissions, timestamps, and file size. 
Each file and directory in a filesystem is represented by an inode, which helps the operating system locate and manage the file's data on the disk `ls -i`. 
Metadata regarding the file. 
![[Pasted image 20240316160149.png]]
Helps the filesystem determine where a file is located, as the inode stores the attributes and disk block location of the object's data.
File-system object attributes may include [metadata](https://en.wikipedia.org/wiki/Metadata "Metadata") (times of last change, access, modification), as well as owner and [permission](https://en.wikipedia.org/wiki/File_system_permissions "File system permissions") data.

Here's an exhaustive list of the things that an inode stores about files/directories:
- File Type
- Owner
- Group
- Access permissions
- Timestamps
- Number of hardlinks to the file 
- Size of the file
- Number of blocks allocated to the file
- Pointers to the data blocks of the file

###### Partitioning
Disk partitioning in Linux involves dividing a physical disk into multiple logical sections called partitions. 
Each partition behaves like a separate disk, with its own file system and storage space.
Partitioning is done for various reasons, such as organizing data, installing multiple operating systems, or improving performance and security.

Tools for disk partitioning:
- *fdisk* - basic command-line partitioning tool, it does not support GPT.
- *parted* - is a command line tool that supports both MBR and GPT partitioning
- *gparted* - GUI version of parted.
- *gdisk* - fdisk, but it does not support MBR. Only supports GPT.

Useful commands for disk management:
- `df`
- `du`

###### Mount
Mounting is the process of making a file system available for access in a specific location in the Linux directory tree. 
When you mount a file system, you attach it to an existing directory (known as the mount point), and the files and directories in the file system become accessible under that mount point. 

Commands for mount and unmount:
- `sudo mount /dev/sdb1/mnt/mydisk`
- `sudo unmount /mnt/mydisk`

### ✏️ Kernel System Calls

(https://github.com/nirsht/DevOpsCourseINT2024/blob/main/Tutorials/Linux/3_linux_intro.md#pencil2-kernel-system-calls)

The Linux Kernel was presented in our first linux lecture - the main component of a Linux OS which functions as the core interface between a computer's hardware and its applications.


Then we moved to learn how to use the Terminal and communicate with the OS using commands such as `ls` or `chmod`.  
But how does it really work? We type a command and hit the Enter key, then what happens? This question tries to investigate this point.

Under the hood, linux commands are compiled C code (get yourself to know what is a compilation process if you don't know..). The C code contains **system calls**. The system call is the fundamental interface between an application and the Linux kernel.

In simple words, when your application wants to use the hardware (e.g. calculate something in the CPU, or write data to the disk), you create a system call to the Linux Kernel, and the linux kernel talks with the hardware on your behalf. Read more about what System Calls are.

`strace` is a Linux command, which traces system calls and signals of a program. It is an important tool to debug your programs in advanced cases. In this assignment, you should follow the `strace` output of a program in order to understand what exactly it does (i.e. what are the system calls of the program to the kernel). You can assume that the program does only what you can see by using `strace`.

To run the program, open a linux terminal in an empty directory and perform:

```shell
wget https://github.com/alonitac/DevOpsBootcampUPES/raw/main/strace_ex/whatIdo
```

The `wget` command is able to retrieve data from the internet.

1. Give the `whatIdo` file an exec permission (make sure you don't get Permission denied when running it).
2. Run the program using strace: `strace ./whatIdo`.
3. Follow strace output. Tip: many lines in the beginning are part of the load of the program. The first “interesting” line comes only at the end of the output.

Try to get a general idea of what this program does by observing the sys calls and the directory you've run the program.

** Credit for Alon Itach