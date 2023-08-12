https://realpython.com/
[[Important Links]]
file:///C:/Users/Anan/Downloads/Learn%20Python%20the%20right%20way.pdf
https://pymbook.readthedocs.io/en/latest/
https://www.guru99.com/python-tutorials.html
https://books.goalkicker.com/PythonBook/
https://cs50.harvard.edu/python/2022/
https://exercism.org/tracks/python

Python blog: https://www.bitecode.dev/

Function invocation in Python:
1. Python checks if the name of the function is legal, in other words, it browses its internal data in order to find an existing function of the name. If this search fails, Python aborts the code.
2. Checks if the function's requirements for the number of arguments allows us to invoke the function. If there was a sufficient number of arguments passed onto the function, the code aborts.
3. Python leaves our code for a moment, and goes to the function that we want to invoke and takes the arguments with it as well.
4. The function is executed. 
5. Python returns to our code from where it left off and goes on executing the rest of the code.

Printing a slash in Python has to be done in the following way:
```python
print("\\")
```
Since `\` is an Escape character in Python, we have to tell the language that we mean to print a slash and not use an escape character.


Passing multiple arguments to the <code>Print()</code> function:
```python
print("Hello, this is the first argument","this is the second argument","and this is the third argument.")
```
- a `print()` function invoked with more than one argument **outputs them all on one line**.
- the `print()` function **puts a space between the outputted arguments** on its own initiative.

### Print() Keyword Arguments
The `print()` function has two keyword arguments that can be used. 
First one is called `end`.

A keyword argument consists of three things:
A keyword identifying the argument `end` in this case, an equal sign `=` and a value assigned to that argument.
Keyword arguments are usually put at the end.

### `end`
```python
print("My name is", "Python.", end=" ")
print("Monty Python.")
```
The `end` keyword arguments determines what characters the print function will end with. 

The default setting for an `end` argument is `end="\n"` which is reflected with `print()`'s behavior with how it automatically skips to a new line each time its invoked.

>If the `end` argument is set to nothing, then the `print()` function will not skip to a new line upon invocation as seen below:

```python
print("My name is", "Python.", end=" ")
print("Monty Python.")
```

### `sep`
The second keyword argument that can be used in the `print()` function is called `sep` which stands for *separator*.
```python
print("My", "name", "is", "Monty", "Python.", sep="-")
```
The argument for the `sep` keyword argument can be empty as well. Doing so will not print and spaces between the words and it will come out as one word. 

Python Standard Library:
https://docs.python.org/3/library/functions.html

---
## Integers

>Integers are numbers that are devoid of fractions.

>Floating-point are numbers that contain (or able to contain) the fractional part.

These two kinds of number differ in how they are stored in a computer memory.

Python allows us to write numbers in the two following ways: 
1. 11111111 
2. Or, we can use underscores: 11_111_111 (Only available in Python 3.6 and newer versions).

### Octal and hexadecimal numbers
If an integer number is preceded by **0O** or **0o** (zero-o), it will be treated as an octal value. Meaning, the number must contain digits from the \[0--7\] range only.

For example:
`0o123` is an <mark style="background: #FFF3A3A6;">octal</mark> number. The `print()` function is able to translate octal to decimal automatically:
```python
print(0o123)
```
As we can see, an octal number `0o123` has a decimal value of 83.

#### Hexadecimal numbers
The other convention allows to use hexadecimal numbers. 
Hexadecimal numbers should be preceded by the prefix `0x` or `0X` (zero-x).

`0x123` is a hexadecimal with a decimal value of 291.
```python
print(0x123)
```

---
## Floats
The other type is called <mark style="background: #FFF3A3A6;">floats</mark>. Represent the numbers that have a *non-empty decimal fraction*.
They are numbers that have (or may have) fractional part after the decimal point.

Floating-point number examples:
- 2.5
- -0.4
Python allows us to write the number `0.4` as `.4`.
The value `4.0` can be written as `4.`.

---
#### Big exponential numbers
When we want to write large numbers, Python allows us to write them as the following: 
```python
print(3E8)
```
The letter `E`, (or `e`, both will work) comes from the word exponent. Which means *times ten to the power of*.
`3 x 10^8` is equal to `3E8`.

---
#### Small exponential numbers
Python will always choose the more economical form of the number's presentation. Run the code below and check the result that you get:
```python
print(0.0000000000000000000001)
```

---
## Strings
Strings need quote marks the same way floats need points.

Sometimes, we need to encode a quote inside a string which is already delimited by quotes such as:
`I like "Monty Python"`

One solution for that is using a backward slash or also known as, an *escape character* as we mentioned above. So in such a case, we have to place a `\` before each `"` we want to print: 
`print("I like \"Monty Python\"")`
Which results in the following output:
```python
print("I like \"Monty Python\"")
```

Another solution is using an *apostrophe* (`'`). Either of these can be used but we have to be consisted with their usage.
`print('I like "Monty Python"')`
```python
print('I like "Monty Python"')
```

Using an apostrophe in a string can be done in one of both ways. For example, if we wanted to print `I'm Monty Python.`, we can use the following syntax to achieve that:
`print('I\'m Monty Python.')`
Or
`print("I'm Monty Python.")`

> A string can be empty. An empty string still remains a string: 
> ''
> ""
> Both of which are still considered a string.

---
## Boolean values

Boolean values represent an abstract value of *truthfulness*.
When we ask Python if a number is bigger than the other, Python will return a *Boolean* value.

A Boolean value has only two distinct values: `True` and `False`. Also denoted as `1` and `0`.

When we want to use Boolean values in Python, we have to be strict about the denotations: we cannot change anything, including case sensitivity. 
`True` and `False` values should be strictly used the same way they were just typed.

---
## Basic operators
An operator is a symbol of the programming language, which is able to operate on the values.
Some of the supported operators in Python are:
`+`, `-`, `*`, `/`, `//`, `%`, `**`

### Exponentiation
A `**` (double asterisk) is an *exponentiation* (power) operator. The left argument is the base and the right argument is the exponent.

For example, in classical mathematics, 2 to the power of 3 is usually written as `2^3`. But in Python, we would write that as `2**3`.

<mark style="background: #FF5582A6;">Note</mark>: when *both* arguments are integers, the result is an integer too.
When at least one argument is a float, the result will be float as well.

>Exponentiation operator uses right-sided binding.

```python
print(2 ** 2 ** 3)
```
Usually, when performing calculations using operators in Python, we start from left to right. 
But, the order is a little different in exponentiation. 
In the example above, the way we calculate the result is the following:
`2**3` ->`8`; `2**8` -> `256`. As we can see, exponentiation operator uses **right-sided binding**.
### Multiplication
An `*` (asterisk) sign is a *multiplication* operator.

### Division
A `/` (slash) sign is a *divisional* operator.
**The result produced by the division operator is always a float.**

### Integer Division
A `//` (double slash) is an *integer divisional* operator. Differs from the standard `/` in one main way:
- The result does not have the fractional part. Its absent for integers and is always equal to zero in floats. Meaning, the results are always rounded.
- An integer by integer division gives an *integer result*. All other cases produce floats (with a rounded zero after the decimal point).
- Rounding always does toward the lesser integer value. For example: `-6 // 4` would give us `-2` instead of `-1.5` because of the rounding.

>Integer division can also be called floor division.


## Modulo
Its graphical representation in Python is `%` (percent) sign.
The result of the operator is a <mark style="background: #BBFABBA6;">remainder left after the integer division</mark>.

Examples: 
```python
print(14 % 4)
```
As we can see, the result is two and this is why:
- `14//4` gives `3` --> *this is the integer quotient*
- `3*4` gives `12` --> *as a result of quotient and divisor multiplication*
- `14-12` gives `2` --> *this is the remainder*

```python
print(12 % 4.5)
```
Gives us `3.0` and not `3`.
If we do the same calculation as the one above:
- `12//4.5` gives us `2.0`
- `2*4.5` gives us `9.0`
- `12-9.0` gives us `3.0`

<mark style="background: #FF5582A6;">Note: Division by 0 does not work.</mark>

## Addition
Works as expected.

## Subtraction
Also works as intended. 
One important thing to note though, is that the subtraction operator can be used in a unary way. Example:
```python
print(-1.1)
```
The minus sign can change the sign of a number.

## List of priorities

| Priority | Operator                                                                                           |       |
| -------- | -------------------------------------------------------------------------------------------------- | ----- |
| 1        | `**`                                                                                               |       |
| 2        | `+`,`-` (note: unary operators located next to the right of the power operator bind more strongly) | unary |
| 3        | `*`, `/`, `//`, `%`                                                                                  |       |
| 4        | `+`, `-`                                                                                                   | binary      |

---
## Variables

https://peps.python.org/pep-0008/#naming-conventions
Talks about good variable, function and class naming. 

- variable names should be lowercase, with words separated by underscores to improve readability (e.g., `var`, `my_variable`)
- function names follow the same convention as variable names (e.g., `fun`, `my_function`)
- it's also possible to use mixed case (e.g., `myVariable`), but only in contexts where that's already the prevailing style, to retain backwards compatibility with the adopted convention.

### Creating variables
Variables can be used to store any value of any of the already presented kinds, and many more.

For example:
```python
var = 1
print(var)
```

### Using variables
We can declare as many variables as we need.
```python
var = 1
account_balance = 1000.0
client_name = 'John Doe'

print(var, account_balance, client_name)
```

Variables can also be used alongside strings in the `print()` function:
```python
var = "3.8.5"
print("Python version: " + var)
```

### Shortcut operators

The following calculations can be shortened:
```python
x = x * 2
sheep = sheep + 1
```
Shortened version:
```python
x *= 2
sheep += 1
```

In other words, <mark style="background: #FFF3A3A6;">variable</mark> = <mark style="background: #FFF3A3A6;">variable</mark> <mark style="background: #FF5582A6;">op</mark> <mark style="background: #BBFABBA6;">expression</mark>
Can be simplified to:
<mark style="background: #FFF3A3A6;">variable</mark> <mark style="background: #FF5582A6;">op</mark>= <mark style="background: #BBFABBA6;">expression</mark>

---
## Key takeaways

Python is *dynamically-typed* meaning there is no need to declare variables in it. We can simply assign variables using the `=` sign.

Tip: If you'd like to quickly comment or uncomment multiple lines of code, select the line(s) you wish to modify and use the following keyboard shortcut: **CTRL** + **/** (Windows) or **CMD** + **/** (Mac OS).

---
## The `input()` function
The `input()` function allows us to read data entered by the user and send the data to the running program.

Here is a simple showcase of using the `input()` function:
```python
print("Tell me anything...")  
anything = input()
print("Hmm...", anything, "... Really?")
```

The same example can be reduced to the following, which has the same functionality:
```python
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")
```

<mark style="background: #FF5582A6;">Important Note: The result of the `input()` function is a string. </mark>
A string containing all the characters the user enters from the keyboard. It is not an integer or a float.
This means that **you mustn't use it as an argument of any arithmetic operation**, e.g., you can't use this data to square it, divide it by anything, or divide anything by it.

---
## Type casting
Python introduces two solutions to the `input()` string problem which are `int()` and `float()`.

Both  `int()` and `float()` take a string and try to convert it to an integer and a float respectively. 
If the casting is failed, the program will be terminated.

```python
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
```
---
## String to number type conversion
We can use the `str()` function to convert a number to a string.
```python
leg_a = float(input("Input first leg length: "))

leg_b = float(input("Input second leg length: "))

print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) **.5))
```
 ___
 
 ## LAB 2.6.1.11
 ```python
hour = 0#int(input("Starting time (hours): "))
mins = 1#int(input("Starting time (minutes): "))
dura = 2939#int(input("Event duration (minutes): "))

# Write your code here.
amount_of_hours = ((dura + mins) // 60)
hour = (hour + amount_of_hours) % 24

amount_of_minutes = (dura + mins) % 60
mins = amount_of_minutes
print(mins)

print(str(hour) + ":" + str(mins))
```

---

## Conditions and conditional execution 

`if statement` example:
```python
if the_weather_is_good:
	go_for_a_walk()
```

`if-else` example:
```python
if true_or_false_condition:
	perform_if_condition_true
else:
	perform_if_condition_false
```
- If the condition evaluates to `True` (value is not equal to zero) the `perform_if_condition_true` statement is executed and the conditional statement comes to an end.

- If the condition evaluates to `False` (equal to zero), then the `perform_if_condition_false` statement is executed, and the conditional statement comes to an end. 

---
## Looping your code with `while`


```
while there is something to do
	do it
```

### Syntax:
```
while conditional_expression:
	instruction
```
An indentation is a must inside the `while` loop, much like the `if` conditional.

---
## Looping your code with `for`

Syntax:
```python
for i in range(100):
	# do_something()
	pass
```


```python
for i in range(2,8):
	print("The value of i is currently ",i)
```
Iterates starting from `i=2` all the way to `i=7`.

The `range()` function can also take 3 arguments.
The third argument is an **increment**, its a value added to control the variable at every loop turn. The default value of the increments is 1.

---
## The `break` and `continue` statements

Can be used in the following cases:
- Unnecessary to continue the loop as a whole

- Need to start the next turn of the loop without completing the execution of the current turn

`break`: exits the loop immediately, and unconditionally ends the loop's operation.

`continue`: behaves as if the program has suddenly reached the end of the body of the loop and skips to the next iteration of the loop.

Syntax:
```python
# break - example
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

```

---
## Loops and `else`

Loops, like the `if` statements, also have the `else` branch too.
The loop's `else` branch is always executed once, regardless of whether the loop has entered its body or not.

Example:
```python
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

```


`for` loops behave a bit differently:
Unlike the `while` loop like the one above, in the `for` loops, the `i` variable retains its last value.
```python
for i in range(5):
    print(i)
else:
    print("else:", i)

```

---
## Bitwise operators

Lets us manipulate single bits of data. 

- `&` (ampersand) - bitwise conjunction;
- `|` (bar) - bitwise disjunction;
- `~` (tilde) - bitwise negation;
- `^` (caret) - bitwise exclusive or (xor).

| Argument `A` | Argument `B` | `A & B` | `A` \| `B` | `A ^ B` |
| ------------ | ------------ | ------- | ------- | ------- |
| `0`          | `0`          | `0`     | `0`     | `0`     |
| `0`          | `1`          | `0`     | `1`     | `1`     |
| `1`          | `0`          | `0`     | `1`     | `1`     |
| `1`          | `1`          | `1`     | `1`     | `0`     |

|Argument|`~` Argument|
|---|---|
|`0`|`1`|
|`1`|`0`|

- `&` requires exactly two `1`s to provide `1` as the result;
- `|` requires at least one `1` to provide `1` as the result;
- `^` requires exactly one `1` to provide `1` as the result.

<mark style="background: #FF5582A6;">Note</mark>: the arguments of these operators **must be integers**; we must not use floats here.

---
## Logical vs. bit operations: continued

Using logical operation:
```python
i = 15
j = 22

log = i and j
```

``` Output:
log: True
```

Using logical operation:
```python
i = 15
j = 22

log = i & j
```
The `&` operator will operate with each pair of corresponding bits separately, producing the values of the relevant bits of the result. Therefore, the result will be as follows:

| `i`           | `00000000000000000000000000001111` |
| ------------- | -------------------------------------- |
| `j`           | `00000000000000000000000000010110` |
| `bit = i & j` | `00000000000000000000000000000110` |
These bits correspond to the integer value of six.


Let's look at the negation operators now. First the *logical* one:
- `logneg = not i`

The `logneg` variable will be set to `False` - nothing more needs to be done.

The *bitwise* negation goes like this:
- `bitneg = ~i`


Each of these two-argument operators can be used in **abbreviated form**. These are the examples of their equivalent notations:

| `x = x & y`  | `x ==&=== y`  |
| ------------ | ------------- |
| `x = x` \| `y` | `x ==\|=== y` |
| `x = x ^ y`  | `x ==^=== y`  |





