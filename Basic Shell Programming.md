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
	`./script.sh firstArgument secondArgument`
	And then inside the script, we call these external arguments via the dollar sign and then a number that represents the number of the argument. `firstArgument` is notated as `$1` inside our code.

### Decision:
- In our bash scripts, we sometimes have to decide between two or more options/things.
- Example: We decide to print the number if its divided by 2. If so, print. If not, do not print. In this case we use an `if-then-else` statement.
	Other cases/examples include using the `case` statement.

### Repetition:
- `do-while, repeat-until`
	The `repeat` and `while` are very similar to each other. The `while` loop allows us to repeat code for *as long as a certain **statement stands*.**
		Whereas the  `until` loop works counterclockwise. The `until` loops allows us to run code for *as long as a certain statement **does not stand.*** 

- `for`
	The for loop allows us to run and repeat code according to the amount of times we tell it to run. 
	For example, we can tell for to run and iterate over and over on code until `i` hits 10, for example. 
	
	The `for` in bash is quite smart. We can also ask it to iterate over all the files that are currently present in the same directory, until we run out of files to check/iterate over. It does that automatically, we just have to tell it to iterate over the current directory (`for i in  *`)
	
	`for` can also run on a list of names