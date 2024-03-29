### Linux Command Line Exploration Mission

https://www.man7.org/linux/man-pages/man1/echo.1.html

https://www.geeksforgeeks.org/man-command-in-linux-with-examples/

1. Use the `echo` command to display a message without a newline.
	- `echo -n no-new-line`
2. Search for a keyword related to networking using the `man` command.
	- `man ip`
3. Display a specific manual page for a built-in shell command using the `help` command.
	- `help echo`
4. Display the full description of the `pwd` command using the `whatis` command.
	```BASH
	anan1337@localhost:~> whatis pwd
	bash_builtins (1)    - bash built-in commands, see bash(1)
	pwd (n)              - Return the absolute path of the current working directory
	```
---
https://linuxhandbook.com/symbolic-link-linux/
https://linuxhandbook.com/linux-alias-command/
### Navigation and File Management:
1. Display the physical current working directory using the `pwd` command.
	 ![[Pasted image 20240317141342.png]]
2. Force symbolic links to be followed when changing directories using the `cd` command.
	- ?
3. List all files and directories, including hidden ones, with detailed information using the `ls` command.
	- `ls -la`
4. Prevent creating a new file if it already exists using the `touch` command.
	- `touch -c file`
5. Display the first 5 lines of the `file.txt` file using the `head` command.
	- `head -n 5 file.txt`
6. Display the last 10 lines of the `file.txt` file using the `tail` command.
	- `tail -n 10 file.txt`
---
### File System Navigation:
1. Recursively list all files and directories in the current directory and its subdirectories using the `ls` command.
	- `ls -R`
2. Change to a directory that starts with a hyphen using the `cd` command.
	- `mkdir ./-hyphen`
	- `cd ./-hyphen/`
3. List files and directories by modification time, newest first, using the `ls` command.
	- `ls -lt`
---
### File System Management:
1. Recursively copy a directory and its contents using the `cp` command.
	- `cp -r Dir1 Dir1Copy`
2. Interactively move a file, prompting before overwriting, using the `mv` command.
	- `mv -i file.txt /home/anan1337/Dir1/file.txt`
	- If the file already exists, the terminal is going to ask if i want to replace the already existing file.txt inside Dir1.
3. Create parent directories if they don't exist using the `mkdir` command.
	- `mkdir -p /home/anan1337/newDir/thisDirDoesntExist/anotherNewDir`
4. Forcefully remove a directory and its contents using the `rm` command.
	- `rm -rf directory`
---
### Command History and Clearing:

1. Clear the command history using the `history` command.
	- `history clear`
2. Clear the terminal screen using the `clear` command.
	- `clear`
---
### File and Directory Permissions:
1. Display the size of each file in blocks using the `ls` command.
	- `ls -lba`
2. Add execute permission to the owner of a file using the `chmod` command.
	- `chmod o+x`
3. Set the owner and group of a file to match another file using the `chown` command.
	- `chwon --reference=file2.txt file1.txt`
---
### Alias and Unalias:

1. Display a list of currently defined aliases using the `alias` command.
```
anan1337@localhost:~> alias
alias +='pushd .'
alias -- -='popd'
alias ..='cd ..'
alias ...='cd ../..'
alias beep='echo -en "\007"'
alias cd..='cd ..'
alias dir='ls -l'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias ip='ip --color=auto'
alias l='ls -alF'
alias la='ls -la'
alias ll='ls -l'
alias ls='_ls'
alias ls-l='ls -l'
alias md='mkdir -p'
alias o='less'
alias rd='rmdir'
alias rehash='hash -r'
alias unmount='echo "Error: Try the command: umount" 1>&2; false'
alias you='if test "$EUID" = 0 ; then /sbin/yast2 online_update ; else su - -c "/sbin/yast2 online_update" ; fi'
```
2. Remove all aliases using the `unalias` command.
	- `unalias -a`
	- Does not affect aliases defined in your shell's configuration files (like `.bashrc` or `.zshrc`), so they will reappear in new shell sessions unless you remove or comment them out in those files.
---
### Exiting and Logging Out:

1. Exit the shell without saving the command history using the `exit` command.
	- `unset HISTFILE && exit`
2. Force logout, even if processes are running, using the `logout` command.
	- `killall -u anan1337`