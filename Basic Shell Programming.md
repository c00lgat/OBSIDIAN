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

### Input:
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
	For example, we can tell for to run and iterate over and over on code until `i` hits 10, for example. `for i in {1..10}` Or `for (( i=0; i<5; i++ ))`
	
	The `for` in bash is quite smart. We can also ask it to iterate over all the files that are currently present in the same directory, until we run out of files to check/iterate over. It does that automatically, we just have to tell it to iterate over the current directory (`for i in  *`)
	
	`for` can also run on a list of names. Example:
	`for i in anan oleg ofir inga rio`
	
	Or even on bash commands:
	`for i in pwd ls date`. for knows to run over the commands and execute them one after the other.

- `select`
	The select loop can be used to prompt a user to pick an option out of the multiple different choices that we set for the select loop. For example:
		`select name in anan inga rio oleg ofir`
		`do`
			`echo "$name selected"
		`done`
	The script above produces a text that lets the user see all the possible options and lets them pick one out of the available options. Once the user picks one option, then the code between the `do` and `done` is executed.
	The `select` loop does not end until the user decides to. It will keep asking the user to pick an option until the user decides to stop it via `CTRL+C`.
	
	
	The `select` loop is especially effective and useful when a `case` statement is used inside of it. Example:
```bash
select name in anan inga rio oleg ofir
do
	case $name in
	anan)
		echo "sleeping"
		;;
	inga)
		echo "studying until 3am"
		;;
	rio)
		echo "playing mortal kombat"
		;;
	oleg)
		echo "teaching us how to connect vscode to github"
		;;
	ofir)
		echo "misses the monkies he used to work with"
		;;
	*)
		echo "Invalid input"
		;;
	esac
done
```

The Bash Shell also allows us to create Functions and Traps.

---
## User input
Shell allows to prompt for user input:
```bash
read varname [more vars]
```
As we can see, bash allows us to read multiple variables at the same time.

Or:
```bash
read -p "prompt" varname [more vars]
```
We can echo and read variables in one line using the `read -p` command. 

Example:
```bash
#! /bin/bash

read -p "enter your name: " first last
echo "First name: $first"
echo "Last name: $last"
```

---

## Special Shell variables: 

 | Parameter | Meaning |
 | --------- | ------- |
 | `$0`      |   Name of the current shell script      |
 | `$1-$9`   |    Positional parameters 1 through 9      |
 | `$#`      |   The number of positional parameters         |
 | `$*`      |     All positional parameters, `$*` is one string     |
 | `$@`      |      All positional parameters, `$@` is a set of strings   |
 | `$?`      | Return status of most recently executed command         |
 |   `$$`        |Process ID of current process           |

---
## Set command

The `set` command can be used to assign values to positional parameters.

```bash
set tim bill ann fred
```
The example above allows us to assign `tim` to `$1`, `bill` to `$2`, `ann` to `$3` and `fred` to `$4`


```bash
echo $*
```
The output to the above code would be `tim bill ann fred`. `$*` prints all of our positional arguments.


```bash
echo $#
```
The output to the above code will give us 4. `$#` is the number of positional arguments we have in our code. 


```bash
echo $1
```
This code simply echoes the value of the positional argument `$1` which is `tim`

---

## Bash built in functions

- `if-then-else`
- `case`
- `loops`
	- `for`
	- `while`
	- `until`
	- `select`

As we can see, we have an extensive set of tools that we can use to achieve a certain goal using the different functions that bash allows us to use.

---
## `if` Statement

### Syntax:
```bash
if [[ command ]]
then
	code
	code
	code
fi
```
The code is executed only if the `command` succeeds.

---
## `test` Command

`test` evaluates an expression and returns true or false:
```bash
if test -w "$1"
then
	echo "file $1 is writeable"
fi
```
As we can see above, we used the `test` keyword to evaluate the boolean result of `-w "$1"` which checks if a certain file has the write permissions or not. 

Instead of using the `test` keyword, we can simply use the brackets that we are more familiar with. So, alternatively:
```bash
if [[ -w "$1" ]]
then
	echo "file $1 is writable"
fi
```
The code above does the exact same thing as the first example. 

Another way of writing the above code is the following: 
```bash
if [[ -w "$1" ]]; then
	echo "file $1 is writable"
fi
```

---
## `if-then-else` Statement

### Syntax
```bash
if [[ condition ]]; then
	statements-1
else
	statements-2
fi
```
The code above runs the `statements-1` if the condition returned true.
`statements-2` are ran if the condition returned false.

### `elif`
#### Syntax:
```bash
if [[ condition ]]; then
	statements
elif [[ condition ]]; then
	statements
else
	statements
fi
```

`elif` stands for "else if".

---
## Relational operators

| Meaning                            | Numeric | String        |
| ---------------------------------- | ------- | ------------- |
| Greater than                       | `-gt`   | -             |
| Greater than or equal              | `-ge`   | -             |
| Less than                          | `-lt`   |               |
| Less than or equal                 | `-le`   |               |
| Equal                              | `-eq`   | `=` or `==`   |
| Not equal                          | `-ne`   | `!=`          |
| str1 is less than str2             | -       | `str1 < str2` |
| str1 is greater than str2          | -       | `str1 > str2` |
| String length is greater than zero | -       | `-n str`      |
| String length is zero              | -       | `-z str`              |

---
## Compound logical expressions

`!` = `not`
`&&` = `and`
`||` = `or`
Both `&&` and `||` must be enclosed within `[[ ]]`

---
## Using the `!` operator


---
echo -n bla
prints without skipping to new line

echo -n "\*"
echo -n " "
echo
only while
only let
![[Pasted image 20230816133948.png]]
![[Pasted image 20230816134857.png]]

![[Pasted image 20230816135935.png]]

![[Pasted image 20230816141136.png]]

