- Linux comprehensive book for beginners [https://tldp.org/LDP/Bash-Beginners-Guide/Bash-Beginners-Guide.pdf](https://tldp.org/LDP/Bash-Beginners-Guide/Bash-Beginners-Guide.pdf)
- Advanced Linux and Bash scripting [https://tldp.org/LDP/abs/abs-guide.pdf](https://tldp.org/LDP/abs/abs-guide.pdf)

Bash, or the Bourne-Again Shell, is a widely-used Unix shell and command language that provides a powerful command-line interface for interacting with the operating system.

Learning Bash can help you:
- Make life easier on UNIX or UNIX-like system
- Ease execution of daily tasks
- Automate important operation task

Overall, learning Bash can help you to become a more efficient and effective system administrator, developer, or data analyst.

The UNIX shell program interprets user commands to the kernel, which are either directly entered by the user, or which can be read from a file called the **shell script**. Apart from passing commands to the kernel, the main task of a shell is providing a **user environment**, which can be configured individually using shell resource configuration files.

The below example shows the evolution bash program. It starts simply by grouping a few commands into a file, without any error handling and flow control... until the form of a well written professional script.

### From Bash commands to Bash program
Consider the below script to clean up log files (messages, wtmp) in /var/log. Copy and execute the following snippet to a .sh file in your local Linux machine.

