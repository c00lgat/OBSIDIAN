**Agenda**:
- CLI
- Shell
- Bash
- Common commands

*What is the CLI?*
CLI stands for Command-Line interface. It is a text-based interface used to interact with a computer or software by typing commands.

The CLI lets us communicate with our system through commands.
As opposed to GUI based applications, where there is a user interface that gets most of the work done with a click of a button.

The shell is a program that provides an interface for users to interact with the operating system's services. 
It acts as a command interpreter, taking commands from the user via the CLI and executing them. Essentially, the shell is the environment in which the CLI operates. 

*BASH*
Bash, short for "Bourse Again Shell", is a popular shell and command language interpreter for Unix-like operating systems, including Linux and macOS. It is the default shell for most Linux distributions and provides a command-line interface (CLI) for users to interact with the operating systems.

*Common commands*
- echo
- man
- help
- whatis
- pwd
- cd (., .., ~, -)
- ls
- touch
- head
- tail
- cat
- less
- file
- history and pipe
- clear
- cp
	- Wildcards: \*, \[], ?
- mv (also used for renaming)
- mkdir (-p)
- rm (-f, -r)
- where (where python3)
- alias
	- alias c=clear
- unalias
	- Removes a specific alias
- exit
- logout

###### Exit codes
*Exit code 0*: all good.
*Exit code anything other than 0*: no good. The code did not execute properly. *127* means command *not found*.

*echo $?*: Prints the exit code of the last command


Tests/4_bash_script_test
Submit into submissions.
mkdir into submissions, dir should be my name/4_linux/scriptname.sh
Submission/AnanAbed/4_linux/script.sh