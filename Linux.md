###### File System
There are a number of types of filesystems out there. A system might host a number of different filesystems.
Common filesystems:
- ext4 - Linux's most common
- NTFS and FAT - Windows
- HFS+ - MacOS

To check what filesystem the system is currently running, run `df`.

Virtual File System (VFS) - the bridge/layer between the filesystem and the applications.

Journaling - the ability of fault tolerance through logs. In case a system goes down while dealing with files, the system will be able to figure out where it left off if the filesystem supports journaling, since it had logged the last thing it was doing before the system went down. 

![[Pasted image 20240315185006.png]]

###### Block Storage
The standard Linux file systems organize storage on hard disk drives. 
Disks are usually accessed in physical blocks rather than a byte (8 bits) at a time. Block sizes may range from 512 bytes to 4000 or larger.

A file is represented by an *inode*, a kind of serial number containing information about the data that makes up the file: to whom this file belongs and where is it located on the hard disk.

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
