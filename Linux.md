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