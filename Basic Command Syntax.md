
https://drive.google.com/file/d/1pTQcpezfBGbRSj2Yab-IiSu_BSD8V0dh/view?usp=drive_link

CLI - Command Line Interface.

Most commands follow a simple pattern of syntax:
command (options...) (arguments...)


`echo -n > kovitz.txt`
>deletes all content from a text file in linux

`ls` - Listing of information about files. 
`ls` -> listing/list of files

Example: `ls Documents` 
It will list the contents of said directory. 

![[Pasted image 20230703160535.png]]
The resulting output is a list of files contained with the `Documents` directory.



Options
`ls -l` - results in a "long display". Meaning, gives more information about each of the files listed. 
`-l` stands for long.
![[Pasted image 20230703161717.png]]

`ls -r` - prints the results in reverse alphabetical order. *Default* is alphabetical order.
`-r` stands for reverse.

options can be given separately or combined.
`ls -l -r`, `ls -lr`, `ls -rl`; they all will output the same. 

<font color ="green">Executables are usually in green after ls -l prompt or just ls</font>

*cd -* (cd minus) takes us to last directory we were in
CTRL SHIFT + makes font bigger
CTRL - makes font smaller

---

`aptitude` command is a package management tool available on some Linux distributions. 

___
Printing Working Directory

`pwd` command can be used to discover where you are currently located within the filesystem.
`pwd [OPTIONS]`

![[Pasted image 20230703162358.png]]
![[Pasted image 20230703162421.png]]
*The output indicates that the user is currently in their home folder.*

`~` is equivalent to `/home/sysadmin/`

---

Changing Directories
---
`cd` (change directory) is a command that changes directories.

`cd [options] [path]`

`cd Documents` will lead us to the Documents directory (as we are already in the sysadmin directory and Documents is located within).
![[Pasted image 20230703163125.png]]


*Main directory in Linux is called the root directory and is represented by `/`
To move to the `/` directory, use the `/` character as the argument to the `cd` command.
![[Pasted image 20230703163405.png]]
![[Pasted image 20230703163428.png]]

Paths are a step by step direction. 
*`Absolute paths`* start at the root of the filesystem.
**/home/sysadmin** is an absolute path.
![[Pasted image 20230703163747.png]]
we can confirm that we have reached the desired directory by using the `pwd` command:
![[Pasted image 20230703163837.png]]

*`Relative paths`* start from your current location.
Relative paths start with the name of a directory, as opposed to Absolute paths where they usually start with /.
![[Pasted image 20230703163958.png]]
![[Pasted image 20230703164013.png]]


In the following diagram, we are trying to reach the art directory using a *Relative path*.
![[Pasted image 20230703164110.png]]

A relative path starts from the current directory, however you dont include it in the path. 
First step would be to enter the *School* directory and then entering the *Art* directory.

`cd School/Art` as we are using a relative path.
![[Pasted image 20230703164413.png]]
![[Pasted image 20230703164358.png]]

Using the `pwd` command to confirm the change:
![[Pasted image 20230703164451.png]]
![[Pasted image 20230703233241.png]]

---
Shortcuts
---
The `..` character: takes you back to the parent directory.
![[Pasted image 20230703233547.png]]


The `.` character: represents your current directory. Not as useful for the `cd` command.


The `~` character: the `~` symbol represents the home directory of the current user. Home directory is located at */home/sysadmin*. To return to home directory we have to execute the following command: 
![[Pasted image 20230703234345.png]]

---
## Changing file Ownership
*chown* command is used to change the ownership of files and directories.

`chown *OPTIONS* *OWNER* FILE`

`sudo chown root hello.sh`: changes ownership to the root user.
![[Pasted image 20230809001525.png]]



---
## Viewing Files

`cat [OPTIONS] [FILE_NAME]`
cat animals.txt: displays the content of animals.txt

`head [OPTIONS] [FILE_NAME]`
`tail [OPTIONS] [FILE_NAME]`
These commands are used to view a select number of lines from the top or bottom of a file. Taking a look at a few lines of a file can sometimes be helpful to ensure that the file is the one you want to use.

`head -n [number_of_lines] [FILENAME]`
The `-n` option with the `head` and `tail` commands can be used to specify the amount of lines to display.

Delimiter
`cat file.txt | cut " " -f1 (first field) -d " "`*(delimiter, once finds a space, stops looking at the rest of the words in the same row).*

>`ls -l >> list2.txt; cat list2.txt`
>We could use piping in order to save an output of a command onto a file.

>`cat file.txt; echo " "; cat kovitz.txt`
>prints contents and puts newline between the two outputs

>`tac` reads file from the opposite end

---
## Copying Files
`cp [OPTIONS] [SOURCE_DESTINATION]`
- f a copy of a file is created before changes are made, then it is possible to revert back to the original.
- A copy of a file can be used to transfer a file to removable media devices.
- A copy of an existing document can be used as a template for a new document.

The `dd` command is a utility for copying files or entire partitions at the bit level.
`dd [OPTIONS] [OPERARND]`
- It can be used to clone or delete (wipe) entire disks or partitions.
- It can be used to copy raw data to removable devices, such as USB drives and CDROMs.
- It can backup and restore the MBR (Master Boot Record).
- It can be used to create a file of a specific size that is filled with binary zeros, which can then be used as a swap file (virtual memory).

Let's examine the following example. The `dd` command creates a file named `/tmp/swapex` with 50 blocks of zeros that are one megabyte in size:
`dd if=/dev/zero of=/tmp/swapex bs=1M count=50`

![[Pasted image 20230718213538.png]]

---
## Removing Files

`rm [OPTIONS] [FILE_NAME]`

The `rm` command will ignore directories that it's asked to remove; to delete a directory, use a recursive option, either the `-r` or `-R` options. Just be careful since these options are "recursive", this will delete all files and all subdirectories.

`rmdir *` (asterisk is all). Removes all directories.


---
## Filtering Input

https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/
https://www.cyberciti.biz/faq/searching-multiple-words-string-using-grep/
https://itslinuxfoss.com/ount-total-number-of-occurrences-using-grep/

`$ grep -o -i Linux SampleFile.txt | wc -l`
- **grep:** Represents the “grep” command for searching.
- **-o:** Counts the number of occurrences of the searched string/pattern in the entire file.
- **-i:** Ignore the case sensitive i.e lower/uppercase while matching.
- “**|**(pipe character)”: Pipes the output of the “grep” and “wc” commands.
- **wc -l**: Denotes the “word count” utility that searches for the number of lines:

https://unix.stackexchange.com/questions/185116/how-to-find-with-grep-lines-that-end-in-a-certain-string
```
grep 'ing$' soi
```
`grep -i` = (ignore) ignores case sensitivity
`grep -v` = (--invert-match) selects non-matching lines


`history | grep "mkdir -p"` = (finds past commands that include the specified string)
![[Pasted image 20230718215652.png]]
<br>
![[Pasted image 20230718215705.png]]
<br>
![[Pasted image 20230718220325.png]]
<br>
![[Pasted image 20230718220402.png]]
<br>
### Match a Single Character With `.`
![[Pasted image 20230718220525.png]]
<br>
![[Pasted image 20230718220539.png]]
<br>
![[Pasted image 20230718220549.png]]
<br>
![[Pasted image 20230718220602.png]]

### Match a Single Character With `[]`

![[Pasted image 20230718220627.png]]
<br>
![[Pasted image 20230718220642.png]]
<br>
![[Pasted image 20230718220655.png]]
<br>
![[Pasted image 20230718220723.png]]
<br>
### Match a Repeated Character Or Patterns With `*`
![[Pasted image 20230718220749.png]]
<br>
![[Pasted image 20230718220801.png]]
<br>
![[Pasted image 20230718220850.png]]
<br>
![[Pasted image 20230718220919.png]]

find Pokemon/ -type d -name "????????\*" (finds all directories with at least 8 letters in the name)

find . -type f -name "\[a]\[b]\*" Finds all files that start with ab

---
## Shutdown
The `shutdown` command arranges for the system to be brought down in a safe way. All logged-in users are notified that the system is going down and within the last five minutes leading up to the shutdown, new logins are prevented.
<br>

![[Pasted image 20230718221014.png]]
<br>
![[Pasted image 20230718221033.png]]

---
## Network Configuration

The `ifconfig` command stands for "interface configuration" and is used to display network configuration information.

`ifconfig [*]OPTIONS]`
<br>
>**Note**
>The `iwconfig` command is similar to the `ifconfig` command, but it is dedicated to wireless network interfaces.

![[Pasted image 20230718221142.png]]
<br>
>**Consider This**
>The `lo` device is referred to as the loopback device. It is a special network device used by the system when sending network-based data to itself.

![[Pasted image 20230718221243.png]]
<br>
![[Pasted image 20230718221257.png]]

---
## Viewing Processes

Running a command results in something called a process. In the Linux operating system, processes are executed with the privileges of the user who executes the command. This allows for processes to be limited to certain capabilities based upon the user identity.
<br>
Although there are exceptions, generally the operating system will differentiate users based upon whether they are the administrator. Typically regular users, like the `sysadmin` user, cannot control another user's processes. Users who have administrative privileges, like the `root` account, can control any user processes, including stopping any user process.
<br>
The `ps` command can be used to list processes.
`ps [OPTIONS]`
<br>
**sysadmin@localhost:~$** ps
  PID TTY          TIME CMD
   80 pts/0        00:00:00 bash
   94 pts/0        00:00:00 ps

The `ps` command will display the processes that are running in the current terminal by default. In the example above, the bottom line is the process created by the execution of the `ps` command. The output includes the following columns of information:

- `PID`: The process identifier, which is unique to the process. This information is useful for controlling the process by its ID number.
    
- `TTY`: The name of the terminal where the process is running. This information is useful for distinguishing between different processes that have the same name.
    
- `TIME`: The total amount of processor time used by the process. Typically, this information isn't used by regular users.
    
- `CMD`: The command that started the process.
    
<br>
Instead of viewing just the processes running in the current terminal, users may want to view every process running on the system. The `-e` option will display every process:

>**sysadmin@localhost:~$** ps -e
  PID TTY          TIME CMD                                                     
    1 pts/0        00:00:00 init                                                    
   33 ?            00:00:00 rsyslogd                                                
   37 ?            00:00:00 cron                                                    
   39 ?            00:00:00 sshd                                                    
   56 ?            00:00:00 named                                                   
   69 pts/0        00:00:00 login                                                   
   79 pts/0        00:00:00 bash                                                    
   94 pts/0        00:00:00 ps

Typically, the `-f` option is also used as it provides more detail in the output of the command, including options and arguments. Look for the `ps` command on the last line, the `CMD` column now includes the options used:

>**sysadmin@localhost:~$** ps -ef
UID        PID  PPID  C STIME TTY          TIME CMD                             
root         1     0  0 19:16 pts/0        00:00:00 /sbin??? /init                  
syslog      33     1  0 19:16 ?            00:00:00 /usr/sbin/rsyslogd              
root        37     1  0 19:16 ?            00:00:00 /usr/sbin/cron                  
root        39     1  0 19:16 ?            00:00:00 /usr/sbin/sshd                  
bind        56     1  0 19:16 ?            00:00:00 /usr/sbin/named -u bind         
root        69     1  0 19:16 pts/0        00:00:00 /bin/login -f                   
sysadmin    79    69  0 19:16 pts/0        00:00:00 -bash                           
sysadmin    95    79  0 19:43 pts/0        00:00:00 ps -ef
---
## Package Management

At the lowest level of the Debian package management system is the `dpkg` command. This command can be tricky for novice Linux users, so the Advanced Package Tool, `apt-get`, a front-end program to the `dpkg` tool, makes management of packages even easier.

<mark style="background: #FF5582A6;">Note:</mark> the `dpkg` or the `apt` tool is used in Debian based systems. 
For RedHat based systems such as REHL, CentOS and Amazon Linux 2, the package manager is the `YUM` package manager (Yellow dog updater, modified). `YUM` is the front end for the `RPM` (RedHat package manager) tool.

Repositories available to a package manager are typically defined in a configuration file.

The following are examples of Amazon Linux 2 repositories managed by AWS:
- `amzn2-core`
- `amzn2extra-docker`

### Installing Packages
Package files are commonly installed by downloading them directly from repositories located on Internet servers. The Debian repositories contain more than 65,000 different packages of software. Before installing a package, it is good practice to refresh the list of available packages using the `apt-get update` command.
<br>
`sudo apt-get update`
>**sysadmin@localhost:~$** sudo apt-get update                             
>\[sudo] password for sysadmin:                                                   
>Ign file: amd64/ InRelease                                                      
>Ign file: amd64/ Release.gpg                                                    
>Ign file: amd64/ Release                                                        
>Reading package lists... Done

To search for keywords within these packages, you can use the `apt-cache search` command.

`apt-cache search [keyword]`
<br>
Once you've found the package that you want to install, you can install it with the `apt-get install` command:

`sudo apt-get install [PACKAGE]`
![[Pasted image 20230718221953.png]]
<br>
### Updating packages
The `apt-get install` command can also update a package, if that package is installed and a newer version is available. If the package is not already on the system, it would be installed; if it is on the system, it would be updated.
<br>
Updating all packages of the system should be done in two steps. First, update the cache of all packages available with `apt-get update`. Second, execute the `apt-get upgrade` command and all packages and dependencies will be updated.
![[Pasted image 20230718222059.png]]
<br>
### Removing Packages
The `apt-get` command is able to either remove or purge a package. The difference between the two is that purging deletes all package files, while removing deletes all but the configuration files for the package.

An administrator can execute the `apt-get remove` command to remove a package or the `apt-get purge` command to purge a package completely from the system.

`apt-get remove [package]`

`apt-get purge [package]`

---
## Using the YUM package manager

`yum [OPTIONS] [command] [list of package names]`

- Install software: `yum -y install <package name>`
	`-y` = Assume that yes is the answer to any conformation prompt

- Update software: `yum update <package name>`

- Inventory installed software: `yum list installed`

- Uninstall software: `yum remove <package name>`

- Display installed packages: `yum list installed`
	  Can be used with grep in the following way:
		  `yum list installed | grep ssh`

- Display the history of updates: `sudo yum history list`

- To display more info about a certain update, use: `sudo yum history info <#>` (replace the `<#>` with the history list number after running `sudo yum history list`)

---
## Updating User Passwords
The `passwd` command is used to update a user’s password. Users can only change their own passwords, whereas the root user can update the password for any user.

`passwd [OPTIONS] [USER]`

<br>
For example, since we are logged in as the `sysadmin` user we can change the password for that account. Execute the `passwd` command. You will be prompted to enter the existing password once and the new password twice. For security reasons, no output is displayed while the password is being typed. The output is shown as follows:

![[Pasted image 20230718222322.png]]
<br>
If the user wants to view status information about their password, they can use the *`-S`* option:

![[Pasted image 20230718222346.png]]
<br>
Output fields are explained below:

![[Pasted image 20230718222416.png]]


The root user can change the password of any user. If the root user wants to change the password for `sysadmin`, they would execute the following command:

>**root@localhost:~#** passwd sysadmin                                               
Enter new UNIX password:                                                        
Retype new UNIX password:                                                       
passwd: password updated successfully

---
## Redirection

Use the `>` character to redirect the STDOUT of the `cat food.txt` command above to a new file called `newfile1.txt`:

`cat food.txt > newfile1.txt`

This is useful if you need to copy content from an important file to another file in order to edit the contents without modifying the original file.

---
## Text Editor
- The `vi` editor is available on every Linux distribution in the world. This is not true of any other editor.
    
- The `vi` editor can be executed both in a CLI (command line interface) and a GUI (graphical user interface).
<br>
There are three modes used in `vi`: *command mode*, *insert mode*, and *ex mode*.

### Command Mode Movement
Initially, the program starts in command mode. Command mode is used to type commands, such as those used to move around a document, manipulate text, and access the other two modes. To return to command mode at any time, press the **Esc** key.

Once some text has been added into a document, to perform actions like moving the cursor, the **Esc** key needs to be pressed first to return to command mode. This seems like a lot of work, but remember that `vi` works in a terminal environment where a mouse is useless.
<br>
Movement commands in `vi` have two aspects, a motion and an optional number prefix, which indicates how many times to repeat that motion. The general format is as follows:

>[count] motion
![[Pasted image 20230718223534.png]]

Note
Since the upgrade to `vim` it is also possible to use the arrow keys `← ↓ ↑ →` instead of `h j k l` respectively.

To move the cursor to a specific line number, type that line number followed by the `G` character. For example, to get to the fifth line of the file type `5G`. `1G` or `gg` can be used to go to the first line of the file, while a lone `G` will take you to the last line. To find out which line the cursor is currently on, use **CTRL+G**.

### Command Mode Actions
The standard convention for editing content with word processors is to use copy, cut, and paste. The `vi` program has none of these. Instead, `vi` uses the following three commands:

![[Pasted image 20230718223759.png]]
![[Pasted image 20230808132756.png]]
![[Pasted image 20230808133019.png]]

The motions learned from the previous page are used to specify where the action is to take place, always beginning with the present cursor location. Either of the following general formats for action commands is acceptable:

`[action] [count] [motion]`

`[count] [action] [motion]`

### Delete
Delete removes the indicated text from the page and saves it into the buffer, the buffer being the equivalent of the "clipboard" used in Windows or Mac OSX. The following table provides some common usage examples:

![[Pasted image 20230718223905.png]]
### Change
Change is very similar to delete; the text is removed and saved into the buffer, however, the program is switched to insert mode to allow immediate changes to the text. The following table provides some common usage examples:

![[Pasted image 20230718223953.png]]
### Yank
Yank places content into the buffer without deleting it. The following table provides some common usage examples:

![[Pasted image 20230718224035.png]]
### Put
Put places the text saved in the buffer either before or after the cursor position. Notice that these are the only two options, put does not use the motions like the previous action commands.

![[Pasted image 20230718224053.png]]

### Searching in vi
Another standard function that word processors offer is find. Often, people use **CTRL+F** or look under the edit menu. The `vi` program uses search. Search is more powerful than find because it supports both literal text patterns and regular expressions.

To search forward from the current position of the cursor, use the `/` to start the search, type a search term, and then press the **Enter** key to begin the search. The cursor will move to the first match that is found.

To proceed to the next match using the same pattern, press the `n` key. To go back to a previous match, press the `N` key. If the end or the beginning of the document is reached, the search will automatically wrap around to the other side of the document.

To start searching backwards from the cursor position, start by typing `?`, then type the pattern to search for matches and press the **Enter** key.

### Insert Mode
Insert mode is used to add text to the document. There a few ways to enter insert mode from command mode, each differentiated by where the text insertion will begin. The following table covers the most common:

![[Pasted image 20230718224240.png]]
### Ex Mode
When the ex mode of the `vi` editor is being used, it is possible to view or change settings, as well as carry out file-related commands like opening, saving or aborting changes to a file. In order to get to the ex mode, type a `:` character in command mode. The following table lists some common actions performed in ex mode:

![[Pasted image 20230718224412.png]]
A quick analysis of the table above reveals that if an exclamation mark, `!`, is added to a command, it then attempts to force the operation. For example, imagine you make changes to a file in the `vi` editor and then try to quit with `:q`, only to discover that the command fails. The `vi` editor doesn't want to quit without saving the changes you made to a file, but you can force it to quit with the ex command `:q!`.

**Consider This**
Although the ex mode offers several ways to save and quit, there's also `ZZ` that is available in command mode; this is the equivalent of `:wq`. There are many more overlapping functions between ex mode and command mode. For example, ex mode can be used to navigate to any line in the document by typing `:` followed by the line number, while the `G` can be used in command mode as previously demonstrated.

---

## Wildcards - power of ? and *
`rm *` - removes all files in directory.

`rm month/*` - removes all files in month directory.

`touch file{3..5}.txt` - creates files file3.txt, file4.txt and file5.txt

`touch file{1..10..2}.txt` - creates files with only odd numbers in the name.

`ls -l * .sh` - lists all files that have a .sh format

`find . -type f -name "f*"`

`ls -l * e * - finds all files with the letter e in them`

`ls -l ?` - the question mark is substituted with only one letter, shows all files that only have one letter in the name. f.txt does not count

`rm alpha*` (removes all files that start with the word alpha in the beginning)

When using a `?` as a wildcard, it does not match up with words that dont have any letters to fill out the `?`


---
## File permissions

Read - r=4
Write - w=2
Execute - e=1

If we want to give only read and write permissions, we can add 6 (4+2).

`chmod 751 aa.txt`

---
## mkdir essentials

`mkdir {dir1,dir2}` Makes two directories with the names of dir1 and dir2.

`mkdir dir1 dir2` Also works the same way

`mkdir dir dir/dd dir/cc` Makes a new folder with new subfolders inside it.

`mkdir dir/dd dir/cc` wouldn't work, throws exception that dir does not exist.

`mkdir -p dir/dd dir/cc` does work. 

`mkdir -p zoo/{predatory/{table,leopard}/,birds/{parrot,chair}}`

`mkdir -p grocery/{bakery/cakes/{minirolls,bars}/,home/cleaning/{wipes,polish}}`

![[Pasted image 20230723141548.png]]


---
# The find command

https://www.baeldung.com/linux/find-files-lacking-permissions

`find . -type d` (only shows the type, d is for directory)

`find . -type d -empty`

`find zoo/`

`find zoo/ -type f`

To find all non-empty files in the same directory, simply add `!` before `-size 0`:  `find -L /home/peter -maxdepth 1  -type f ! -size 0`

`find . -empty (looks for empty files)`

`find . -type f -empty -print -delete` (looks for empty files, prints them and deletes them in one go)

 [Copy the content/file to all subdirectory in a directory using terminal](https://askubuntu.com/questions/300744/copy-the-content-file-to-all-subdirectory-in-a-directory-using-terminal)
`find <target-dir> -type d -exec cp <the file> {} \;`

- `exec commandName` = Runs the specified command on the returned file or files.

`find /etc -iname "*.conf" -mtime 7` = Shows how to search for files with a file name extension of `.conf` that start in the `/etc/` directory. The search should be case insensitive and return only those matching files that were modified exactly 168 (7 x 24) hours ago.

---
## SED
https://www.gnu.org/software/sed/manual/sed.html
https://www.cyberciti.biz/faq/how-to-use-sed-to-find-and-replace-text-in-files-in-linux-unix-shell/
https://www-users.york.ac.uk/~mijp1/teaching/2nd_year_Comp_Lab/guides/grep_awk_sed.pdf

https://stackoverflow.com/questions/5998454/remove-occurrences-of-string-in-text-file
Remove occurrences of string in text

---
AWK
https://www.geeksforgeeks.org/awk-command-unixlinux-examples/
https://www.gnu.org/software/gawk/manual/gawk.html
https://exercism.org/tracks/awk

`awk '{print $1,$4}' employee.txt` (prints first and fourth field in every line in file)

---
# File compression
`gzip` 
`zcat` lets us read compressed files

---
Random notes

double tab while doing `cd ..`/ will show us directories that are in the back directory

`CTRL+a` goes back to the beginning of the row 
`CTRL+e` goes back to the end of the row

`echo "" | cat file.txt - kovitz.txt` (The - is standard input, first is cats the file.txt, waits for standard input which is the "" that we entered and then goes on to display the kovitz.txt)

`uptime` - shows the uptime of the machine or in other words, how long the system has been up since the last boot. `uptime -p to display the uptime of the system in an easily readable format.

`whoami` = Prints out the name of the user. 

`history` displays all commands that were entered in the console. History is stored in `/home/[USERNAME]/.bash_history`

`who | tee who_output.txt` (prints and saves in txt file in one go)

`gedit [FILE_NAME]` opens the text file in a GUI text editor (have to install gedit)

`mv {Croatia,Wales}/* Poland/` (moves all the files from Croatia and wales directories into the Poland directory)

`touch Croatia/{abc,file.txt,file.doc}` (touches 3 different files at once)

`mv {Croatia,Wales}/{\*.txt, \*.doc} Poland/` (moves all the files from Croatia and wales directories into the Poland directory)

---
# Basic Linux Keystrokes

`Esc` = Escaping out of editing mode - get out of any of the pressed keys

Tilde: used for cd, backtick is used 

1/!: in linux, referred to as bang

2/@: 

3/#: this key is used in scripting in config files/for comments 

4/$: variable

5/%:

6/^: caret means anything in the beginning of something, used in commands for that purpose

7/&: to put processes in the background

8/\*:

9/(: open parenthesis 

-/\_: dash used for options in commands

=/+:

Tab key: skips few spaces

{/\[:

}/]:

Enter key: sometimes referred to as carriage return

:/; 

‘/”: 

|: pipe

\: backslash. Used in windows.

Shift key: 

<: input output

\>: input output

.

,

?:

/: used in linux to access paths 

Right control key: while using certain commands, pressing right ctrl can do different things than pressing the left key

---
## Some basic Linux notes
Super user called root.
powerful account that can create modify delete and make changes to system config files
Linux is case sensitive
Linux kernel is not an OS. It is a small software that lets you manipulate the computer hardware through commands
Linux is mostly CLI and not GUI.

---
## Access Linux
Console is like a direct access to the operating system.
Remote access: connecting to your machine remotely through the internet.

For example, if we wanted to connect to a remote Linux machine using windows, we use the PuTTY client. If you have windows 10 and later, you can use the CMD to connect to a remote machine with SSH as it comes with the operating system by default and thus there is no need to download software in order to SSH into a remote machine.

---

If `ifconfig` does not work, we could use `ip addr`
or we can install net-tools and then run `ifconfig`

---
## Command prompt
Short text that sits at the start of the command line.
![[Pasted image 20230731112921.png]]
To get your prompt back: *CTRL + C*. If you get stuck, you can press *CTRL + C* to get the prompt back and are able to enter new commands again. 

---
## File system structure and its description

Files used for the bootloader, every time our machine boots up, it will
go to the /boot folder and looks into it. 
`/root` root user home directory. Not the same as /
`/dev` System devices (keyboards, speakers, etc.)
`/etc` config files. If we have any apps on the system, all of their config files reside in the /etc folder. Remember to do a backup to the config file before modifying it.
`/bin` -> /usr/bin every day user commands
`/sbin` -> /usr/sbin System/filesystem commands
`/opt` optional add-on applications, apps that do not come with the OS.
`/proc` Running processes (only exist in Memory)
`/lib` -> /usr/lib C programming library files needed by commands and apps
`strace -e` 
`/tmp` stores temporary files. 
`/home` for regular users. 
`/var` System logs
`/run` stores temporary runtime files.
`/mnt` To mount external filesystem. 
`/media` For cd-rom medias. if we use a cd drive it will appear there.

![[Pasted image 20230731115246.png]]


---
## Navigating File System
`cd` - stands for change directory
`pwd` - stands for print working directory
`ls` - stands for list

---
## Linux File or Directory Properties
![[Pasted image 20230731121126.png]]

---
![[Pasted image 20230731121625.png]]

---
3 types of root in Linux:
Root account: most powerful account which has access to all commands and files.
Root as /: the very first directory in Linux
Root home directory: the root user account has a directory located in /root which is called root home directory

---
## Changing password
Should change your initial password as soon as you login.
Command is: `passwd userid`
Old password: enter your old password 
New password: enter the desired password
Retype new password: retype the new password

>Only root can modify passwords.

---

If we want to make a script, 
the first line should say `#! /bin/bash` which tells the system to run the code using the bash interpreter.

---
## Creating files and Directories
- `touch`
- `cp`
- `vi`

### Creating Directories
`mkdir`

`ls -ltr` = Shows files from last to latest created

`cp -R` = copies all files and subfolders inside a directory

---
## Find files and directories
Two main commands to find files/directories:
 - `find`
 - `locate`

`find . (current directory) -name [filename]`
`locate ""`

`find / -name "ifcfg-enp0s3(filename)"` *RUN AS SUDO*

### Difference between find and locate commands
`locate` is much faster because it looks for specific files that are cached. locate uses a prebuilt database.

To update locate database run `updatedb`

`find` runs over all the directories in real time thus taking more time and compute power.

---
## Wild cards

A character that can be used as a substitute of a class of characters in a search

`*` - represents zero or more characters.
`?` - represents a single character.
`[]` - represents a ra nge of characters.

`touch file{1..9}.txt` creates 9 files, from 1 to 9 in one go. So file1.txt, file2.txt on and on until file9.txt

![[Pasted image 20230731152419.png]]


---
## Soft and Hard links

Every time you create a file, the operating system gives said file a number. The number is called an *inode*. Pointer or number of a file on the hard disk.

Soft Link = link will be removed if file is removed or renamed.

Hard Link = Deleting or renaming or moving the original file, will not affect the hard link

![[Pasted image 20230731155126.png]]

![[Pasted image 20230731155305.png]]

`ls -i` shows the inode numbers of the files/directories.

![[Pasted image 20230731160021.png]]




![[Pasted image 20230808233259.png]]
*Taken from the AWS restart course.*

- Hard link: Every file has an object that is called inode, which stores the file's disk block locations and attributes. An inode is identified with a unique number. A hard link is a pointer to a file's inode.
	A hard node **cannot** reference a directory.
		If the original file is deleted, its data still exists until the hard link is deleted.
	Syntax: `ln [OPTIONS] [ORIGINAL_FILE_NAME] [LINK_NAME]`



- Symbolic link: Also known as a soft link or symlink, a symbolic link points to the original file name or a hard link.
	Points to an original file name or a hard link.
	**Can** point to a directory.
	If the original file is deleted, the soft link is broken until you create a new file with the original name.
		Syntax: `ln -s [OPTIONS] [ORIGINAL_FILE_NAME] [LINK_NAME]` 
![[Pasted image 20230808233942.png]]
The screenshot shows that we can tell when a file is in fact a soft link that is pointing to another file/directory/hard link.

---
https://www.makeuseof.com/linux-command-line-chaining-operators/


---

## File permissions with numeric values
![[Pasted image 20230801093707.png]]


## File ownership commands
![[Pasted image 20230801100101.png]]

---
## ACL
![[Pasted image 20230801100303.png]]

`setfacl -m u:user:rwx /path/to/file` = To add permission for user

`setfacl -m g:group:rw /path/to/file` = add permissions for a group

`setfacl -Rm "entry" /path/to/file` = To allow all files or directories to inherit ACL entries from the directory it is within

`setfacl -x u:user /path/` = remove a specific entry

 `-b /path/` = to remove all entries

`getfacl /path` = shows all accesses to groups and users

---
## Help commands
`what is` command
`[command] --help`
`man [command]` (manual)

---
## Adding text to files

### 3 simple ways:
- `vi`
- Redirect command output `>` or `>>`
- `echo >` or `>>`

---
## Input and output redirects
3 Redirects in Linux
1. Standard input (stdin)
   ![[Pasted image 20230808103713.png]]
   Standard input is the file handle that your process reads to get information from you. It can be from the user who provides the information or from a file.
   
2. Standard output (stdout)
   ![[Pasted image 20230808104151.png]]

3. Standard error (stderr)
   ![[Pasted image 20230808104446.png]]
 
`-- Output (stdout)`

---
## Standard output to a File (tee)

`tee` command is used to store and view (at the same time) the output of any command.

Named after the T-splitter used in plumbing. Both displays and saves into a file. Simultaneously.

`echo "David Puddy is Elaine's boyfriend"`
`echo "David Puddy is Elaine's boyfriend" > elaine-david`
Does not throw the output to the screen.

`echo "David Puddy is Elaine's boyfriend" | tee elaine-david`
Does throw the output to the screen while also saving it to the elaine-david file.
The tee commands overrides the contents of a file by default.

`echo "David Puddy is Elaine's boyfriend" | tee -a elaine-david`
By using the *-a* option, it appends the input instead of having it override the current content of a file.
![[Pasted image 20230809205001.png]]


---
## Pipes
Used by the shell to connect the output of one command directly to the input of another command.

`ls -ltr | more` piping our output into the more command, which shows content one page at a time when there is too many results showing on the page.

---
## File Maintenance Commands
1. `cp`
2. `rm`
3. `mv`
4. `mkdir`
5. `rmdir or rm -r`
6. `chgrp`
7. `chown`

`rm -Rf` will forcefully remove sub-directories and their contents as well.

---
## File display commands
- `cat`
- `more`
- `less`
- `head`
- `tail`

---
## Filters / Text processors commands
- `cut`
- `awk`
- `grep` and `egrep`
- `sort`
- `uniq`
- `wc`
---
## Cut
Allows you to cut parts of lines from specified files.

- `cut [filename]` = does not work
- `cut --version` = checks version
- `cut -cl [filename]` = list one character
- `cut -c1,2,4` = pick and choose character
- `cut -c1-3,6-8 [filename]` = list range of characters
- `cut -b1-3 [filename]` = list by byte size
- `cut -d: -f 6 /etc/passwd` = list the first 6th column separated by ":"
- `cut -d: -f 6-7 /etc/passwd` = list the first 6 and 7th columns separated by ":"

---
## AWK
Utility/language designed for data extraction. Used for files or from an ouitput

- `awk --version` = check version
- `awk '{print $1}' [FILE_NAME]` = shows only the first field from a file
- `ls -l | awk '{print $1,$3}'` = list the first and third columns from ls -l
- `ls -l | awk '{print $NF}'` = last field of the output
- `awk '/Jerry/ {print}' [FILE_NAME]` = search for a specific word
- `awk -F: '{print $1}' /etc/passwd` = output only the first field of /etc/passwd
- `echo "Hello Tom" | awk '{$2="Adam" ; print $0}'` = replace words field words
- `cat file | awk '{$2="Imran" ; print $0}` = replace words field words
- `awk 'length($0) > 15' filename` = displays all lines that have a length greater than 15
- `ls -l | awk '{if($9 == "seinfeld") print $0;}'` 
- `ls -l | awk '{print NF}'` 

https://www.ibm.com/docs/zh/aix/7.2?topic=awk-command
https://www.cs.unibo.it/~renzo/doc/awk/nawkA4.pdf

---
## grep/egrep
Stands for "global regular expression print", processes line by line and prints any lines that match a specified pattern.

- `grep --version` OR `grep --help`
- `grep [keyword] [FILE_NAME]` = looks for the word in the file
- `grep -c [keyword] [FILE_NAME]` = counts words that matches the pattern
- `grep -i [keyword] [FILE_NAME]` = ignores case sensitivity 
- `grep -n [keyword] [FILE_NAME]` = display the matched lines and their matched word
- `grep -v [keyword] [FILE_NAME]` = shows lines that DO NOT contain the word
- `grep [keyword] [FILE_NAME] | awk '{print $1}'` = search for a keyword and only give the first field
- `ls -l | grep Desktop`
- `grep -e -i "keyword|keyword2" [FILE_NAME]` = look for fields that contain either the first keyword or the second keyword
https://www.gnu.org/software/grep/manual/html_node/Character-Classes-and-Bracket-Expressions.html

---
## Sort and uniq commands

1. `sort` command sorts in alphabetical 
2. `uniq` commands filters out

commands:
- `sort --version` OR `sort --help`
- `sort [FILE_NAME]` = sorts the file alphabetically
- `sort -r [FILE_NAME]` = sort in reverse alphabetical order
- `sort -k2 [FILE_NAME]` = sort by the second column 
- `uniq [FILE_NAME]` = remove duplicates
- `sort [FILE_NAME] | uniq` = sort first then uniq
- `sort [FILE_NAME] | uniq -e` = sort first and then uniq, while showing the amount of duplicates
- `sort [FILE_NAME] | uniq -d` = only shows repeated lines
---
## wc
The command reads either standard input or from a list of files and generates 

- `wc --version` OR `wc --help`
- `wc [FILE_NAME]` = check file line count, word count and byte count
- `wc -l [FILE_NAME]` = get the number of lines in a file
- `wc -w [FILE_NAME]` = get the number of words in a file
- `wc -b [FILE_NAME]` = get the number of byes in a file
- `wc -c [FILE_NAME]` = counts characters in file
- `wc [DIRECTORY]` = NOT ALLOWED
- `ls -l | wc -l` = runs ls first and then counts how many lines there are, counts the amount of folders. Keep in mind that it also counts the total row so we should count minus 1 from the output we get from the wc. Number of files
- `grep [keyword] | wc -l` = looks for a word in a file and then counts how many lines there are that matched. Number of keyword lines.

---
## Compare 

- `diff` = compares line by line and displays the differences
	  Valuable for comparing two files
	  Output is called a *diff*
	  Syntax = `diff [OPTIONS] File1 File2`
- `cmp` = compares byte by byte

---
## Compress and decompress files


- `gzip` = compresses a file
- `gzip -d` OR `gunzip` = decompresses a file


- `tar` = zips files together for easier copying or downloading. Created bundle is called a *tarball*.
	`tar cvf .` = copy everything 
		To bundle and compress file1, file2 and file3 into a file called tarball.tar: `tar -cvf tarball.tar file1 file2 file3`
	`tar xvf .` = extract everything 
		To unbundle or extract files from the tarball:
		`tar -xf tarball.tar`
	`tar` options:
		`-x` = Extracts the contents of a tarball
		`-z` = Compresses the contents of a tarball by using the `gzip` utility.
		`-f` = Specifies the name of the tarball
		`-v` = Produces verbose output by showing file names while the tarball is processed

- `zip` used as a compression tool
	Syntax: `zip -r [FolderName]`
	The `-r` option is used to include the contents of a directories' subdirectories.

- `unzip` command is used as an extraction tool
	Syntax: `unzip [FolderName].zip` 


https://www.freecodecamp.org/news/tar-command-linux-tar-cvf-tar-xvf/

---
## Truncating file size (truncate)
Used to shrink of extend the size of a file to the specified size
Will actually chop the file and **lose** the content of the file. 

- `truncate -s 10 [FILE_NAME]` = shrinks the file to 10 bytes

Can be used to make the file bigger as well. Adds empty letters to fill up the file and make it bigger. Looks something like "^@^@^@^@^@^@".

---
## Combining and splitting files
- Multiple files can be combined into one 
- One file can be split into multiple files

- `cat file1 file2 file3 > file4`
- `split file4`

for example: `split -l 300 file.txt childfile.txt` = Split file.txt into 300 line per file and output to chidlfileaa childfileab childfileac

---
## Linux vs Windows commands
![[Pasted image 20230801122841.png]]

---

## tr
The **tr** command is a UNIX command-line utility for translating or deleting characters. It supports a range of transformations including uppercase to lowercase, squeezing repeating characters, deleting specific characters, and basic find and replace. It can be used with UNIX pipes to support more complex translation. **tr stands for translate.**

\[:upper:\], \[:lower:\], \[:alnum:\] are called character classes.
https://www.gnu.org/software/grep/manual/html_node/Character-Classes-and-Bracket-Expressions.html

`echo "Hello hello World world" | tr [:upper:] [:lower]`
translates all upper case characters to lowercase characters
**output:** hello hello world world

`echo "Hello hello World world" | tr [:lower:][:upper]`
**output:** HELLO HELLO WORLD WORLD


*alnum*: numbers and letters
`echo "Hello hello World world" | tr [:upper:] [:lower] | tr '[:alnum]' 'n'`
substitutes all alphanumerical characters into the letter n.
**output:** nnnnn nnnnn nnnnn nnnnn

Instead, we want to enter a new line. And instead of substituting the words that we want to count, we need to substitute the non alphanumerical spaces into new lines. 

`echo "Hello hello World world" | tr [:upper:] [:lower] | tr -c '[:alnum]' '\n`
`-c` is the compliment. (המשלים)

![[Pasted image 20230803095145.png]]

But that results in unnecessary new lines. 

`echo "Hello hello World world" | tr [:upper:] [:lower] | tr -sc '[:alnum]' '\n'`
`-s` is for squeeze   .
![[Pasted image 20230803095703.png]]


![[Pasted image 20230803100716.png]]
`curl -s`
`-s` is for silent mode

![[Pasted image 20230803101514.png]]
`-c` in `uniq` is for count

---
 ## User Account Management
- `useradd`
  ![[Pasted image 20230808112647.png]]
- `groupadd`, located in `/etc/group
  ![[Pasted image 20230808115325.png]]`
- `userdel`, `userdel -r` to also delete the user's home directory.
  
- `groupdel`
  ![[Pasted image 20230808115429.png]]`
- `usermod` - modify a user
  ![[Pasted image 20230808112744.png]]
  ![[Pasted image 20230808115754.png]]
  - `gpasswd` - Is used to administer the `/etc/group` file
    `gpasswd [option] [GROUP]`
    ![[Pasted image 20230808120026.png]]
    

Files:
- `/etc/passwd`
  ![[Pasted image 20230808112218.png]]
  
- `/etc/group`
- `/etc/shadow`

`id username` to verify that we created user

`cat /etc/group` to verify that the new group was created

automatically adds spiderman to spiderman group when creating useradd spiderman

`-m` to create home directory for the user

`useradd babubutt -m(Create home dir) -s /bin/bash`(set bash to be the default shell command interpreter)

`chsh -s /bin/bash`

---
## Password Aging - chage
`chage [-m min days] [-M max days] [-d last day] [-I inactive] [-E expire date] [-W warn days] user`

File = `/etc/login.defs`
- `PASS_MAX_DAYS 99999`
- `PASS_MIN_DAYS 0`
- `PASS_MIN_LEN 5`
- `PASS_WARM_AGE 7`

![[Pasted image 20230803115633.png]]

---
## Switch Users and sudo Access

#### Commands:
- `su - [USERNAME]`
- `sudo [command]`
- `visudo - /etc/sudoers` - used to configure user permissions
  ![[Pasted image 20230808121238.png]]
![[Pasted image 20230808121011.png]]

%wheel allows people in group wheel to run all commands

![[Pasted image 20230808121226.png]]
![[Pasted image 20230808121449.png]]

`sudo` requires the password of the current user whereas `su` requires the password of the substitute account.
![[Pasted image 20230808121847.png]]

`sudo` is a safer method to run commands because it does not require a password exchange (student01 does not need to know the password of adminuser).


`usermod -aG wheel anan` 
adds user anan to the wheel group that has all permissions to run all commands


---
## Monitor Users
- `who` - how many people are logged in, user ID, terminal ID and how long have they been logged in. `who -H -a` to display information about the users who are logged in and some additional information.
- `last` - every user that has logged in.
- `w` - works the same as who, just gives more information.
- `finger` - does the trace of a user where its coming from and what kind of protocol is using.
	  CentOS 8 and newer, finger was replaced with pinky.
- `id.` - `id username` displays info about a user.

---
## Talking to Users
Communicating with all users connected to a certain server or application.
- `users` - shows all users that are currently logged in.
- `wall` - broadcasts a message to everyone that's logged into the Linux system.
- `write` - dedicated to one single user.

`wall` then double enter, write a message and then `CTRL + D` to broadcast the message. Directed to anyone that is logged in.

Writing a message to a specific user: `write username`, press enter and then write your message, press enter and it will be broadcasted to the specific user. The user who got the message can also message back using the same command in the same syntax to the administrator that sent the message.

---
## Linux Account Authentication

If a user joined the company and we have to make an account for the user for every service there is. We are not going to make tens of accounts for all the different services or servers, and for that, we use Linux Account Authentication.

Types of accounts:
- Local accounts
- Domain/Directory accounts
 ![[Pasted image 20230806195024.png]]

![[Pasted image 20230806194938.png]]
Windows = Microsoft Active Directory

LDAP is a protocol that is used for any OS, to authenticate a directory.

---
## Difference between Active Directory, LDAP, IDM, WinBIND, OpenLDAP etc.

- Active Directory = Windows
- IDM = Identity Manager. Created by RedHat. 
- WinBIND = Used in Linux to communicate with Windows (Samba). Allows Windows users to connect to Linux machines using WinBIND.
- OpenLDAP (open source)  
  LDAP is a directory service
- IBM Directory Server. Proprietary product.
- JumpCloud 
- LDAP = Lightweight Directory Access Protocol

---
## System Utility Commands

- `date` - tells the date, time and year. Can be used in a script.
- `uptime` - tells us how long the system has been up for, load average etc:
  ![[Pasted image 20230806200028.png]]
- `hostname` - tells us the hostname. Running it is recommended each time we log into a system. `hostname -s` to display a shortened version of a computer's host name.
- `uname` - `uname -a` gives us information about the system, what its running etc.
- `which` - `which pwd` looks for the commands shows us where its located in the system
- `cal` - short for calendar. gives us a calendar. `cal 9 1977` will show us september 1977. `cal -j` to see the Julian dates for your current month. `cal -s` or `cal -m` to see alternative views of the calendar.
- `bc` - opens a calculator in the terminal
---
## Processes and Jobs
- Application = Service
- Script
- Process - When we run an application, it runs a process. Could be a single process, could be multiple processes.
- Daemon - keeps running in the background and keeps listening to incoming or outgoing traffic.
- Threads 
- Job - Created by a scheduler

### Process/Services Commands
- `systemctl`
- `ps` - shows us what processes are running in the system
- `pstree` - the same as ps, except it shows the results in a tree format
- `top` - shows processes in the system showing based on the load, showing memory and CPU usage
- `kill` - stops processes 
- `crontab` - schedules processes or applications 
- `at.` - one time basis, same as crontab
---
## `systemctl` command

It is used to start an application.
Is a tool to control system services. Replaced the old command `service`.

Syntax: `systemctl <subcommand> <service name>`
	Subcommands include `status`, `start`, `stop`, `restart`, `enable` and `disable`

Example:
- `systemctl start|stop|status servicename.service (firewalld)`
  `systemctl status firewalld.service` - Checks if the service is running and is enabled or not.
  `systemctl stop firewalld.service` 
  `systemctl disable firewalld` - disables at boot time.
- `systemctl enable servicename.service`
- `systemctl restart|reload servicename.service`
- `systemctl list-units --all` - gives us all services that are running and ones that are inactive.
- `systemctl list-units --type=service --state=active` - lists all active services
  ![[Pasted image 20230806201254.png]]
  
### To add a service under systemctl management:
Create a unit file in /etc/systemd/system/servicename.service

Can also be used to power off, halt and reboot our machine:
`systemctl poweroff`
`systemctl halt`
`systemctl reboot`

----
## `ps` Command

`ps` command stands for process status and it displays all the currently running processes in the Linux system

`ps` = shows the processes of the current shell

*PID* = the unique process ID
*TTY* = terminal type that the user logged-in to
*TIME* = amount of CPU in minutes and seconds that the process has been running
*CMD* = name of the command

`pidof [OPTIONS] programName`
This command displays the `process ID` (PID) of a running program.

- `pstree` - the same as ps, except it shows the results in a tree format
- `ps -e` = shows all running processes
- `ps aux` = shows all running processes in BSD format
- `ps -ef` = shows all running processes in full format listing
- `ps -u username` = shows all processes by username
![[Pasted image 20230810002022.png]]

---
## `top` Command

- `top` is used to show the Linux processes and it provides a real-time view of the running system
- This command shows the summary information of the system and the list of processes or threads which are currently managed by the Linux Kernel
- When the top command is executed then it foes into interactive mode and you can exit by hitting `q`
![[Pasted image 20230806202354.png]]
Zombie process is a process whose parent process is dead and is still running in the background. The child process becomes a zombie process.
![[Pasted image 20230810001808.png]]

- `top -u user` - shows tasks/processes by user
- `top + c` - shows commands absolute path
- `top + k` - after pressing k, we are prompted to enter a process ID.
- `top + M and P` - to sort all Linux running processes by memory usage
![[Pasted image 20230810002638.png]]







> top command refreshes every 3 seconds.

---
## `kill` Command

Used to terminate processes manually
Sends a signal which ultimately terminates or kills a particular process or group of processes.

`kill [OPTION] [PID]`
*OPTION* = Signal name or signal number/ID
*PID* = process ID

`kill -l` = to get a list of all signal names or signal number. Signals tell the kill command what to do.

- `kill PID` = kill a process with default signal
- `kill -1` = Restart process
- `kill -2` = interrupt from the keyboard just like `CTRL + C`
- `kill -9` = forcefully kill a process (SIGKILL)
- `kill -15` = kill a process gracefully (SIGTERM)
- `kill -19` = Pauses the process and can use the command line (SIGSTOP)

`killall` - kills the process and all related processes
`pkill` - kills process by process name and not by process ID

---
## `crontab` Command

`crontab` is used to schedule tasks
Lets us schedule a job or a process to run at a specific time.

There is the `cron` daemon and then there's the `crontab`. The difference is that the `crontab` specifies commands or scripts to be run at a specific time, which the user can modify. The commands and steps are stored in the `crontab` file that holds the commands and steps that the `cron` daemon will run.
The `cron` daemon can check the file each minute for scheduled tasks, and then then the `cron` daemon will run these tasks.



- `crontab -a fileName` = creates the `crontab` file that holds the commands and steps that the `cron` daemon will run
- `crontab -e` = edit the crontab (copy the original crontab text to a new file for backup)
- `crontab -l` = list the crontab entries
- `crontab -r` = remove the crontab
- `crond` = crontab daemon/service that manages scheduling
- `systemctl status crond` = to manage the crond service
![[Pasted image 20230806203742.png]]
The `crontab` file format has six fields:
- `MIN`: Minutes - any value from 0 to 59
- `HOUR`: Hour - any value from 0 to 23
- `DOM`: Day of month - any value from 1-31
- `MON`: Month - any value from 1-12
- `DOW`: Day of week - any value from 0-6
- `CMD`: Command - any command or path


> Note: There is a system `crontab` and user `crontab`:
> 	- System wide scheduled tasks are managed by root at `/etc/crontab`
> 	- Each user manages user-specific tasks at `/var/spool/cron/crontabs/$USERNAME`
> 	- `crontab -e` should always be used to edit the scheduled tasks. 


MINUTE HOUR DAY OF THE MONTH(* FOR EVERY DAY) 10(OCTOBER) \*(EVERYDAY OF THE WEEK) and then the command we want to run. we can output it to a file crontab-entry

There are `cron` directories that are precreated and prescheduled directories that administrators can use to store scripts that will run at specified times:
- `/etc/cron.daily`
- `/etc/cron.hourly`
- `/etc/cron.monthly`
- `/etc/cron.weekly`


---
## `at` command
Like crontab, lets you schedule jobs but only once.
When the command is run it will enter interactive mode and you can get out by pressing `CTRL+D`

Usage:
- `at HH:MM PM` = Schedule a job
- `atq` = list the at entries
- `artm #` = remove an entry
- `atd` = at daemon/service that
- `systemctl status atd` = to manage the atd service.

Creating an at entry by scheduling a task:
`at 4:45PM`, *PRESS ENTER* `echo "this is my first entry" > at-entry` *CTRL+D*


Other future scheduling format:
`at 2:45 AM 101621` = schedule a job to run on Oct 16th, 2021 at 2:24am
`at 4PM + 4 days` = schedule a job at 4pm four days from now
`at now +5 hours` = schedule a job to run five hours from now
`at 8:00 AM Sun` = schedule a job to 8am on coming Sunday
`at 10:00 AM next month` = schedule a job to 10am next month

---
## Additional Cron Jobs

- By default there are 4 different types of cronjobs
	- Hourly
	- Daily
	- Weekly
	- Monthly
- All the above crons are setup in `/etc/cron.___(directory)`
- The timing for each are set in `/etc/anacrontab --` except hourly
- For hourly `/etc/cron.d/0hourly.`


---
## Process management
- Background =`Ctrl + z`, runs in the bg
	  `bg [job process number or name]` to run in the bg

- Foreground = `fg [job process number or name` to run in the foreground 

- Run process even after exit = `nohup [process] &`
		OR = `nohup process > /dev/null 2>&1 &`

- Kill a process by name = `pkill`

`man 7 signal`
To read more about the rest of the signals

- Process priority = `nice (nice -n 5 [process])`
		Goes from -20 to 19. The lower the number the more priority a task gets

- `renice` - Adjusts the priority of a process. Used for running processes.

- Process monitoring = `top`

- List process = `ps`

Every time we run a process, it attaches itself to that terminal. Closing the terminal will stop the process.
There is a workaround that lets us run commands with no regards to whether the terminal is running or has been terminated: we use `nohup`.

`nice -n (set priority)`
`nice -n 5 sleep 10`
This gives the sleep command a priority of 5.

---
## System Monitoring

- `lscpu` - list CPU information
- `lshw` - List hardware
- `top` - lists all processes running, similar to task manager on windows.
- `df` - display disk size and free space. `df -h` makes the output more human readable. 
	  https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html#df-invocation
- `vmstat` - Indicate use of virtual memory
- `du` - check file and directory sizes
- `dmesg` - Show
- `iostat` - input output statistics
- `netstat` - prints network connection, all things internet connectivity
- `free` - displays the amount of free and used memory in the system
- `cat /proc/cpuinfo` - proc stores info about the system CPU
- `cat /proc/meminfo` - shows us information about the system memory
- `uptime` Indicate the amount of time that the system has been up, number of users, and CPU wait time.
---
## Log Monitoring

There are different types of logs:
- System logs (system startup information and system shutdown times)
- Events logs (user login and logout events)
- Applications logs (startup time, actions and errors)
- Services logs

Usually used to trace which applicated triggered an error, which user made a wrong action or which outside host accessed the server.

Logs are key to security audits (gathering information about the system) and service-level agreements (troubleshooting must start within x hours after an issue occurs).

![[Pasted image 20230810203156.png]]


- Log Directory = `/var/log` - Directory that stores all the logs
	 `ls -more /var/log`: We get a comprehensive list of all logs

- `more boot log` - gives us all boot logs, errors and or checks
	Rebooting will generate a new boot file 

- `boot` - booting up logs

- `chronyd`  

- `cron` - daemon to execute scheduled commands.

- `maillog` - all information about our emails

- `secure` - records all logging in and log out information. 

- `messages` - every time there is an issue with our machine, we usually go to the messages log. Has all kinds of information, app information, processes information, system information etc.
  What is going on with our system, what failed and when it failed.
- `httpd`

The Linux operating system offers logging levels that indicate the Severity Level and identification:
![[Pasted image 20230810203425.png]]

### Important log files:

| Log File                      | Description                                                               |
| ----------------------------- | ------------------------------------------------------------------------- |
| `/var/log/syslog`             | Stores system information                                                 |
| `/var/log/secure`             | Stores authentication information for Red Hat-derived distributions       |
| `/var/log/kern`               | Stores Linux kernel information                                           |
| `/var/log/boot.log`           | Stores startup messages                                                   |
| `/var/log/maillog`            | Stores mail messages                                                      |
| `/var/log/daemon.log`         | Stores information about running background services                      |
| `/var/log/auth.log`           | Stores authentication information for Debian-derived distributions        |
| `/var/log/cron.log`           | Stores cron messages for scheduled tasks                                  |
| `/var/log/httpd`              | Stores Apache information for Red Hat-derived distributions               |
| `/var/log/YUM`                | Stores YUM installer information for Red Hat-derived distributions        |
| `/var/log/apache2/access.log` | Stores Apache authentication information for Debian-derived distributions |
| `/var/log/lastlog`            | Stores information about successful logins to the host                    |

#### `lastlog` command
Retrieves user information from the `/var/log/lastlog` file and outputs it in the console.

- `lastlog -u ec2-user` displays information of the ec2-user only.
- `lastlog -t 1` displays login information more recent than 1 day ago.
- run `man lastlog` for more options



---
## System Maintenance Commands

- `shutdown` - `shutdown -H` is the same as `halt`
- `init 0-6`
- `reboot` - reboots our computer, shuts it down and then powers it back on.
- `halt` - shuts down right away. As if we are pressing a long press on the physical system to shut it down. Doesn't care about the processes running. Force shuts.

---
## Changing system Hostname
In case our machine is being used to something else, decommissioned or just used for another purpose and now we want to change the hostname. 
`hostname` - displays the hostname.
- `hostnamectl` - First, have to become root. /etc/hostname is the file that stores our hostname details.
  `hostnamectl set-hostname nychost1`
  Running the command will change the /etc/hostname file and now your hostname has been changed. 
  We have to restart the machine in order to see the changes in our terminal.
  Alternatively, we can directly change the contents of /etc/hostname 
  Reboot, and then get the new hostname
- Version
- Version

___
## Finding System Information

- `cat /etc/redhat-release` - a file that tells us what Linux we are running
- `uname -a` - tells us date and time, hostname, Linux kernel and all kinds of information about the machine.
- `dmidecode` - `dmidecode | more` to see information one page at a time. Tells us information about the machine such as the manufacturer, hardware information and more. 
- `hostname` - tells us what hostname we using

---
## System Architecture
Two types:
- 32 bits
- 64 bits

Main difference is the number of calculations per second they can perform.
There is backward compatibility, 32 bit apps can run on 64 bit computers but not the other way around.

- `arch` - displays the CPU architecture of your machine.
---
## Terminal control keys
Key combos have special effect on the terminal.

- `CTRL + c` stop/kill a command. Force stop.
- `CTRL + z` stop/kills a command, politely
- `CTRL + u`  erase everything you've typed on the command line
- `CTRL + d` exits from an interactive program (signals end of data)
---
## Terminal commands

- `clear` - clears the screen
- `exit` exit out of the shell, terminal or a user session
- `script` stores terminal activities in a log file.
  Records everything we do in our session.
  `script logfile-activity.log` creates a log file that will store all terminal activity. All commands and all output is recorded. `exit` command will stop it from recording any further. The terminal will display a message that the logging has stopped.
---
## Recover Root Password

- Restart the computer
- Edit the grub file
- Change password
- reboot

We can force reset using our VM. Select the right boot, and then press `E`, and then edit the grub file.
delete `ro`

>If on centos or redhat, simply go to the last of the line and write `rd.break`

Change the `ro` to `rw` and then add `init=/sysroot/bin/sh`
`ctrl+x`
`chroot /sysroot`
`passwd root`
`exit`
`reboot`

Before exiting, update SELinux info by running `touch /.autorelabel`

---
## SOS Report

Redhat created SOS as a command, collects and packages diagnostic and support data. 
`sos-version` gives us the SOS version

`sudo apt-get install sosreport`

`sos-report`
Will automatically collect the data, package it and save it in a tar file. Once completed, the terminal will ask us to share the package file.

---
## Environment variables

Dynamic-named value that can affect the way running processes will behave on a computer. 
In simple words: set of defined rules and values to build an environment.

To view all environment variables:
- `printevn` OR `env`

To view ONE environment variable:
`echo $SHELL`

`echo $USERNAME` will echo your username.

To set the environment variables:
`export TEST=1`
`echo $TEST`

Meanings to some of the environment variables:
- `XDG_VTNR` - specifies the virtual terminal number
- `XDG_SESSION_ID` - specifies the session ID
- `HOSTNAME` - specifies the name of the computer
- `SHELL` - specifies the shell path
- `TERM` - defines terminal handling


To set environment variable permanently
It is recommended to backup our .bashrc file in case of a failure or unwanted behavior:
`cp .bashrc bashrc.orig`

`vi .bashrc`
`TEST='123'`
`export TEST`

To set global environment permanently. Meaning, setting the environment variable to anyone that logs into the machine and not just to a single user.
`vi /etc/profile or /etc/bashrc`
`TEST='123'`
`export TEST`

>`echo $MAIL` will return the mail directory where the mail is defined

>`echo $HOME` will return our home directory

https://bash.cyberciti.biz/guide/Unset
The `unset` command unsets variables in our current session. Can remove both functions and shell variables.

![[Pasted image 20230810214616.png]]

---
## Special Permissions with `setuid`, `setgid` and `sticky bit`

`setuid` tells Linux to run a program with the effective user id of the owner instead of the executor

`setgid` tells Linux to run a program with the effective group id of the owner instead of the executor 

`sticky bit` is a bit set on files/directories that allows only the owner or root to delete the files

- to assign special permissions at the user level:
  `chmod u+s xys.sh`
- to assign special permissions at the group level:
  `chmod g+s xyz.sh`
- To remove special permissions at the user or group level:
	  `chmod u-s xyz.sh`
	  `chmod g-s xyz.sh`

<mark style="background: #FF5582A6;">To find all executables in Linux with `setuid` and `setgid`
find / -perm /6000 -type f</mark>

Note: Only works on .exe files (files that are written in C or CPP)(?)

>Note: 2000/4000/6000 are incomplete permissions, so you should replace 000 with the appropriate permissions, e.g. 4755.

https://www.sobyte.net/post/2022-04/linux-suid/

`Sticky bit`
- It is assigned to the last bit of permission
  `-r w x  r w x  r w` <mark style="background: #FFB86CA6;">t</mark>
  The highlighted bit is the sticky bit, Why?
  If we have a t, it means that although the user has read write permissions, he cannot delete the file.

- Become root and create `dir mkdir /allinone`
assign all `rwx` to the dir: `chmod 777 /allinone`
- Become user and create dir inside of `/allineone`: `mkdir imrandir`
- Give all rwx perms to the dir: chmod 777 imrandir
- create 3 files in that dir: `touch a b c`
- Logging as another user and trying to delete the imrandir directory will result in deleting it.

Now, becoming root and assigning sticky bit permission to `/allinone` dir: `chmod +t /allinone`

Become user and create a dir inside of `/allinone`
Give all `rwx` perms to that dir
Create 3 files in that dir: `touch a b c`
Become another user again and try to delete that dir
We wont be able to delete the directory.

<mark style="background: #FF5582A6;">When we see a capital letter T as the sticky bit then it means that the others do not have an execute permission.</mark>

---
## Aliases

`alias alias_name='command'`

By using aliases, you can define new commands by substituting a long command with a short one.
Can be set temporarily in the current shell. 
Can be set permanent by adding them to the user's `.bashrc` file.

`alias 'lsd'='ls -l -a'
`unalias ''

Can be used when we want a shorter version of a long command that is used daily.

`alias ls="ls -al"`
`alias pl="pwd; ls"`
`alias tell="whoami; hostname"`
`alias dir="ls -l | grep ^d"`

---
## Creating User or Global Aliases

- User = Applies only to a specific user profile
- Global = Applies to everyone who has account on the system

User = `/home/user/.bashrc`
Global = `/etc/bashrc`

---
## Shell History

Every command that we run in the terminal is recorded in the command history.

`history` gives us a comprehensive list of all commands that have been run in the terminal. 
Records since we have logged into the system.


If we want to run command 406 from `history` as example, we can run the following command: `!406`

The history of the shell commands are saved in `/home/user/.bash_history`

To view other users history of shell commands:
Become root (`su -`)
`cat /home/user/.bash_history`

---

## Network Components

- IP = Internet protocol
- Subnet mask

![[Pasted image 20230806153633.png]]
![[Pasted image 20230806153850.png]]

- Gateway
- Static vs. DHCP
- Interface
- Interface MAC
---
## Network Files and Commands

- Interface Detection
- Assigning an IP address
- Interface configuration files
	- /etc/nsswitch.conf
	- /etc/hosts
	- /etc/sysconfig/network
	- /etc/sysconfig/network-scripts
	- /etc/resolv.conf

`enp0s3` is our name of the interface

`cd /etc/sysconfig/network-scripts`
`BOOTPROTO=____` change from dhcp to static

- Network commands
	- `ping`
	- `ifconfig` - 
	- `ifup` or `ifdown`
	- `netstat`
	- `tcpdump` - traces every single transaction that is leaving your machine and coming into our machine

---
## NIC
Network Interface Card

`lo` = loopback device, special interface that the machine uses to communicate with itself. Used for diagnostics and troubleshooting and to connect to servers running on the local machine.

`virb0` = "Virtual Bridge 0" used for NAT (Network Address Translation). Virtual environments sometimes use it to connect to outside networks.

`ethtool virb0` - will tell us that device is connected

`ethtool ens33` to check if its a duplex connection, connection speeds etc.


---
## NIC Bonding
NIC = Network Interface Card (PC or Laptop)

NIC Bonding, also known as Network bonding. Can be defined as the aggregation or combination of multiple NIC into a single bond interface. It's main purpose is to provide high availability and redundancy.

![[Pasted image 20230806161819.png]]
We can also aggregate ports for a higher bandwidth. Link aggregation.

### NIC Bonding Procedure

- `modprobe bonding`
- `modinfo bonding`
- Create /etc/sysconfig/network-scripts/ifcfg-bond0
- Edit /etc/sysconfig/network-scripts/eth0
- Edit /etc/sysconfig/network-scripts/eth1

After restarting and running `ifconfig`, we should be able to see two network interfaces.

---
## Download Files or Apps (`wget`)

- Can do a recursive download
- Supports HTTP, HTTPS, and FTP protocols
- Performs retries over an unreliable connection

`wget "insertlink"`

If a certain app does not exist in the default repository, we can just use a download link through the browser and then use the `wget` command to download the installation package.

---

## `curl` and `ping` Commands

- Downloads a single resource only
- Supports HTTP, HTTPS, FTP and many other additional protocols (such as FTPS and FILE)
- Runs on more platforms than `wget`

`curl http://website.com/filename` brings the content of the page/file. Most likely html source code etc. If it returns something, it means that the website is up which is good.
`curl -O http://website.com/filename`

`ping www.google.com`

`nslookup`

To download something from the internet using the `curl` command:
`curl -O [link_goes_here]`
Where does it download it? Usually downloads it in whichever directory we are currently at.

---
## FTP - File Transfer Protocol

FTP is a standard network protocol used fort the transfer of computer files between a client and a server on a computer network.

Protocol = Set of rules used by computers to communicate. 

Default FTP Port = 21

A server has to be running a listening service to receive the protocol, we have to make sure its running `ftpd` (FTP daemon), it will run on the 21 port by default.

When we need to connect to our FTP server, we have to run systemctl status vsftpd in order to make sure that the service is running.

Once that has been established, look for /etc/vsftpd.conf and edit the file. 
If you cannot find the file, first you have to stop vsftpd before configuring by running /etc/init.d/vsftpd stop

Once you have the config file opened, go to `anonymous_enable` and write NO, so the line should look like `anonymous_enable=NO` without the hashtag at the beginning.

Then, we have to uncomment (remove the hashtags) from the following lines:
`ascii_upload_enable=YES`
`ascii_download_enable=YES`

Then, uncomment (remove the hashtag at the beginning of the line) `ftpd_banner`

And then add the following line to the end of the file:
`user_localtime=YES`

Then, we have to run the following commands:
`systemctl start vsftpd`
`systemctl enable vsftpd`
`systemctl stop firewalld`
`systemctl disable firewalld`

Now, once we have all those steps done, go to your client machine and run `ftp 192.168.136.x` (the ip is taken from `ifconfig` from the server side)
Once you run that, you can specify as what user you are connecting to the server (if it says none on the console then just type your name and press enter).
Enter password and afterwards you should be connected to the server.

Then, in the client side, enter `bi` and run it in order to switch to Binary mode.

Then run `hash` so that we get to see the upload/download progress.

---
## rsync - Remote Synchronization

 ![[Pasted image 20230806231826.png]]

---
# Module 8

## System Run Level

### Main Run Level
- `0` Shut down (or halt the system)
- `1` Single-user mode; usually aliased as s or S - to troubleshoot issues
- `6` reboot the system

### Other run levels
- `2` multiuser mode without networking
- `3` multiuser mode with networking
- `5` multiuser mode with networking and GUI
- `4` is user-definable

`init 0`
`who -r` tells us what run level we are currently at

---
## Computer Boot Process

Power goes through the socket, to the power supply unit and then to the motherboard which in turn powers on the CPU and the BIOS. The CPU starts and pulls instructions from the BIOS.
The BIOS is a software on a little chip on the motherboard which is only readable. The BIOS code is saved on ROM  (Read only memory).
The BIOS settings such as time, date etc is saved on the CMOS. The CMOS runs on a battery that is located on the motherboard.
POST - power on self test. The CPU goes through every device that is attached to the PC and checks if its running properly.
Once the computer posts, the BIOS goes to the MBR (Master boot record) located in the HDD and the OS is then loaded onto the computer memory (RAM). 
The entire process of booting up is called Bootstrap

---
## Linux Boot Process

![[Pasted image 20230807100826.png]]
After pressing power on, the computer looks into the BIOS which in turn looks at the MBR (Master Boot Record) which is usually a really small code that executes GRUB (Grand Unified Bootloader) which in turn executes the Kernel. The Kernel then executes`/sbin/init/`. Init executes run level programs; Runlevel programs are executed from `etc/rc.d/rc*.d` 

![[Pasted image 20230807101050.png]]
![[Pasted image 20230807101443.png]]

---
## Linux Boot Process

`systemd` is the new service manager in CentOS/RHEL 7 that manages the boot sequence.

Backward compatible with `SysV init script` used by previous versions.

`BIOS` = Basic Input and Output Setting (firmware interface)
POST = Power-On Self_Test started; asks all devices if they are okay and working properly


`MBR` = Master Boot Record
Information saved in the first sector of a hard disk that indicates where the GRUB2 is located so it can be loaded in computer RAM


`GRUB2` = Grand Unified Boot Loader v2
*Loads Linux Kernel*
`/boot/grub2/grub.cfg`


`Kernel` = Core of Operating System
Loads required drivers from `initrd.img`
Starts the first OS process (`systemd`)


`Systemd` = System Daemon (PID #1)
It then starts all the required processes
Reads = `/etc/systemd/system/default.target` to bring the system, to the run-level total of 7 run-levels (0 through 6).

---
## Message of the Day

A message that shows up on the screen every time a user is connected to the Linux machine machine. 
For example, when connecting to a remote server usually we are prompted with a security warning.

- `/etc/motd`

---
## Customize message of the day

Instead of manually going to `/etc/motd/` we can do:
Create a new file `/etc/profile.d/motd.sh`
Add desired commands in `motd.sh` file
Modify the `etc/ssh/sshd_config` to edit `#PrintMotd yes`
to `PrintMotd no`
Restart sshd service -> `systemctl restart sshd.service`


In the script itself, we can simply use `hostname` and `whoami` 
"You are logged in as `whoami`"
And the script will automatically show the relevant hostname and username to each user that connects to the Linux machine.

`uname -r` to display the kernel version

---
## Computer Storage

- Local Storage 
	- RAM, HDD, SSD, etc.
- DAS (Direct Attached Storage)
	- CD/DVD, USB flash drive, external directly attached with USB or other cables
- SAN (Storage Area Network)
	- Storage attached through iSCSI or fiber cable
- NAS (Network Attached Storage)
	- Storage attached over network (TCP/IP)
	- E.g. Samba, NFS etc.

---
## Disk Partition

Commands for disk partitioning:
- `df` - `df -h` will give us human readable output
- `fdisk` - `fdisk -l` we will see the disk size. And the disk partitions

Useful when we want to add new partitions and add more storage to our system

---
## Adding Disk and Creating Partition

Purpose? Out of space. Or additional space for apps etc.

Commands for disk partitioning:
- `df`
- `fdisk`

`fdisk -l` So that we can see the newly added disk
`fdisk /dev/sdb` we run this on the newly added disk
- we press `n` for new
- `p` for primary
- K,M,G 2 partitions +1G for two partitions each being 1G (?) but we go with default
- Once we proceed, we press `w` to write the changes

`mkfs.xfs` (to create filesystem) `/dev/sdb`
then we have to `mount` `/dev/sdb1` `/data` (/data is the name of the partition in the filesystem)

But in order to have it mounted on every bootup, then we go to `/etc/fstab`
And then add the newly created disk: add the following line: `/dev/sdb1 /data xfs defaults 0 0`

---
## Logical Volume Management (LVM)

- LVM allows disks to be combined together
![[Pasted image 20230807112450.png]]

---

## LVM Configuration During Install
187 in the Udemy course

---

## Add Disk and Create LVM Partition
188
![[Pasted image 20230807113858.png]]

`fdisk -l` So that we can see the newly added disk

**Partitions and Physical Volume creation:**
`fdisk /dev/sdb` we run this on the newly added disk
- we press `n` for new
- `p` for primary
- K,M,G 2 partitions +1G for two partitions each being 1G (?) but we go with default
- Once we proceed, we press `t` to change type of partition from 'Linux' to 'Linux LVM'
- Then `w` to write the changes and to write the physical volume.


**Volume Groups:**
Next, we need to create the volume group: `vgcreate (name of volumegroup) /dev/sdcl`

>To verify, run `vgdisplay (name of volumegroup)`

**Logical Volumes:**
`lvcreate -n (name of logical volume) --size 1G (name of volumegroup)`

>To verify, run `lvdisplay`

**File System Creation:**
And then we run the `mkfs.xfs` on the logical volume:
`mkfs.xfs /dev/oracle_vg/oracle_lv`
Make a directory in the logical volume: `/oracle`

And then we finally mount the disk and directory:
`mount /dev/oracle_vg/oracle_lv /oracle`

---
## Add and extending disk using LVM

If we already have a disk and its full. We need to extend it. 

Few options:
- Delete older files to free up disk space
- Add new physical disk mount to /oracle2 but we don't always have a free physical slot to do that
- Create a new virtual disk and mount to /oracle2 
- Or extend /oracle through LVM

Go to settings -> Storage -> Create Virtual Hard Disk -> give it a different name -> give it the desired size

Start your virtual machine.
Login as root

`df -h` to see our disk info
`fdisk -l` to find our newly added disk

In this case, our newly added disk is called `/dev/sdd`

`fdisk /dev/sdd`

Continue using the same steps as before
Reboot the system

run `fdisk -l` again to check our newly created disk


Now we want to extend our full disk.

`pvdisplay` to find which volume group our full disk belongs to.
We want to add a new disk to the same group which the full disk belongs to.

`pvcreate /dev/sdd1/`
`vgextend oracle_vg /dev/sdd1`

`lvextend -L+1024MB /dev/mapper/oracle_vg-oracle_lv

`resize2fs /dev/mapper/oracle_vg-oracle_lv`
`xfs_growfs /dev/mapper/oracle_vg-oracle_lv`

And then we need to verify with `df -h`

---
## Add/Extend Swap Space

Used when our RAM is full. The system uses the slower storage to store the things it needed to write into the RAM. Also called Virtual Memory.

Recommended Swap size is usually twice as big as the RAM.

Commands:
- `dd`
- `mkswap`
- `swapon` or `swapoff`

`free -m` To see physical memory and the Swap memory

How can we extend the Swap space?
We can slice some of the disk drive and use it for Swap.

Say we already have 1Gig of Swap and we want to extend it to 2Gig. We also want to take a slice of the data drive and turn it into Swap memory.

`# dd if=/dev/zero of=newswap bs=1M count=1024`
if - read from file
of - output to file
Creates a file the size of 1Gig

Why not use a touch command. dd command is used since we can control how big the file is going to be.

chmod to the swap file: `chmod go-r swapFile`

Then we use `mkswap` to turn our swapFile into a swap:
`mkswap /newswap`

`free -m` to check 

`swapon /newswap`

Extends the existing swap by adding the swapfile we created to the currently used swap.

To verify, run `free -m`

In order to have the swap file automatically extended using the swapfile we created, we have to edit the `/etc/fstab` and add the following line: `/newswap swap swap defaults 0 0 ` and save it so that it is automatically added on boot.

Reboot the system to verify that the swap has been added on boot-up.

`swapoff /newswap`
`rm /newswap`

---

## Implement Advanced Storage Features
Next Gen volume management solution called Stratis:

1. Uses thin provisioning by default.

2. Combines the process of creating logical volume management and creation of filesystems into one management .

3. In LVM if a filesystem system gets full you will have to extend it manually whereas Stratis extends the filesystem automatically if it has available space in its pool.


In LVM:
![[Pasted image 20230807130738.png]]

In Stratis:
![[Pasted image 20230807130826.png]]


- Install Stratis package
- Enable and start Stratis service `systemctl enable|start stratisd`
-  Add new disks from virtualization software: Add a new VDI.
- Run `lsblk` in order to see that the disks have been added.
- Create a new Stratis pool and verify
  `stratis pool create pool /dev/sdc`
  `stratis pool list` *to verify*
- Extend the pool 
  `stratis pool add-data pool1 /dev/sdc`
  `stratis pool list` *to verify*

- Create a new filesystem using Stratis:
	`stratis filesystem create pool1 fs1` *(we can give the filesystem whichever name we want, fs1 in this case)*
	`stratis filesystem list` *to verify*

- Create a directory for mount point and mount filesystem
	- `mkdir /bigdata`
	- `mount /stratis/pool1/fs1 /bigdata`
	- `lsblk`

- Create a snapshot of your filesystem
	- `stratis filesystem snapshot pool1 fs1 fs1-snap`
	- `stratis filesystem list` *to verify*

- Add the entry to /etc/fstab to mount at boot
	- `UUID="asf-0887afgdja-" /bigdata xfs defaults, x- systemd.requires-stratisd.service 0 0`

---
## RAID 

RAID (Redundant Array of Independent Disks).

Types of RAID:
- RAID0
- RAID1
- RAID5

![[Pasted image 20230807132052.png]]
Usually used for data warehousing. If one of them fails then we lose the data. Used also for backups. 



![[Pasted image 20230807132158.png]]
Mirrors hard disks together. RAID1 is slow!



![[Pasted image 20230807132238.png]]
Some information of DISK1 to DISK2. Some information of DISK2 to DISK3 etc. 
We are not going to have 15 Gigs though. Since some of the information is copied from one disk to another.

RAID mostly configured on the physical disks.

LVM mostly configured on virtual disks.

---

## File System Check (`fsck` and `xfs_repair`)

`fsck` utility is used to check and repair Linux filesystems (ext2, ext3, ext4, etc)

`xfs_repair` utility is used to check and repair Linux filesystems for *xfs* filesystem type
>`df -T` to check what filesystem the Linux is running

Depending on when was the last time a file system was checked, the system runs the `fsck` during boot time to check whether the filesystem is in consistent state by default.

System admin could also run it manually when there is a problem with the filesystems.

Make sure to execute the `fsck` on an unmounted file systems to avoid any data corruption issues. Not mounted to any mount points


What if we wanted to run it on `/root`? The only way to do that is in single user mode or in recovery mode and mount it on the disk.

- Force a filesystem check even if its clean using option `-f`. Instead of going back and forth to check which partitions are clean, we can just use `-f` tp force check all partitions
- Attempt to fix detected problems automatically using option `-y`
- `xfs_repair` is highly scalable. For larger partitions like terabytes. We don't want to wait each time we run the system and that is why it doesn't run automatically on bootup.

Possible exit codes for `fsck` command:
![[Pasted image 20230807151807.png]]

Older versions of RedHat, we are going to see ext\* Filesystems.

When we try to `xfs_repair` a filesystem, the terminal will throw an error since the filesystem is currently mounted.

Thus, we need to unmount first: `unmount /mountpoint`
Once we do that, it will no longer show when we run `df -T` and for that, it is advised to save the path to the said disk.

And then we can run the `xfs_repair` on the relevant disk.

If we get a  `0` once the code finishes running, it means that it found no errors.

After checking, we need to mount our disk back:
`mount /dev/sdbl /data`

This is good for when our system is corrupted. We then use `xfs_repair` to fix it up and bring it back online.

---
## System Backup (`dd` Command)

One of the ways to do a system backup is using the `dd` command.

There are 5 different ways of backups:
1. System backup (entire image using tools such as acronis, veeam, commvault etc.)
2. Application backup (third party application backup solution)
3. Database backup (Oracle dataguard, SQL backup etc.) - backups only the data.
4. Filesystem backup (tar, gzip directories etc.) backups the files and directories etc.
5. Disk backup or disk cloning (`dd` command). Can clone an entire disk and creates an image and then put it on another disk.

`dd` is a command-line utility for Unix and Unix-like OS with the purpose to convert and copy files and partitions.
As a result, `dd` can be used for tasks such as backing up the boot sector of a hard drive and obtaining a fixed amount of random data.

To backup or clone an entire hard disk to another hard disk connected to the same system execute the `dd` command as shown:

 `dd if=\<source file name> of=\<target file name> \[Options]`

 `dd if=/dev/sda of=/dev/sdb`

To backup/copy the disk partition
`dd if =/dev/sda1 of=/root/sda1.img`

Restoring this image file to other machine after copying the .img
`dd if =/dev/sda1.img of=/dev/sdb3`

`df -h` to determine which partition we want to copy
`dd if=/dev/sda1 of=/data/boot.img`
copies partition to filesystem
To verify, we can `cd` to the directory and check if the  `boot.img` is there.

If we wanted to copy a partition to a partition we can do the following:
`dd if=/dev/sda1 of=/dev/sdb1`

---
## Network File System (NFS)

Sharing your files with other computers and users.
It is not local to your computer.

It is a client/server system that allows users to access files across a network and treat them as if they resided in a local file directory.

For example, if you were using a computer linked to a second computer via NFS, you could access files on the second computer as if they resided in a directory on the first computer. This is accomplished through the processes of exporting (the process of which an NDS server provides remote clients with access to its files) and mounting (the process by which client map NFS shared filesystem).


![[Pasted image 20230807154134.png]]
Once server approves the NFS Request, then the server approves:

![[Pasted image 20230807154209.png]]


**Steps for NFS Server Configuration**
On server side which is trying to share its filesystem:
- Install NFS packages: `nfs-utils`, `libnfsidmap`
Once installed, enable and start NFS services
`systemctl enable rpcbind`
`systemctl enable nfs-server`
`systemctl start rcpbind`
`systemctl start nfs-server`
`systemctl start rpc-statd`
`systemctl start nfs-idmapd`

Create NFS share directory and assign permissions
`mkdir /mypretzels`
`chmod a+rwx /mypretzels`

Modify `/etc/exports` to add new shared filesystem
`/mypretzels (IP ADDRESS OF CLIENT MACHINE) (rw,sync,no_root_squash)` = for only 1 host

`/mypretzels *(rw,sync,no_root_squash)` = for everyone

`exportfs -rv`

![[Pasted image 20230807154738.png]]

**Steps for NFS Client Configuration**

Install same packages as above.
Start `rpcbind` service once installed the packages: `systemctl enable rpcbind`
`systemctl start rpcbind`

Make sure the `firewalld` service is disabled: `ps -ef | grep "firewall|iptable"`

![[Pasted image 20230807155345.png]]

>`ip addr` to check a machine's ip address, `ifconfig` alternative


---
## Samba

Samba is a Linux tool or utility that allows sharing for Linux resources such as files and printers to with other operating systems

It works exactly like NFS but the difference is NFS shares within Linux or UNIX like system whereas Samba shares with other OS (Windows, MAC etc)


Samba
Samba shares its filesystem through a protocol called SMB (Server Message Block) which was invented by IBM

Another protocol used to share Samba is through CFIS


- Take a snapshot of your VM
- Install samba packages
- Enable samba to be allowed through firewall (only if you have a firewall running)
- Disable firewall
- Create Samba share directory and assign permissions
- Also change the SELinux security context for the samba shared directory
- Or disable SELinux
- Modify `/etc/samba/smb.conf` file to add new shared filesystem
- Verify the setting
- Once the packages are installed, enable and start Samba services (`smb` and `nmb`)
- Mount Samba share on Windows client
- Additional instructions on creating secure

![[Pasted image 20230807170629.png]]
### Samba download, install and configuration (Taken directly from the Udemy course)

 - Samba is a Linux tool or utility that allows sharing for Linux resources such as files and printers to with other operating systems.
 
 - It works exactly like NFS but the difference is NFS shares within Linux or Unix like system whereas Samba shares with other OS (e.g. Windows, MAC etc.).

 For example, computer “A” shares its filesystem with computer “B” using Samba then computer “B” will see that shared filesystem as if it is mounted as the local filesystem.

 - Samba shares its filesystem through a protocol called SMB (Server Message Block) which was invented by IBM.
 
 - Another protocol used to share Samba is through CIFS (Common Internet File System) invented by Microsoft and also NMB (NetBios Name server).
 
 - CIFS became the extension of SMB and now Microsoft has introduced newer version of SMB v2 and v3 that are mostly used in the industry.

 - Most people, when they use either SMB or CIFS, are talking about the same exact thing. The two are interchangeable not only in discussion, but also in application – i.e., a client speaking CIFS can talk to a server speaking SMB and vice versa. Why? Because CIFS is a form of SMB.
 
### Step by steps installation instructions

First please make sure to take a snapshot of your VM

- Install samba packages:
	- Become root user
	- `yum install samba samba-client samba-common`

- Enable samba to be allowed through firewall (Only if you have firewall running):
	- `firewall-cmd --permanent --zone=public --add-service=samba`
	- `firewall-cmd –reload`

- To stop and disable firewall or iptables:
	- `systemctl stop firewalld`
	- `systemctl stop iptables`
	- `systemctl disable firewalld`
	- `systemctl disable iptables`

- Create Samba share directory and assign permissions
	- `mkdir -p /samba/morepretzels`
	- `chmod a+rwx /samba/morepretzels`
	- `chown -R nobody:nobody /samba`

- Also, you need to change the SELinux security context for the samba shared directory as follows: (Only if you have SELinux enabled)
	- `chcon -t samba_share_t /samba/morepretzels`

- If you want to disable SELinux, follow these instructions
	 `sestatus` (To check the SELinux status)
	 `vi /etc/selinux/config`
		 *Change* `SELINUX=enforcing` To `SELINUX=disabled`
	 and then `reboot`


- Modify `/etc/samba/smb.conf` file to add new shared filesystem (**Make sure to create a copy of `smb.conf` file**).
  Delete everything from `smb.conf` file and add the following parameters:
`[global]`
		`workgroup = WORKGROUP`
		`netbios name = centos`
		`security = user`
		`map to guest = bad user`
		`dns proxy = no`

`[Anonymous]`
		`path = /samba/morepretzels`
		`browsable = yes`
		`writable = yes`
		`guest ok = yes`
		`guest only = yes`
		`read only = no`

- Verify the setting
	`testparm`

- Once the packages are installed, enable and start Samba services
	`systemctl enable smb`
	`systemctl enable nmb`
	`systemctl start smb`
	`systemctl start nmb`

- Mount on Windows client
	Go to the start menu on Windows
	Go to search bar
	Type `\\192.168.1.95` (This is my server IP, you can check your Linux IP by running the command ifconfig)

- Mount on Linux client
	*Become root*
	`yum -y install cifs-utils samba-client`
	Create a mount point directory: `mkdir /mnt/sambashare`

- Mount the samba share
	`mount -t cifs //192.168.1.95/Anonymous /mnt/sambashare/`
	`Entry without password`

- Secure Samba Server
  Create a group `smbgrp` & user `larry` to access the samba server with proper authentication:
	`useradd larry`
	`groupadd smbgrp`
	`usermod -a -G smbgrp larry`
	`smbpasswd -a larry`
	*New SMB password: YOUR SAMBA PASS
	Retype new SMB password: REPEAT YOUR SAMBA PASS
	Added user larry*

- Create a new share, set the permission on the share:
	`mkdir /samba/securepretzels`
	`chown -R larry:smbgrp /samba/securepretzels`
	`chmod -R 0770 /samba/securepretzels`
	`chcon -t samba_share_t /samba/securepretzels`

- Edit the configuration file `/etc/samba/smb.conf` (Create a backup copy first)
	`vi /etc/samba/smb.conf`
	*Add the following lines*
		`[Secure]`
		`path = /samba/securepretzels`
		`valid users = @smbgrp`
		`guest ok = no`
		`writable = yes`
		`browsable = yes`

- Restart the services
	`systemctl restart smb`
	`systemctl restart nmb`

---

## NAS Device for NFS or Samba

A storage can be carved on a Linux server and it can be shared with another Linux machine through NGS or to a Windows machine through Samba service
![[Pasted image 20230807170846.png]]

NFS/Samba or any NAS service can be setup through a dedicated NAS device.
![[Pasted image 20230807170915.png]]

---
## SATA and SAS

- **SATA** stands for Serial Advanced Technology Attachment and **SAS** stands for Serial Attached SCSI (SCSI Stands for Small Computer System Interface, typically pronounced as "scuzzy").
- Both

The main difference is that SAS drives are faster and more reliable than SATA drives.

SAS is generally more expensive and better suited for use in servers or in processing heavy computer workstations. SATA is less expensive and is better suited for desktop file storage

In a SATA cable all 4 wires are placed within the same cable. In a SAS cable, the 4 wires are separated into 2 different cables.

Why divide the wires between 2 cables?
- So you can connect more devices to one another,. With a SATA cable you can only link the motherboard and the storage drive. You could  hook up an expansion device but that takes up valuable room inside your computer
- With a SAS cable, you can hookup the motherboard to both a storage drive and another piece of hardware that has SAS connectors

---
## Difference between Linux 5, 6 and 7

Enhanced feats, better feats and patched bugs are the reason why there are multiple versions of Linux usually.

https://drive.google.com/file/d/1vGKroJy3cDKhiRppIs-9fI31tWs3vHbx/view?usp=drive_link

---

## The `hash` Command

- Displays a list of recently run programs, their location and the number of times they have run.
- Information is maintained by the command in a hash table
- Can be used to reset or modify the hash table
- Location information includes the program's full path name
- Syntax: `hash [OPTIONS] [-p PATHNAME] [OPTIONS] [COMMANDNAME]`

Option examples:
- `-d` = Deletes the location for `commandName` from the hash table
- `-l` = Displays output in a format that can be used as input to another command
- `-p` = Sets `pathName` as the full path location for `commandName`
- `-r` = Empties the hash table
- `-t` = Displays the location of `commandName`

![[Pasted image 20230808232250.png]]

---
## The `cksum` Command

- This command generates a checksum value for a file or stream of data
- It is used to see whether the file was corrupted during transfer
- The `cksum` command displays a cyclic redundancy check (*CRC*) value and the byte count for a file
- If the file's CRC value is the same before and after a transfer, the file was not corrupted.
- Syntax: `cksum [FileName]`

![[Pasted image 20230808232516.png]]

---
## Linux Kernel

Shell sends commands to the kernel upon boot-up
Shell + Kernel = Operating system

![[Pasted image 20230809094222.png]]

---
## Introduction to Shell

What is a shell?
- A shell accepts and interprets commands.
- A shell is an environment in which commands, programs, and shell scripts are run.
- There are many types of Linux shells available. Bash is one of them.

- Shell is like a container
- Interfaces between users and Kernel/OS
- CLI is a Shell

#### Find your Shell:
- echo $0
- Available shells: `cat etc/shells`
- Your Shell? `/etc/passwd/`

### Bourne Again Shell: Bash
- Bash is the default shell in Linux.
- It offers an efficient environment for interacting with the operating system and scripting.

---
## Types of Linux Shells

- Gnome - graphical environment in Linux. 
- KDE - another Linux desktop environment.
- sh - one of the original shells. The bourne shell.
- bash - stands for Bourne Again Shell.
- csh and tcsh - CShell and TCShell. TShell does not run scripts.
- ksh - Korn Shell compatible with sh and bash, adds floating points and more to the shells.

`cat /etc/shells` to see all the type of shells installed in your system.

---
## Shell Scripting

### What is a Shell Script?
A shell script is an executable file containing multiple shell commands that are executed sequentially. The file can contain:
- Shell (#!/bin/bash)
- Comments (# comments)
- Commands (echo, cp, grep, etc)
- Statements (if, while, for etc)

Shell should have executable permissions.
Has to be called from absolute path (`/home/userdir/script.bash`)
Can be called from the current directory.

---
## Shell Script - Basic Scripts

- Outputting to the screen using `echo`

- Creating tasks
	- Telling your id, location, your files/dirs, system info
	- Creating files or directories
	- Output to a file using `>`

- Filters/Text processors through scripts (`cut`,`awk`,`grep`,`sort`,`uniq`, `wc`)
---
## Bash metacharacters

| Metacharacter     | Description                                                                 |
| ----------------- | --------------------------------------------------------------------------- |
| `*` (asterisk)    | Any number of any character (wildcard)                                      |
| `?` (hook)        | Any one character (wildcard)                                                |
| `[characters]`    | Any matching characters between brackets (wildcard)                         |
| \`cmd\` or `$cmd` | Command substitution - uses backticks (\`), not single quotation marks ('') |
| `;`               | Chain commands together                                                     |
| `~`               | Represents the home directory of the user                                   |
| `-`               | Represents the previous working directory                                   |

---
## Redirection operators

| Operator | Description                                                                      |
| -------- | -------------------------------------------------------------------------------- |
| `>`      | Sends the output of a command to a file                                          |
| `<`      | Receives the input for a command from a file                                     |
| \|      | Runs a command and redirects its output as input to another command              |
| `>>`     | Appends the output of a command to the existing contents of a file               |
| `2>`     | Redirects errors that are generated by a command to a file                       |
| `2>>`    | Appens errors that are generated by a command to the existing contents of a file |


---
## Input/Output

- Create a script that takes an input from the user
`read`
`echo`


`#!/bin/bash`
`echo hello, my name is motty`
`echo`
`echo What is your name?`
`read namecont` - waits for user input. We need to assign a variable. The variable name is `namecont`
`echo`
`echo Hello, $namecont`


`#!/bin/bash`
`a=hostname`
`echo hello, my name is $a`
`echo`
`echo What is your name?`
`read b`
`echo`
`echo Hello, $b`

<mark style="background: #FF5582A6;">Note: if we wanted to use a variable that we initialized in an echo command, then we need to use a backtick (`)</mark>

---
## `if-then` Scripts

- If then statement:
	If this happens: do this
	Otherwise: do that 

---
## For Loop Scripts

Keep running until specified number of variable
e.g: `variable = 10` then run the script 10 times 
OR
variable = green

---
## do-while Scripts

`do while`

The while statements continually executes a block of statements while a particular condition is true or met.

e.g: Run a script until 2pm

`while [condition]`
	`do`
		`echo task`
		`echo task`
		`do task`
`done`

---
## Case Statement Scripts

- Case
	If option a is selected = do this
	If option b is selected = do this
	If option c is  selected = do this

---
## Check Other Servers Connectivity

A script to check the status of remote hosts

---

#! /bin/bash
letter=a

if \[\[ $letter = "a"\]\]
then

fi

---
## Customizing Bash Prompt And Internal Bash variables

https://www.baeldung.com/linux/customize-bash-prompt
https://ss64.com/bash/syntax-prompt.html
https://tldp.org/LDP/abs/html/internalvariables.html

