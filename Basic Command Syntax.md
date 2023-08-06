
file:///C:/Users/Anan/Downloads/Linux%20Command%20Line%20for%20You%20and%20Me.pdf

CLI - Command Line Interface.

Most commands follow a simple pattern of syntax:
command (options...) (arguments...)


echo -n > kovitz.txt 
>deletes all content from a text file in linux

**`ls`** - Listing of information about files. 
ls -> listing/list of files

Example: **`ls Documents`** 
It will list the contents of said directory. 

![[Pasted image 20230703160535.png]]
The resulting output is a list of files contained with the `Documents` directory.



Options
**`ls -l`** - results in a "long display". Meaning, gives more information about each of the files listed. 
**`-l`** stands for long.
![[Pasted image 20230703161717.png]]

**`ls -r`** - prints the results in reverse alphabetical order. *Default* is alphabetical order.
**`-r`** stands for reverse.

options can be given separately or combined.
**`ls -l -r`, `ls -lr`, `ls -rl`**; they all will output the same. 

<font color ="green">Executables are usually in green after ls -l prompt or just ls</font>

*cd -* (cd minus) takes us to last directory we were in
CTRL SHIFT + makes font bigger
CTRL - makes font smaller

---

**`aptitude`** command is a package management tool available on some Linux distributions. 

___
Printing Working Directory

**`pwd`** command can be used to discover where you are currently located within the filesystem.
**`pwd`** *[OPTIONS]*

![[Pasted image 20230703162358.png]]
![[Pasted image 20230703162421.png]]
*The output indicates that the user is currently in their home folder.*

**`~`** is equivalent to **`/home/sysadmin/`**

---

Changing Directories
---
**`cd`** (change directory) is a command that changes directories.

**`cd [options] [path]`**

**`cd Documents`** will lead us to the Documents directory (as we are already in the sysadmin directory and Documents is located within).
![[Pasted image 20230703163125.png]]


*Main directory in Linux is called the root directory and is represented by **`/`**
To move to the **`/`** directory, use the **`/`** character as the argument to the **`cd`** command.
![[Pasted image 20230703163405.png]]
![[Pasted image 20230703163428.png]]

Paths are a step by step direction. 
*`Absolute paths`* start at the root of the filesystem.
**/home/sysadmin** is an absolute path.
![[Pasted image 20230703163747.png]]
we can confirm that we have reached the desired directory by using the **`pwd`** command:
![[Pasted image 20230703163837.png]]

*`Relative paths`* start from your current location.
Relative paths start with the name of a directory, as opposed to Absolute paths where they usually start with /.
![[Pasted image 20230703163958.png]]
![[Pasted image 20230703164013.png]]


In the following diagram, we are trying to reach the art directory using a *Relative path*.
![[Pasted image 20230703164110.png]]

A relative path starts from the current directory, however you dont include it in the path. 
First step would be to enter the *School* directory and then entering the *Art* directory.

**`cd School/Art`** as we are using a relative path.
![[Pasted image 20230703164413.png]]
![[Pasted image 20230703164358.png]]

Using the **`pwd`** command to confirm the change:
![[Pasted image 20230703164451.png]]
![[Pasted image 20230703233241.png]]

---
Shortcuts
---
The **`..`** character: takes you back to the parent directory.
![[Pasted image 20230703233547.png]]


The **`.`** character: represents your current directory. Not as useful for the **`cd`** command.


The **`~`** character: the **`~`** symbol represents the home directory of the current user. Home directory is located at */home/sysadmin*. To return to home directory we have to execute the following command: 
![[Pasted image 20230703234345.png]]

---
## Changing file Ownership
*chown* command is used to change the ownership of files and directories.

chown *OPTIONS* *OWNER* FILE

sudo chown root hello.sh: changes ownership to the root user.

---
## Viewing Files

cat *OPTIONS* *FILE*
cat animals.txt: displays the content of animals.txt

head *OPTIONS* *FILE*
tail *OPTIONS* *FILE*
These commands are used to view a select number of lines from the top or bottom of a file. Taking a look at a few lines of a file can sometimes be helpful to ensure that the file is the one you want to use.

head -n *number_of_lines* *FILENAME*
The `-n` option with the `head` and `tail` commands can be used to specify the amount of lines to display.

Delimiter
cat file.txt | cut " " -f1 *(first field)* -d " "*(delimiter, once finds a space, stops looking at the rest of the words in the same row).*

>ls -l >> list2.txt; cat list2.txt
>We could use piping in order to save an output of a command onto a file.

>cat file.txt; echo " "; cat kovitz.txt
prints contents and puts newline between the two outputs

>tac reads file from the opposite end
---
## Copying Files
cp *OPTIONS* SOURCE_DESTINATION
- f a copy of a file is created before changes are made, then it is possible to revert back to the original.
- A copy of a file can be used to transfer a file to removable media devices.
- A copy of an existing document can be used as a template for a new document.

The `dd` command is a utility for copying files or entire partitions at the bit level.
dd *OPTIONS* OPERARND
- It can be used to clone or delete (wipe) entire disks or partitions.
- It can be used to copy raw data to removable devices, such as USB drives and CDROMs.
- It can backup and restore the MBR (Master Boot Record).
- It can be used to create a file of a specific size that is filled with binary zeros, which can then be used as a swap file (virtual memory).

Let's examine the following example. The `dd` command creates a file named `/tmp/swapex` with 50 blocks of zeros that are one megabyte in size:
*dd if=/dev/zero of=/tmp/swapex bs=1M count=50*

![[Pasted image 20230718213538.png]]

---
## Removing Files

rm *OPTIONS* FILE

The `rm` command will ignore directories that it's asked to remove; to delete a directory, use a recursive option, either the `-r` or `-R` options. Just be careful since these options are "recursive", this will delete all files and all subdirectories.

rmdir * (asterisk is all). Removes all directories.


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
grep -i (ignore) ignores case sensitivity
grep -v (--invert-match) selects non-matching lines


history | grep "mkdir -p" (finds past commands that include the specified string)
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
<br>
ifconfig *OPTIONS*
<br>
>**Note**
The `iwconfig` command is similar to the `ifconfig` command, but it is dedicated to wireless network interfaces.
<br>
![[Pasted image 20230718221142.png]]
<br>
>**Consider This**
The `lo` device is referred to as the loopback device. It is a special network device used by the system when sending network-based data to itself.
<br>
![[Pasted image 20230718221243.png]]
<br>
![[Pasted image 20230718221257.png]]

---
## Viewing Processes

Running a command results in something called a process. In the Linux operating system, processes are executed with the privileges of the user who executes the command. This allows for processes to be limited to certain capabilities based upon the user identity.
<br>
Although there are exceptions, generally the operating system will differentiate users based upon whether they are the administrator. Typically regular users, like the `sysadmin` user, cannot control another user's processes. Users who have administrative privileges, like the `root` account, can control any user processes, including stopping any user process.
<br>
>The `ps` command can be used to list processes.
ps *OPTIONS*
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
<br>
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

At the lowest level of the Debian package management system is the `dpkg` command. This command can be tricky for novice Linux users, so the Advanced Package Tool, **`apt-get`**, a front-end program to the `dpkg` tool, makes management of packages even easier.

### Installing Packages
Package files are commonly installed by downloading them directly from repositories located on Internet servers. The Debian repositories contain more than 65,000 different packages of software. Before installing a package, it is good practice to refresh the list of available packages using the **`apt-get update`** command.
<br>
*sudo apt-get update*
>**sysadmin@localhost:~$** sudo apt-get update                                       
[sudo] password for sysadmin:                                                   
Ign file: amd64/ InRelease                                                      
Ign file: amd64/ Release.gpg                                                    
Ign file: amd64/ Release                                                        
Reading package lists... Done
<Br>
To search for keywords within these packages, you can use the `apt-cache search` command.

apt-cache search *keyword*
<br>
Once you've found the package that you want to install, you can install it with the `apt-get install` command:

*sudo apt-get install (PACKAGE)*
![[Pasted image 20230718221953.png]]
<br>
### Updating packages
The **`apt-get install`** command can also update a package, if that package is installed and a newer version is available. If the package is not already on the system, it would be installed; if it is on the system, it would be updated.
<br>
Updating all packages of the system should be done in two steps. First, update the cache of all packages available with **`apt-get update`**. Second, execute the **`apt-get upgrade`** command and all packages and dependencies will be updated.
![[Pasted image 20230718222059.png]]
<br>
### Removing Packages
The `apt-get` command is able to either remove or purge a package. The difference between the two is that purging deletes all package files, while removing deletes all but the configuration files for the package.

An administrator can execute the **`apt-get remove`** command to remove a package or the **`apt-get purge`** command to purge a package completely from the system.

>apt-get remove [package]

>apt-get purge [package]

---
## Updating User Passwords
The **`passwd`** command is used to update a user’s password. Users can only change their own passwords, whereas the root user can update the password for any user.

>passwd [OPTIONS [USER]

<br>
For example, since we are logged in as the *`sysadmin`* user we can change the password for that account. Execute the **`passwd`** command. You will be prompted to enter the existing password once and the new password twice. For security reasons, no output is displayed while the password is being typed. The output is shown as follows:
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

>**sysadmin@localhost:~/Documents$** cat food.txt > newfile1.txt
**sysadmin@localhost:~/Documents$**
This is useful if you need to copy content from an important file to another file in order to edit the contents without modifying the original file.

---
## Text Editor
- The `vi` editor is available on every Linux distribution in the world. This is not true of any other editor.
    
- The `vi` editor can be executed both in a CLI (command line interface) and a GUI (graphical user interface).
<br>
There are three modes used in `vi`: command mode, insert mode, and ex mode.
<br>

### Command Mode Movement
Initially, the program starts in command mode. Command mode is used to type commands, such as those used to move around a document, manipulate text, and access the other two modes. To return to command mode at any time, press the **Esc** key.

Once some text has been added into a document, to perform actions like moving the cursor, the **Esc** key needs to be pressed first to return to command mode. This seems like a lot of work, but remember that `vi` works in a terminal environment where a mouse is useless.
<br>
Movement commands in `vi` have two aspects, a motion and an optional number prefix, which indicates how many times to repeat that motion. The general format is as follows:

>[count] motion
![[Pasted image 20230718223534.png]]
**Note**
Since the upgrade to `vim` it is also possible to use the arrow keys `←``↓``↑``→` instead of `h``j``k``l` respectively.

<br>
To move the cursor to a specific line number, type that line number followed by the `G` character. For example, to get to the fifth line of the file type `5G`. `1G` or `gg` can be used to go to the first line of the file, while a lone `G` will take you to the last line. To find out which line the cursor is currently on, use **CTRL+G**.
<br>
### Command Mode Actions
The standard convention for editing content with word processors is to use copy, cut, and paste. The `vi` program has none of these. Instead, `vi` uses the following three commands:
![[Pasted image 20230718223759.png]]
The motions learned from the previous page are used to specify where the action is to take place, always beginning with the present cursor location. Either of the following general formats for action commands is acceptable:

>action [count] motion

>[count] action motion

<br>
### Delete
Delete removes the indicated text from the page and saves it into the buffer, the buffer being the equivalent of the "clipboard" used in Windows or Mac OSX. The following table provides some common usage examples:
![[Pasted image 20230718223905.png]]
<br>
### Change
Change is very similar to delete; the text is removed and saved into the buffer, however, the program is switched to insert mode to allow immediate changes to the text. The following table provides some common usage examples:
![[Pasted image 20230718223953.png]]
<br>
### Yank
Yank places content into the buffer without deleting it. The following table provides some common usage examples:
![[Pasted image 20230718224035.png]]
<br>
### Put
Put places the text saved in the buffer either before or after the cursor position. Notice that these are the only two options, put does not use the motions like the previous action commands.
![[Pasted image 20230718224053.png]]
<br>
### Searching in vi
Another standard function that word processors offer is find. Often, people use **CTRL+F** or look under the edit menu. The `vi` program uses search. Search is more powerful than find because it supports both literal text patterns and regular expressions.

To search forward from the current position of the cursor, use the `/` to start the search, type a search term, and then press the **Enter** key to begin the search. The cursor will move to the first match that is found.

To proceed to the next match using the same pattern, press the `n` key. To go back to a previous match, press the `N` key. If the end or the beginning of the document is reached, the search will automatically wrap around to the other side of the document.
<br>
To start searching backwards from the cursor position, start by typing `?`, then type the pattern to search for matches and press the **Enter** key.
<br>
### Insert Mode
Insert mode is used to add text to the document. There a few ways to enter insert mode from command mode, each differentiated by where the text insertion will begin. The following table covers the most common:
![[Pasted image 20230718224240.png]]
<br>
### Ex Mode
When the ex mode of the `vi` editor is being used, it is possible to view or change settings, as well as carry out file-related commands like opening, saving or aborting changes to a file. In order to get to the ex mode, type a `:` character in command mode. The following table lists some common actions performed in ex mode:
![[Pasted image 20230718224412.png]]
A quick analysis of the table above reveals that if an exclamation mark, `!`, is added to a command, it then attempts to force the operation. For example, imagine you make changes to a file in the `vi` editor and then try to quit with `:q`, only to discover that the command fails. The `vi` editor doesn't want to quit without saving the changes you made to a file, but you can force it to quit with the ex command `:q!`.
<br>
>**Consider This**
Although the ex mode offers several ways to save and quit, there's also `ZZ` that is available in command mode; this is the equivalent of `:wq`. There are many more overlapping functions between ex mode and command mode. For example, ex mode can be used to navigate to any line in the document by typing `:` followed by the line number, while the `G` can be used in command mode as previously demonstrated.

---

## Wildcards - power of ? and *
rm * - removes all files in directory.
rm month/* - removes all files in month directory.

touch file{3..5}.txt - creates files file3.txt, file4.txt and file5.txt

touch file{1..10..2}.txt - creates files with only odd numbers in the name.

ls -l * .sh - lists all files that have a .sh format

find . -type f -name "f*"

ls -l * e * - finds all files with the letter e in them

ls -l ? - the question mark is substituted with only one letter, shows all files that only have one letter in the name. f.txt does not count

rm alpha* (removes all files that start with the word alpha in the beginning)

When using a ? as a wildcard, it does not match up with words that dont have any letters to fill out the ?


---
## File permissions

Read - r=4
Write - w=2
Execute - e=1

If we want to give only read and write permissions, we can add 6 (4+2).

chmod 751 aa.txt

which means, we gave the USER 7 permission points, meaning rwe
we gave the group read and execute permissions, 5 permission points as read is 4 and execute is 1
and for others we only gave execute permissions because we only gave the third digit only 1 permission points, which is execute

---
## mkdir essentials

mkdir {dir1,dir2} Makes two directories with the names of dir1 and dir2
mkdir dir1 dir2 Also works the same way

mkdir dir dir/dd dir/cc Makes a new folder with new subfolders inside it.

mkdir dir/dd dir/cc wouldnt work, throws exception that dir does not exist.

mkdir -p dir/dd dir/cc does work. 

mkdir -p zoo/{predatory/{table,leopard}/,birds/{parrot,chair}}

mkdir -p grocery/{bakery/cakes/{minirolls,bars}/,home/cleaning/{wipes,polish}}
![[Pasted image 20230723141548.png]]


---
# The find command

https://www.baeldung.com/linux/find-files-lacking-permissions
find . -type d (only shows the type, d is for directory)

find . -type d -empty

find zoo/
find zoo/ -type f

To find all non-empty files in the same directory, simply add ! before -size 0: 
$ find -L /home/peter -maxdepth 1  -type f ! -size 0

find . -empty (looks for empty files)

$ find . -type f -empty -print -delete (looks for empty files, prints them and deletes them in one go)

 [Copy the content/file to all subdirectory in a directory using terminal](https://askubuntu.com/questions/300744/copy-the-content-file-to-all-subdirectory-in-a-directory-using-terminal)
`find <target-dir> -type d -exec cp <the file> {} \;`


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
$ awk '{print $1,$4}' employee.txt (prints first and fourth field in every line in file)

https://exercism.org/tracks/awk


---
# File compression
gzip 
zcat lets us read compressed files

---
double tab while doing cd ../ will show us directories that are in the back directory


CTRL+a goes back to the beginning of the row 
CTRL+e goes back to the end of the row


echo "" | cat file.txt - kovitz.txt (The - is standard input, first is cats the file.txt, waits for standard input which is the "" that we entered and then goes on to display the kovitz.txt)


uptime - shows the uptime of the machine
uptime --help 


whoami
Prints out the name of the user. 


history displays all commands that were entered in the console.


who | tee who_output.txt (prints and saves in txt file in one go)


gedit opens the text file in an actual notepad 


hello (first field) lmao (second field) 
Each word is a field, spaces 

mv {Croatia,Wales}/* Poland/ (moves all the files from croatia and wales directories into the poland directory)

touch Croatia/{abc,file.txt,file.doc} (touches 3 different files at once)



mv {Croatia,Wales}/{\*.txt, \*.doc} Poland/ (moves all the files from croatia and wales directories into the poland directory)

---
# Basic Linux Keystrokes

Esc: Escaping out of editing mode - get out of any of the pressed keys

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
if <code>ifconfig</code> does not work, we could use <code>ip addr</code>
or we can install net-tools and then run <code>ifconfig</code>

---
## Command prompt
Short text that sits at the start of the command line.
![[Pasted image 20230731112921.png]]
To get your prompt back: *CTRL + C*. If you get stuck, you can press *CTRL + C* to get the prompt back and are able to enter new commands again. 

---
## File system structure and its description
Files used for the bootloader, every time our machine boots up, it will
go to the /boot folder and looks into it. 
/root root user home directory. Not the same as /
/dev System devices (keyboards, speakers, etc.)
/etc config files. If we have any apps on the system, all of their config files reside in the /etc folder. Remember to do a backup to the config file before modifying it.
/bin -> /usr/bin every day user commands
/sbin -> /usr/sbin System/filesystem commands
/opt optional add-on applications, apps that do not come with the OS.
/proc Running processes (only exist in Memory)
/lib -> /usr/lib C programming library files needed by commands and apps
strace -e open pwd to
/tmp stores temporary files. 
/home for regular users. 
/var System logs
/run stores temporary runtime files.
/mnt To mount external filesystem. 
/media For cd-rom medias. if we use a cd drive it will appear there.
![[Pasted image 20230731115246.png]]

---
## Navigating File System
<code>cd</code> - stands for change directory
<code>pwd</code> - stands for print working directory
<code>ls</code> - stands for list

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
Command is: <code>passwd userid</code>
Old password: enter your old password 
New password: enter the desired password
Retype new password: retype the new password

>Only root can modify passwords.

---


If we want to make a script, 
the first line should say <code>#! /bin/bash</code> which tells the system to run the code using the bash interpreter.

---
## Creating files and Directories
touch
cp
vi

### Creating Directories
mkdir

ls -ltr
Shows files from last to latest created

---
cp -R copies all files and subfolders inside a directory

---
## Find files and directories
Two main commands to find files/directories:
 >find
 
 >locate

find . (current directory) -name "filename"
locate ""

find / -name "ifcfg-enp0s3(filename)" *RUN AS SUDO*

### Difference between find and locate commands
<code>locate</code> is much faster because it looks for specific files that are cached. locate uses a prebuilt database.

To update locate database run <code>updatedb</code>

<code>find</code> runs over all the directories in real time thus taking more time and compute power.

---
## Wild cards

A character that can be used as a substitute of a class of characters in a search

\* - represents zero or more characters.
\? - represents a single character.
\[] - represents a range of characters.

<code>touch file{1..9}.txt</code> creates 9 files, from 1 to 9 in one go. So file1.txt, file2.txt on and on until file9.txt

![[Pasted image 20230731152419.png]]


---
## Soft and Hard links
Every time you create a file, the operating system gives said file a number. The number is called an *inode*. Pointer or number of a file on the hard disk

Soft Link = link will be removed if file is removed or renamed.

Hard Link = Deleting or renaming or moving the original file, will not affect the hard link

![[Pasted image 20230731155126.png]]

![[Pasted image 20230731155305.png]]

<code>ls -i</code> shows the inode numbers of the files/directories.

![[Pasted image 20230731160021.png]]

---
https://www.makeuseof.com/linux-command-line-chaining-operators/


su demo 
whoami -> demo
pwd -> /home/anan
exit
whoami -> anan
su - demo
whoami -> demo
pwd -> /home/demo

---
man ls
ls manual

## File permissions with numeric values
![[Pasted image 20230801093707.png]]


## File ownership commands
![[Pasted image 20230801100101.png]]

---
## ACL
![[Pasted image 20230801100303.png]]
To add permission for user
setfacl -m u:user:rwx /path/to/file

add permissions for a group
setfacl -m g:group:rw /path/to/file

to allow all files or directories to inherit ACL entries from the directory it is within
setfacl -Rm "entry" /path/to/file

remove a specific entry
setfacl -x u:user /path/

to remove all entries -b /path/

getfacl /path 
shows all accesses to groups and users

---
## Help commands
*what is* command
command *--help*
*man* command (manual)

---
## Adding text to files

### 3 simple ways:
vi
Redirect command output > or >>
echo > or >>

---
## Input and output redirects
3 Redirects in Linux
1. Standard input
2. Standard output
3. Standard error

-- Output (stdout)

---
## Standard output to a File (tee)

"tee" command is used to store and view (at the same time) the output of any command

Named after the T-splitter used in plumbing. Both displays and saves into a file. Simultaneously.

<code>echo "David Puddy is Elaine's boyfriend"</code>
<code>echo "David Puddy is Elaine's boyfriend" > elaine-david</code>
Does not throw the output to the screen.

<code>echo "David Puddy is Elaine's boyfriend" | tee elaine-david</code>
Does throw the output to the screen while also saving it to the elaine-david file.
The tee commands overrides the contents of a file by default.

<code>echo "David Puddy is Elaine's boyfriend" | tee -a elaine-david</code>
By using the *-a* option, it appends the input instead of having it override the current content of a file.

---
## Pipes
Used by the shell to connect the output of one command directly to the input of another command.

<code>ls -ltr | more</code> piping our output into the more command, which shows content one page at a time when there is too many results showing on the page.

---
## File Maintenance Commands
1. cp
2. rm
3. mv
4. mkdir
5. rmdir or rm -r
6. chgrp
7. chown

<code>rm -Rf</code> will forcefully remove sub-directories and their contents as well.

---
## File display commands
- cat
- more
- less
- head
- tail

---
## Filters / Text processors commands
- cut
- awk
- grep and egrep
- sort
- uniq
- wc
---
## Cut
Allows you to cut parts of lines from specified files.

- cut filename = does not work
- cut --version = check version
- cut -cl filename = list one character
- cut -c1,2,4 = pick and choose character
- cut -c1-3,6-8 filename = list range of characters
- cut -b1-3 filename = list by byte size
- cut -d: -f 6 /etc/passwd = list the first 6th column separated by ":"
- cut -d: -f 6-7 /etc/passwd = list the first 6 and 7th columns separated by ":"

---
## AWK
Utility/language designed for data extraction. Used for files or from an ouitput

- awk --version = check version
- awk '{print $1}' file = shows only the first field from a file
- ls -l | awk '{print $1,$3}' = list the first and third columns from ls -l
- ls -l | awk '{print $NF}' = last field of the output
- awk '/Jerry/ {print}' file = search for a specific word
- awk -F: '{print $1}' /etc/passwd = output only the first field of /etc/passwd
- echo "Hello Tom" | awk '{$2="Adam" ; print $0}' = replace words field words
- cat file | awk '{$2="Imran" ; print $0} = replace words field words
- awk 'length($0) > 15' filename = displays all lines that have a length greater than 15
- ls -l | awk '{if($9 == "seinfeld") print $0;}' = 
- ls -l | awk '{print NF}' = 

https://www.ibm.com/docs/zh/aix/7.2?topic=awk-command
https://www.cs.unibo.it/~renzo/doc/awk/nawkA4.pdf

---
## grep/egrep
Stands for "global regular expression print", processes line by line and prints any lines that match a specified pattern.

- grep --version OR grep --help
- grep keyword file = looks for the word in the file
- grep -c keyword file = counts words that match the pattern
- grep -i keyword file = ignores case sensitivity 
- grep -n keyword file = display the matched lines and their matched word
- grep -v keyword file = shows lines that DO NOT contain the word
- grep keyword file | awk '{print $1}' = search for a keyword and only give the first field
- ls -l | grep Desktop 
- egrep -i "keyword|keyword2" file = look for fields that contain either the first keyword or the second keyword
https://www.gnu.org/software/grep/manual/html_node/Character-Classes-and-Bracket-Expressions.html

---
## Sort and uniq commands

1. Sort command sorts in alphabetical 
2. Uniq commands filters out

commands:
- sort --version OR sort --help
- sort file = sorts the file alphabetically
- sort -r file = sort in reverse alphabetical order
- sort -k2 file = sort by the second column 

- uniq file = remove duplicates
- sort file | uniq = sort first then uniq
- sort file | uniq -e = sort first and then uniq, while showing the amount of duplicates
- sort file | uniq -d = only shows repeated lines
---
## wc
The command reads either standard input or from a list of files and generates 

- wc --version OR wc --help
- wc file = check file line count, word count and byte count
- wc -l file = get the number of lines in a file
- wc -w file = get the number of words in a file
- wc -b file = get the number of byes in a file
- wc -c file = counts characters in file
- wc DIRECTORY = NOT ALLOWED
- ls -l | wc -l = runs ls first and then counts how many lines there are, counts the amount of folders. Keep in mind that it also counts the total row so we should count minus 1 from the output we get from the wc. Number of files
- grep keyword | wc -l = looks for a word in a file and then counts how many lines there are that matched. Number of keyword lines.

---
## Compare 

- diff = compares line by line
- cmp = compares byte by byte

---
## Compress and decompress files

- tar = zips files together
- gzip = compresses a file
- gzip -d OR gunzip = decompresses a file

tar cvf . = copy everything 
tar xvf . = extract everything 

https://www.freecodecamp.org/news/tar-command-linux-tar-cvf-tar-xvf/

---
## Truncating file size (truncate)
Used to shrink of extend the size of a file to the specified size
Will actually chop the file and **lose** the content of the file. 

- truncate -s 10 filename = shrinks the file to 10 bytes

Can be used to make the file bigger as well. Adds empty letters to fill up the file and make it bigger. Looks something like "^@^@^@^@^@^@".

---
## Combining and splitting files
- Multiple files can be combined into one 
- One file can be split into multiple files

- cat file1 file2 file3 > file4
- split file4

for example: <code>split -l 300 file.txt childfile.txt</code> = Split file.txt into 300 line per file and output to chidlfileaa childfileab childfileac

---
## Linux vs Windows commands
![[Pasted image 20230801122841.png]]

---

## tr
The **tr** command is a UNIX command-line utility for translating or deleting characters. It supports a range of transformations including uppercase to lowercase, squeezing repeating characters, deleting specific characters, and basic find and replace. It can be used with UNIX pipes to support more complex translation. **tr stands for translate.**

\[:upper:\], \[:lower:\], \[:alnum:\] are called character classes.
https://www.gnu.org/software/grep/manual/html_node/Character-Classes-and-Bracket-Expressions.html

echo "Hello hello World world" | tr \[:upper:\] \[:lower\]
translates all upper case characters to lowercase characters
output: hello hello world world

echo "Hello hello World world" | tr \[:lower:\] \[:upper\]
output: HELLO HELLO WORLD WORLD


alnum: numbers and letters
echo "Hello hello World world" | tr \[:upper:\] \[:lower\] | tr '\[:alnum\]' 'n'
substitutes all alphanumerical characters into the letter n.
output: nnnnn nnnnn nnnnn nnnnn

Instead, we want to enter a new line. And instead of substituting the words that we want to count, we need to substitute the non alphanumerical spaces into new lines. 

echo "Hello hello World world" | tr \[:upper:\] \[:lower\] | tr -c '\[:alnum\]' '\\n'
-c is the compliment. 

![[Pasted image 20230803095145.png]]

But that results in unnecessary new lines. 

echo "Hello hello World world" | tr \[:upper:\] \[:lower\] | tr -sc '\[:alnum\]' '\\n'
-s is for squeeze   .
![[Pasted image 20230803095703.png]]


![[Pasted image 20230803100716.png]]
curl -s
-s is for silent mode

![[Pasted image 20230803101514.png]]
-c in uniq is for count

---
 ## User Account Management
- useradd
- groupadd
- userdel
- groupdel
- usermod - modify a user

Files:
- /etc/passwd
- /etc/group
- /etc/shadow


id username to verify that we created user

cat /etc/group to verify that the new group was created

automatically adds spiderman to spiderman group when creating useradd spiderman

-m to create home directory for the user

---
## Password Aging - chage
chage \[-m min days\] \[-M max days\] \[-d last day\] \[-I inactive\] \[-E expire date\] \[-W warn days\] user

File = /etc/login.defs
- PASS_MAX_DAYS 99999
- PASS_MIN_DAYS 0
- PASS_MIN_LEN 5
- PASS_WARM_AGE 7

![[Pasted image 20230803115633.png]]

---
## Switch Users and sudo Access

#### Commands:
- su - username
- sudo command
- visudo - /etc/sudoers - used to configure user permissions

%wheel allows people in group wheel to run all commands

usermod -aG wheel anan 
adds user anan to the wheel group that has all permissions to run all commands

---
## Monitor Users
- `who` - how many people are logged in, user ID, terminal ID and how long have they been logged in.
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
![[Pasted image 20230806194938.png]]
Windows = Microsoft Active Directory





---
## Process management
Background =Ctrl + z, runs in the bg
Foreground = fg 
Run process even after exit = nohup process &
	OR = nohup process > /dev/null 2>&1 &
Kill a process by name = pkill
Process priority = nice (nice -n 5 process)
	Goes from -20 to 19. The lower the number the more priority a task gets
Process monitoring = top
List process = ps

Every time we run a process, it attaches itself to that terminal. Closing the terminal will stop the process.
There is a workaround that lets us run commands with no regards to whether the terminal is running or has been terminated: we use `nohup`.

`nice -n (set priority)`
`nice -n 5 sleep 10`
This gives the sleep command a priority of 5.

---
## System Monitoring

- top - lists all processes running, similar to task manager on windows.
- df - report file system space usage. `df -h` makes the output more human readable. 
- du - estimate file space usage 
- dmesg - Show
- iostat - input output statistics
- netstat - prints network connection, all things internet connectivity
- free - displays the amount of free and used memory in the system
- cat \/proc/cpuinfo - proc stores info about the system cpu
- cat \/proc/meminfo - shows us information about the system memory
---
## Log Monitoring
Log Directory = /var/log - Directory that stores all the logs
ll -more /var/log 
We get a comprehensive list of all logs
more boot log - gives us all boot logs, errors and or checks
rebooting will generate a new boot file
- boot - booting up logs
- chronyd = NTP - 
- cron - daemon to execute scheduled commands.
- maillog - all information about our emails
- secure - records all logging in and log out information. 
- messages - every time there is an issue with our machine, we usually go to the messages log. Has all kinds of information, app information, processes information, system information etc.
  What is going on with our system, what failed and when it failed.
- httpd 

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
- `uname -a` - tells us date and time, hostname, Linux kernel and all kinds of information about the machine
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

---
## Special Permissions with `setuid`, `setgid` and `sticky bit`

`setuid` tells linux to run a pprogram with the effectivbe user id of the owner instead of the executor

setgid tells linux to run a program with the effective group id of the owner instead of the executor 

sticky bit is a bit set on files/directories that allows only the owner or root to delete the files

- to assign special permissions at the user level:
  chmod u+s xys.sh
- to assign special permissions at the group level:
  chmod g+s xyz.sh
- To remove special permissions at the user or group level:
	  chmod u-s xyz.sh
	  chmod g-s xyz.sh

<mark style="background: #FF5582A6;">To find all executables in Linux with `setuid` and `setgid`
find / -perm /6000 -type f</mark>

Note: Only works on .exe files (files that are written in C or CPP)(?)

>Note: 2000/4000/6000 are incomplete permissions, so you should replace 000 with the appropriate permissions, e.g. 4755.

https://www.sobyte.net/post/2022-04/linux-suid/

`Sticky bit`
- It is assigned to the last bit of permission
  \-r w x  r w x  r w <mark style="background: #FFB86CA6;">t</mark>
  The highlighted bit is the sticky bit, Why?
  If we have a t, it means that although the user has read write permissions, he cannot delete the file.

become root and create dir mkdir \/allinone
assign all rwx to the dir chmod 777 \/allinone
become user and create dir inside of \/allineone: mkdir imrandir
give all rwx perms to the dir: chmod 777 imrandir
create 3 files in that dir: touch a b c
Logging as another user and trying to delete the imrandir directory will result in deleting it.

Now, becoming root and assigning sticky bit permission to \/allinone dir: `chmod +t /allinone`

Become user and create a dir inside of \/allinone
Give all rwx perms to that dir
Create 3 files in that dir: touch a b c
Become another user again and try to delete that dir
We wont be able to delete the directory.

<mark style="background: #FF5582A6;">When we see a capital letter T as the sticky bit then it means that the others do not have an execute permission.</mark>

---
## Aliases
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

lo = loopback device, special interface that the machine uses to communicate with itself. Used for diagnostics and troubleshooting and to connect to servers running on the local machine.

virb0 = "Virtual Bridge 0" used for NAT (Network Address Translation). Virtual environments sometimes use it to connect to outside networks.

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
## Download Files or Apps

`wget "insertlink"`

If a certain app does not exist in the default repository 


