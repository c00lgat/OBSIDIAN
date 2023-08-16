https://drive.google.com/file/d/1bACHL-ctwFJpXpVNRrTUCI1m_IsnLIFb/view?usp=sharing
File created by Yaniv Hadar

A bash script file is always started with a Shebang. 
`#! /bin/bash` 
This line tells the shell to read the code using the bash interpreter. As we know, there are multiple shells out there. Bash comes preinstalled on all Linux distributions. 

How do we run a script?
First, we need to give the script we just wrote execution permissions:
- `chmod +x script.sh`
Then we run the script in the terminal via:
- `./script.sh`

We can pass arguments to our little, precious bash script in two ways:
- By prompting the user. Example:
	`read -p "Please enter argument" argument `
- Second way is by using external arguments. Also called command line arguments. Basically, instead of explicitly asking the user to enter arguments as seen above, we use the `$1, $2` and etc notation. For example:
	`./script.sh firstArgument 