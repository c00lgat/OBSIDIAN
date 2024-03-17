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

Navigation and File Management:

1. Display the physical current working directory using the `pwd` command.
2. Force symbolic links to be followed when changing directories using the `cd` command.
3. List all files and directories, including hidden ones, with detailed information using the `ls` command.
4. Prevent creating a new file if it already exists using the `touch` command.
5. Display the first 5 lines of the `file.txt` file using the `head` command.
6. Display the last 10 lines of the `file.txt` file using the `tail` command.

File System Navigation:

1. Recursively list all files and directories in the current directory and its subdirectories using the `ls` command.
2. Change to a directory that starts with a hyphen using the `cd` command.
3. List files and directories by modification time, newest first, using the `ls` command.

File System Management:

1. Recursively copy a directory and its contents using the `cp` command.
2. Interactively move a file, prompting before overwriting, using the `mv` command.
3. Create parent directories if they don't exist using the `mkdir` command.
4. Forcefully remove a directory and its contents using the `rm` command.

Command History and Clearing:

1. Clear the command history using the `history` command.
2. Clear the terminal screen using the `clear` command.

File and Directory Permissions:

1. Display the size of each file in blocks using the `ls` command.
2. Add execute permission to the owner of a file using the `chmod` command.
3. Set the owner and group of a file to match another file using the `chown` command.

Alias and Unalias:

1. Display a list of currently defined aliases using the `alias` command.
2. Remove all aliases using the `unalias` command.

Exiting and Logging Out:

1. Exit the shell without saving the command history using the `exit` command.
2. Force logout, even if processes are running, using the `logout` command.