[[Python Learning Resources]]

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

| `x = x & y`  | `x &= y`  |
| ------------ | ------------- |
| `x = x` \| `y` | `x `\|`= y` |
| `x = x ^ y`  | `x ^= y`  |

---
## Shift operators

Multiplying 12345 by 10 shifts the number to the left, filling the resulting gap with a zero: `12345 x 10 = 123450`.

And then there is also division by ten: `12340 ÷ 10 = 1234`. Dividing by ten is nothing but shifting the digits to the right.

The same kind of shifting is performed by our computers. But with one difference: computers multiply and divide by  `2` instead of by `10`.
Shifting a value one bit to the left is done by multiplying it by two; and shifting one bit to the right is like dividing by two.

#### Syntax:
```python
value << bits
value >> bits
```
The left argument of these operators is an integer value whose bits are shifted. The right argument determines the size of the shift.

#### Example:
```python
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)
```

#### Output:
`17 68 8`

#### Explanation:
- `17 >> 1` → `17 // 2` (**17** floor-divided by **2 to the power of 1**) → `8` (shifting to the right by one bit is the same as integer division by two).
- `17 << 2` → `17 * 4` (**17** multiplied by **2 to the power of 2**) → `68` (shifting to the left by two bits is the same as integer multiplication by four).

`>>` is **division**.
`<<` is **multiplication**.


### Updated priority table:
| Priority | Operator                                                           |        |
| -------- | ------------------------------------------------------------------ | ------ |
| 1        | `~`, `+`, `-`                                                      | unary  |
| 2        | `**`                                                               |        |
| 3        | `*`, `/`, `//`, `%`                                                |        |
| 4        | `+`, `-`                                                           | binary |
| 5        | `<<`, `>>`                                                         |        |
| 6        | `<`, `<=`, `>`, `>=`                                               |        |
| 7        | `==`, `!=`                                                         |        |
| 8        | `&`                                                                |        |
| 9        | \|                                                               |        |
| 10       | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `^=`, \|`=`, `>>=`, `<<=` |        |

---
## Collections of data

# Lists
```python
numbers = [10, 5, 7, 2, 1]
```

The above statement creates a list with a length of 5.
The elements in a list may have different types:
```python
`my_list = [1, None, True, "I am a string", 256, 0]`
```

If we wanted to print the list, we do it in the following way:
```python
numbers = [10, 5, 7, 2, 1]
print("This is our list printed: ", numbers)
```

What if we wanted to change the value of the first element in the list?
```python
numbers[0] = 111
numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
```
Our list has now changed: 
```python
numbers = [111, 5, 7, 2, 1]
```

To print the first element of a list, we do the following:
```python
print(numbers[0]) #prints the first number
```

If we wanted to print the entire list then we run the following code:
```python
print(numbers) #prints the entire list
```
```output 
[111, 1, 7, 2, 1]
```

If we wanted to check the list's current length, we can use the `len()` function. 
The function takes the list's name as an argument and returns the number of elements currently stored inside the list.
```python
print("List length: ", len(numbers))# Printing the list's length.
```

We can also remove elements from a list. 
When we remove an element from a list, it will vanish from the list and the list's length will be reduced by one. Example:
```python
del numbers[1]
print(len(numbers))#Now we should see that the length is 4 instead of 5 since we deleted an element
print(numbers)
```

Negative indices are legal. Can be very useful.
An element with an index equal to `-1` is the last one in the list.
```python
numbers = [111, 7, 2, 1]

print(numbers[-1])
print(numbers[-2])
```
```output
1
2
```
Although legal, we cannot go any lower than `numbers[-4]` as we will get an error! Meaning, if we write `numbers[-5]` we will get the following error:
```Error
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    print(numbers[-5])
IndexError: list index out of range
```

### Functions vs methods
In general, a typical function invocation may look like this:
```python
result = function(arg)
#The function takes an argument, does something and returns a result
```

A typical method invocation on the other hand, looks like this:
```python
result = data.method(arg)
#Note: the name of the method is preceded by the name of the data which owns the method. Next, you add a dot, followed by the method name, and a pair of parenthesis enclosing the arguments.
#The method will behave like a function, but can do something more - it can change the internal state of the data from which it has been invoked.
```

---
## Adding elements to a list: `append()` and `insert()`
A new element may be glued to the end of the existing list: 
```python
list.append(value)
```
It takes its argument's value and puts it at the end of the list. The list owns the method.
The list's length then increases by one.


The `insert()` method is a bit smarter - it can add a new element at any place in the list, not only at the end:
```python
list.insert(location, value)
```
It takes two arguments:
- First argument shows the location in which we want to enter the new element. All elements that are on the right side to the new element (including the element which resided in the place where we want to enter the new element) are shifted to the right in order to make place for the new element.

- The second is the element that we want to insert.

We can initialize a list by making it empty: `my_list = []`

```python
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)
```
```output
[1, 2, 3, 4, 5]
```

If we wanted to do the same but in the reverse order, we use the `insert()` method:
```python
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)
```

### Swapping values in Python:
Instead of a temp variable, python lets us do the following:
```python
variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1
```

We can use that to reverse an array's order:
```python
my_list = [10, 1, 8, 3, 5]  

my_list[0],my_list[4] = my_list[4],my_list[0]  my_list[1],my_list[3] = my_list[3],my_list[1]

print(my_list)   
```
```output
[5, 3, 8, 1, 10]
```
We can do the same for a 100 long array with a `for` loop:
```python
my_list = [10, 1, 8, 3, 5]

for i in range(length // 2):
my_list[i],my_list[length - i - 1] = my_list[length - i - 1],my_list[i]
```

---
## Bubble Sort

```python
my_list = [8, 10, 6, 2, 4] # list to sort
swapped = True # It's a little fake, we need it to enter the while loop.
while swapped:
	swapped = False # no swaps so far
	for i in range(len(my_list) - 1):
		if my_list[i] > my_list[i + 1]:
			swapped = True # a swap occurred!
			my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] 

print(my_list)   
```

Python has its own sorting algorithms built in:
```python
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)
```

Python also has its own `reverse()` method as well:
```python
lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()

print(lst) # outputs: [4, 2, 1, 3, 5]
```

The name of a list is the name of a **memory location where the list is stored**. Meaning:
```python
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)
```
Will print out `2` and not `1`!

The assignment: `list_2 = list_1` copies the name of the array, not its contents. In effect, the two names (`list_1` and `list_2`) identify the same location in the computer memory. Modifying one of them affects the other, and vice versa.


How do we cope with that behavior? The `slice` syntax.
A slice is an element of Python syntax that allows you to **make a brand new copy of a list, or parts of a list**.
It actually copies the list's contents, not the list's name.

```python
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)
```
The output will now be `1` instead of `2` as seen above. 
The default syntax of the slice is `my_list [start:end]`
The `slice` usually does not copy the `end` index, but rather the `end - 1` index: 
```python
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
```
The `new_list` list will have `end - start` (3 - 1 = 2) elements - the ones with indices equal to `1` and `2` (but not `3`).

The snippet's output is: `[8, 6]`

### Negative indices and slice
This is how they work:
```python
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
```
```output
[8, 6, 4]
```

If the `start` is omitted from the slice, the slice will assume that we want to get a slice from the beginning or from index `0`.

`my_list[:end]` is the same as `my_list[0:end]`

Similarly, if the `end` is omitted, then the slice will assume that we meant to slice until the last index:
`my_list[start:]` is the same as `my_list[start:len(my_list)]`

We can use `del` to delete slices as well! 
```python
my_list = [10, 8, 6, 4, 2] 
del my_list[1:3]
print(my_list)
```
```output
[10, 4, 2]
```


```python
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)
```
That will delete all elements at once, leaving the array completely empty.
Whereas:
```python
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)
```
Will completely delete the array and it will no longer exist.


Python can check whether an element exists in an array or not: `in` and `not in`:
```python
elem in my_list
elem not in my_list
```
For example:
```python
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
```
The `in` and `not in` will return `True` and `False` values.

---
## LAB 3.6.1.9
Imagine a list - not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.

Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.

```python
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Write your code here.

print("The list with unique elements only:")
print(my_list)
```

Solution:
```python
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

temp = []

# Write your code here.
i=0
while i < len(my_list):

    if my_list[i] in my_list[i+1:]:

        del my_list[i]

        i=0

    else:

        i=i+1

print("The list with unique elements only:")

print(my_list)
```

---
## List in lists

Python has special syntax that is used to fill huge lists:
```python
row = []  for i in range(8):  row.append(WHITE_PAWN)
```

That is not the syntax, that was an example of what we are trying to do with the special syntax that is listed below:
```python
row = [WHITE_PAWN for i in range(8)]
```
The part of the code placed inside the brackets specifies:
- the data to be used to fill the list (`WHITE_PAWN`)
- the clause specifying how many times the data occurs inside the list (`for i in range(8)`)

The special syntax is called `list comprehension`

More `list comprehension` examples:
```python
squares = [x ** 2 for x in range(10)]
```
The snippet produces a ten-element list filled with squares of ten integer numbers starting from zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

Example two:
```python
twos = [2 ** i for i in range(8)]
```
The snippet creates an eight-element array containing the first eight powers of two (1, 2, 4, 8, 16, 32, 64, 128)

Example three:
```python
odds = [x for x in squares if x % 2 != 0 ]
```
The snippet makes a list with only the odd elements of the `squares` list.

---
## Two dimensional arrays
Example:
```python
board = []  
for i in range(8):
row = [EMPTY for i in range(8)]  board.append(row)
```
- the inner part of the loop creates a row consisting of eight elements (each of them equal to `EMPTY`) and appends it to the `board` list;
- the outer part repeats it eight times;
- in total, the `board` list consists of 64 elements (all equal to `EMPTY`)

- the elements of the rows are fields, eight of them per row;
- the elements of the chessboard are rows, eight of them per chessboard.

The `board` variable is now a **two-dimensional array**. It's also called, by analogy to algebraic terms, a **matrix**.


We can shorten the board creation in the following way:
```python
board = [[EMPTY for i in range(8)] for j in range(8)]
```
The inner part creates a row, and the outer part builds a list of rows.

---

## Functions and scopes
A scope is the part of a code where a variable is properly recognizable. 

For example:
```python
def scope_test():
    x = 123

scope_test()
print(x)
```
In the example above, we will get the following error:
> `NameError: name 'x' is not defined`


Can a function recognize a variable that resides outside the function? Lets test that out:
```python
def my_function():
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)
```
```Output
Do I know that variable? 1
1
```

The answer to that is, yes: **a variable existing outside a function has a scope inside the functions' bodies**.

This rule has a very important exception. Let's try to find it.
```python
def my_function():
	var = 2
	print("Do I know that variable?", var)
	
var = 1
my_function()
print(var)
```
The result has changed, too - the code produces a slightly different output now:
```Output
Do I know that variable? 2
1
```
- the `var` variable created inside the function is not the same as when defined outside it - it seems that there two different variables of the same name;
- moreover, the function's variable shadows the variable coming from the outside world.

**A variable existing outside a function has a scope inside the functions' bodies, excluding those of them which define a variable of the same name.**

It also means that the **scope of a variable existing outside a function is supported only when getting its value** (reading). Assigning a value forces the creation of the function's own variable.

---
## The `global` keyword
There's a special Python method which can **extend a variable's scope in a way which includes the functions' bodies** (even if you want not only to read the values, but also to modify them).
Such an effect is caused by a keyword named `global`:
```python
global name
global name1, name2, ...  
```

Using this keyword inside a function with the name (or names separated with commas) of a variable(s), forces Python to refrain from creating a new variable inside the function - the one accessible from outside will be used instead.

In other words, this name becomes global (it has a **global scope**, and it doesn't matter whether it's the subject of read or assign).

```python
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
 
```
The code now outputs:
```Output
Do I know that variable? 2
2
```

This should be sufficient evidence to show that the `global` keyword does what it promises.

---
## Behavior of lists inside functions
- if the argument is a list, then changing the value of the corresponding parameter doesn't affect the list (remember: variables containing lists are stored in a different way than scalars),
- but if you change a list identified by the parameter (note: the list, not the parameter!), the list will reflect the change. ie. deletion of an index.

---
## BMI calculation function

```python
def ft_and_inch_to_m(ft, inch = 0.0):
	 return ft * 0.3048 + inch * 0.0254
	
print(ft_and_inch_to_m(6))
```

```python
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2


print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))


```
---
## Fibonacci numbers
```python
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))


```

```Output
1 -> 1
2 -> 1
3 -> 2
4 -> 3
5 -> 5
6 -> 8
7 -> 13
8 -> 21
9 -> 34
```

---
## Recursion
Recursion is a **technique where a function invokes itself**.

**The Fibonacci numbers definition is a clear example of recursion**. We already told you that:
**Fib(i) = Fib(i-1) + Fib(i-2)**

The definition of the ith number refers to the i-1 number, and so on, till you reach the first two.

Can it be used in the code? Yes, it can. It can also make the code shorter and clearer.

The second version of our `fib()` function makes direct use of this definition:
```python
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
```

Yes, there is a little risk indeed. **If you forget to consider the conditions which can stop the chain of recursive invocations, the program may enter an infinite loop**. You have to be careful.

Factorial in recursive:
```python
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
```

---
