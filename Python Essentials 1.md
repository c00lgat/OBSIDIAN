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

String methods:
- `capitalize()` – changes all string letters to capitals;
- `center()` – centers the string inside the field of a known length;
- `count()` – counts the occurrences of a given character;
- `join()` – joins all items of a tuple/list into one string;
- `lower()` – converts all the string's letters into lower-case letters;
- `lstrip()` – removes the white characters from the beginning of the string;
- `replace()` – replaces a given substring with another;
- `rfind()` – finds a substring starting from the end of the string;
- `rstrip()` – removes the trailing white spaces from the end of the string;
- `split()` – splits the string into a substring using a given delimiter;
- `strip()` – removes the leading and trailing white spaces;
- `swapcase()` – swaps the letters' cases (lower to upper and vice versa)
- `title()` – makes the first letter in each word upper-case;
- `upper()` – converts all the string's letter into upper-case letters.


- `endswith()` – does the string end with a given substring?
- `isalnum()` – does the string consist only of letters and digits?
- `isalpha()` – does the string consist only of letters?
- `islower()` – does the string consists only of lower-case letters?
- `isspace()` – does the string consists only of white spaces?
- `isupper()` – does the string consists only of upper-case letters?
- `startswith()` – does the string begin with a given substring?

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

|  `A` |  `B` | `A & B` | `A` \| `B` | `A ^ B` |
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

Another way to append new values to an existing list is by doing the following:
```Python
list1= [1,2,3]
list1 += 'hello'
print(list1)
```
But as we can see, the list that we receive looks like the following:
`[1,2,3,h,e,l,l,o]`.
Since *strings* behave similarly to lists, the above code is basically the same as adding two lists together.

So, if we want the entire word "hello" to be a single value inside the list, we run the following code:
```Python
list1= [1,2,3]
list1 += ['hello']
print(list1)
```
Tells the code that the word hello is a single value as opposed to 5 different values of letters that make up the word hello.


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

###### List.count(`value`)
Counts how many times a value exists inside a list.

###### List.index(`value`)
Returns the index in which a value is located inside a list.

What if a list contains more than one of the same value? The function returns the first occurrence of the value inside the list.

`list.index(90, 5)` tells the index function to start looking for the value "90" starting from the fifth index.

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
We can also run the following code, sorting and then reversing the list simultaneously:
`my_list.sort(reverse=True)`

Python also has its own `reverse()` method as well:
```python
lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()

print(lst) # outputs: [4, 2, 1, 3, 5]
```
---
### Copy lists

```Python
list1 = [1,2,3,4,5]
list2 = list1.copy()
```
Copies the content of a pre-existing list to a new list that we just created. list1 and list2 in this case are not pointing at the same list object in memory.

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



---
### Remove values from lists
```Python
list1= [1,2,3]
list1.remove(3)
```
Removes the value 3 from the list.

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
`clear` on the other hand, deletes all the values inside a list but does not delete the list itself.

`del` can also be used to delete one index at a time:
```python
del my_list[5]
```
Deletes the value that is stored in the fifth index inside the list.


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

> alternatively, we could have iterated over the list by using a for in the following way:
> 
> `for i in range(my_list.count(value))` as it lets us know how many times a certain value exists in the list.

---
### Pop
Pop method "pops out" a value, or in other words, removes it, but also it returns the value that was removed. Pop removes the last value in a list.

One useful way we could use pop is to store the numbers that we have removed so far from a list:
```Python
nums = [1,4,656,768,2,5,78,34,894,12]
removed_number = nums.pop()
print(removed_number)
```

Not only we could store it in an int type variable, but we could also store the removed numbers inside another list if we wanted to keep the values around and not lose them forever. Maybe useful while manipulating lists in specific ways that require us to remove values but also store the values that were removed.

---
## Nested Lists
```python
inner1 = [1,2,3]
inner2 = [11,22,33]
inner3 = [111,222,333]
lists = []
lists.append(inner1)
lists.append(inner2)
lists.append(inner3)

print(lists)
```
```Output
[[1,2,3],[11,22,33],[111,222,333]]
```
- `len(lists)` returns 3 as there are 3 values inside lists, and each one of these values are a list themselves.

- `lists[0][0]` returns 1 (returns the first list inner1 and then the first value from the list inner1 which is 1).

- `lists[-1][1]` returns 222. The first -1 returns the last value from lists which is inner3, and the second 1 returns the index 1 which contains the value 222.

---
## List in lists

###### Lists in lists without list comprehensions:
```Python
import random as rd

matrix = []
for i in range(4):
	row = []
	for j in range(4):
		row.append(rd.randint(10,99))
	matrix.append(row)

print(matrix)
```

### List Comprehensions
https://youtu.be/OM4Ep-Zo2tA?si=XKdfkcVlpkRAXKAW

Can be used on tuples, sets, dictionaries etc.

```Python
prices = [10,14,56,34,87,34,12,95]
```

```Python
prices = [10,14,56,34,87,34,12,95]
prices_in_shekels = []

for price in prices:
	prices_in_shekels.append(price * 3.5)

print(prices_in_shekels)
```

We can do the above code in a single line:
```Python
prices = [10,14,56,34,87,34,12,95]

prices_in_shekels = [price * 3.5 for price in prices]

print(prices_in_shekels)
```
Output:
![[Pasted image 20230910160137.png]]

```Python
from random import uniform
prices = [round(uniform(1,50),2) for i in range(20)]
```
Creates a list that has 20 random numbers between 1 and 50.


What if we wanted to use list comprehensions to get the first letter of each word in a specific sentence?
```Python
sentence = 'The cold never bothered me anyway'

first_letters = [word[0].upper() for word in sentence.split()]
```
![[Pasted image 20230910161404.png]]

###### List Comprehensions - Conditions
We can use conditions inside List Comprehensions.
```Python
import random as rd

numbers = [rd.randint(1,150) for i in range(50)] # Normal list comprehension
```
But what if we wanted to filter out some values?
```Python
import random as rd

above_120 = [n for n in numbers if n > 120] 
```
The above code goes over the list `numbers` and only puts those that are above 120 inside the new list that we created with the name `above_120`.

List Comprehensions with conditionals is an easy way to filter out certain values from a pre-existing list and make a new list with the desired values.

```Python
import random as rd

above_120 = [n * 1.2 for n in numbers if n > 120] 
```
Takes all numbers that are above 120 from `numbers`, multiplies them by 1.2 and adds them to the new list.

###### List comprehensions `else`
https://youtu.be/w1HKCR43LHE?si=TyLg0mXPNKceWEZw
```Python
import random as rd

above_120 = [n * 1.2 if n > 120 else n for n in numbers] 
```
Returns all the numbers that are bigger than 120 and multiplies them by 1.2, and if the number isn't greater than 120, then simply return n for every n in `numbers`.


```Python
text = 'The past can hurt. But the way I see it, you can either run from it, or learn from it.'
vowels = 'aeiou'
print([letter for letter in text if letter in vowels])
```
Prints all the vowels from the text provided using list comprehensions.

Instead, we can print an asterisk for each time that we find a vowel in the text:
```Python
text = 'The past can hurt. But the way I see it, you can either run from it, or learn from it.'
vowels = 'aeiou'
print(['*' if letter in vowels else letter for letter in text])
```
That way, we get all the letters, with the vowels being substituted with an asterisk. But the format that we get back is a little weird and it looks like this:
![[Pasted image 20230910163423.png]]
So we use a little trick that is used to join strings together:
```Python
text = 'The past can hurt. But the way I see it, you can either run from it, or learn from it.'
vowels = 'aeiou'
print(''.join(['*' if letter in vowels else letter for letter in text]))
```
![[Pasted image 20230910163505.png]]
And this is the output that we get.

We can also do the same thing in many other variations. If for whatever reason we wanted to print the vowels as an asterisk and all the other letters as an underscore (\_) then we do it as follows:
```Python
text = 'The past can hurt. But the way I see it, you can either run from it, or learn from it.'
vowels = 'aeiou'
print(''.join(['*' if letter in vowels else '_' letter for letter in text]))
```
![[Pasted image 20230910163625.png]]
This is the output we get.

Another example that works with temperature degrees:
```Python
import random as rd
temp = [rd.randint(0,38) for n in range(30)]
```
Now we want to substitute the temperature degrees with the feelings 'Cold', 'Nice' and 'Hot':
```Python
import random as rd
temp = [rd.randint(0,38) for n in range(30)]

print(['Cold' if t < 15 else 'Nice' if t < 25 else 'Hot' for t in temp])
```
And we get the following output:
![[Pasted image 20230910164009.png]]

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
## Dictionary Comprehensions
https://youtu.be/QhRjdrfqKd4?si=S9GZJBRN4-TP5SI3

Dictionary comprehensions allow us to make dictionaries in an easier, more efficient way.

We want to make a dictionary where the key is a number and the value for each corresponding key is the squared value of each key:
```Python
squares = {n: n**2 for n in range(1,11)}
```
We get the following output:
![[Pasted image 20230910165516.png]]

Now, we want to make a dictionary where each word is a key and each value for the corresponding key is the length of the word:
```Python
fc = 'The first rule of Fight Club is you do not talk about Fight Club.'
words = {word: len(word) for word in fc.split()}
```
> We need to split the string since strings behave just like lists. So if we run the code without the split, our string will just be a list of singular letters instead of complete words. The split will give us the following output, which is the desired output on which we want to run the code on:
> 
> ![[Pasted image 20230910165841.png]]

We get the following output:
![[Pasted image 20230910165940.png]]
As we can see, we received a dictionary in which each key is a word and its value is the length of the word.


What if we wanted to flip the keys to values and the values to keys?
```Python
my_dictionary = {1: 'aa', 2: 'bb', 3: 'cc', 4: 'dd', 5: 'ee', 6: 'ff'}

flip_keys = {v: k for k,v in my_dictionary.items()}
```
Output:
![[Pasted image 20230910174603.png]]

We can also use conditionals:
```Python
my_dictionary = {1: 'aa', 2: 'bb', 3: 'cc', 4: 'dd', 5: 'ee', 6: 'ff'}

flip_keys = {v: k for k,v in my_dictionary.items() if k % 2 ==0}
```
Output:
![[Pasted image 20230910174643.png]]

###### Complex dictionaries with dictionary comprehensions

```Python
drinks = {'Cola': 5, 'Coffee': 8.5, 'Tea': 6, 'B eer': 12, 'Wine': 15}

drinks = {name: {'NIS': price, 'USD': round(price * 3.52,2), 'Euro': round(price * 3.78,2), 'Yen': round(price * 3.2,2)} for name, price in drinks.items()}
```

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
## Tuples
Tuples and lists are similar in the way we initialize them:
```Python
my_list = []
my_tuple = ()

my_list = [1,2,3]
my_tuple = (1,2,3) 
```

We can also turn any list into a tuple:
```Python
my_tuple = tuple([1,2,3])
```

The main difference between tuples and lists is that we cannot change values in tuples.

Both tuples and strings are immutable.

###### Tuple methods:
- `tuple_values.count(value)`: counts how many a certain value has occurred inside the tuple
- `tuple_values.index(value)`: returns the index in which the value exists
- `sorted(tuple_values, reverse=True)`: returns the values of the tuple in a sorted manner. Does not change the tuple itself.
- `a,b,c = (1,2,3)`: sometimes, certain get methods return tuples and we want to keep the order of the tuples intact. Example:
```python
 values = [(1,10),(2,20),(3,30),(4,40)]
 for n1,n2 in values:
	 print(n1,n2)
```
---
## Zip and Enumerate
https://youtu.be/tKippVMbsEI?si=2Uhp3nHeXkfP4cdf
Tuple unpacking.
```Python
a,b,c = (1,2,3)
a,b,c = 1,2,3
a,b,c = [1,2,3]
```
Not necessary to use tuple. But Python does use tuples in that format automatically.

We want to find all the numbers greater than 3:
```Python
numbers = [1,2,3,4,1,2,3,4,1]

for number in numbers:
	if number > 3:
		print(number)
```
Sometimes, we also want to know which index each 4 is located at:
```Python
numbers = [1,2,3,4,1,2,3,4,1]

for num in numbers:
	if num > 3:
		print(num, number.index(number))
```
In that case, we will get the following output:
```Output
4 3
4 3
4 3
```
If you can recall, the method `index()` only returns the first index in which a value occurs. Enumerate can solve that:
```Python
numbers = [1,2,3,4,1,2,3,4,1]

for index, num in enumerate(numbers):
	if num > 3:
		print(num, index)
```
Enumerate will generate a tuple in which will help us figure out the index in which a number exists.
```Output
4 3
4 6
4 8
```

Example for `zip`:
```Python
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

calls = [23,13,26,41,11,31,12] #number of calls received each day of the week

list(zip(days,calls))
```
```Output
[('Sunday',23), ('Monday',13), ('Tuesday',26), ('Wednesday',41), ('Thursday',11), ('Friday',31), ('Saturday',12)]
```
---
## Dictionaries
https://youtu.be/b3dn4VFN-O4?si=p8y6wgNWQre1K-cD

Dictionaries work with `key` and `values`.

Say we have a list of bus lines. But there is key information missing: destinations.
We cannot display the destination to each one of the bus lines using just a list in an efficient and easy to read way.
```Python
buses = [123,45,67,432]
```

And for that purpose, dictionaries are used:
```Python
buses = {123: 'Tel Aviv', 45: 'Ramat Gan', 67: 'Jerusalem', 432: 'Tel Aviv'}
```

We cannot read dictionaries the conventional way: `buses[0]` will return an error.
Instead, we use the `key` part of each field to access the data stored in the relevant field:
```Python
print(buses[123])
```
```Output
'Tel Aviv'
```

Another example for what we can do with dictionaries:
```Python
clients = {100: {'first name': 'Rick', 'last name:': 'Sanchez'},
	200: {'first name': 'Peter',
	 'last name': 'Griffin'},
	300: {'first name': 'Homer',
	'last name': 'Simpson'}}
```
We made a dictionary inside a dictionary. Each number represents a client and each client represents the first name of the client and the last name of the client.
```Python
print(clients[100])
```
```Output
{'first name': 'Rick',
'last name': 'Sanchez'}
```
In order to access the data of the first dictionary, for example the last name of client 100:
```Python
print(clients[100]['last name'])
```
```Output
'Sanchez'
```
Dictionaries allow us to grab data without having to remember the index in which a client's data exists. We can simply pull the data of client 100 and get the 'last name' field of said client.

With dictionaries, we can dig even deeper:
```Python
clients = {100: {'first name': 'Rick', 'last name:': 'Sanchez'},
	200: {'first name': 'Peter',
	 'last name': 'Griffin'},
	300: {'first name': 'Homer',
	'last name': 'Simpson',
	'children': ['Bart','Lisa','Maggie'],
	'address': {'house': 742,
	'street': 'Evergreen Terrace',
	'city': 'Springfield',
	'country': 'USA'}}}
```
By using a dictionary, we were able to list all kinds of information about a client in the same dictionary.
```Python
print(clients[300]['address']['street'])
```
```Output
'Evergreen Terrace'
```

###### Initializing a dictionary:
```Python
rest = dict()

rest = {}
```

Adding key-values to dictionaries:
```Python
menu = {'Hummus': 9.90, 'Pizza': 15.5}
```
If we wanted to add a new key-value, we do it in the following way:
```Python
menu['Salad'] = 12.1
```
Printing the dictionary will return the following:
```Output
{'Hummus': 9.90, 'Pizza': 15.5,'Salad': 12.1}
```

Say the price of Salad went down. So, if we wanted to update a certain value in the dictionary, we do it the following way:
```Python
menu['Salad'] = 9.5
```

If we wanted to delete a certain key-value, we use the `pop()` method.
The following code will remove 'Salad' from the menu as well as store it in a variable:
```Python
price = menu.pop('Salad')
```

We can also use the `del` function:
```Python
del menu['Hummus']
```

Deleting the entire dictionary is done by using `del` as well:
```Python
del menu
```
menu will no longer exist in the memory and will be entirely deleted.

###### Dictionary keys
https://youtu.be/c12hsJCZZak?si=PJOes9z8JMt5tusc
```Python
menu = {'Hummus': 9.90,
		'Pizza': 15.5,
		'Salad': 23,
		'Hamburger': 40,
		'Chips': 5,
		'Orange Juice': 23}
```
The method `keys()` will return a list that contains all the keys in a certain dictionary:
```Python
menu.keys()
```

And if we wanted to get the keys, or the prices in this case, we use `values()` method:
```Python
menu.values()
```

And if we wanted to get both the key and the values, we use `items()`:
```Python
menu.items()
```
The `items()` method will return the following:
![[Pasted image 20230909204838.png]]
A list of tuples that contain the keys and the values.
If we wanted to print a comprehensive menu, we can do it the follow way:
```Python
for food, price in menu.items():
	print(f'The price of {food} is {price} NIS.')
```
![[Pasted image 20230909205008.png]]

In order to check whether a certain key exists in a dictionary, we get `get()` method:
```Python
menu.get('Coffee')
```
If a key does not exist, `get()` simply does not return anything.

We can also set a default value: `setdefault()` method checks whether a key exists, if it exists then it returns the value of the said key. And if the key does not exist, then the `setdefault()` will add the key-value pair to the dictionary:
```Python
menu.setdefault('Coffee', 10)
```

If we wanted to update a dictionary's values, we use the `update()` method:
![[Pasted image 20230909205424.png]]
Takes the values from `rest_new` and updates the values that correlate to the same keys that are found in both dictionaries. If not found in both dictionaries, then it will simply add it to the original dictionary.
Basically, the end product will be the union of both dictionaries.

###### Dictionary sort
https://youtu.be/NumGmnqQQj8?si=70cCYNU0eqfBn9Ky

One way we can sort a dictionary is by sorting the keys:
```Python
menu = {'Hummus': 9.90,
		'Pizza': 15.5,
		'Salad': 23,
		'Hamburger': 40,
		'Chips': 5,
		'Orange Juice': 23,
		'Wine': 30,
		'Tea': 5,
		'Beer': 17,
		'Coffee': 10}

for key in sorted(menu):
	print(key,menu[key])
```
Now that should return something similar to the following:
![[Pasted image 20230910140945.png]]
We can see that the dictionary was sorted according to the alphabetical order.

But, what if we wanted to sort according to the values instead of the keys? In this case, we would be sorting according to the price instead of the alphabetical order of the items that are on the menu. So, how do we do that?
We can access the values of the dictionary by running `menu.values()` and we would get the following output:
![[Pasted image 20230910141153.png]]

We can also run the following: `sorted(menu.values())` which returns the following output:![[Pasted image 20230910141239.png]]
It returns a sorted list that contains the values, or in this case, a list of sorted prices. But that is not very helpful, is it? Since we do not know which price correlate to which product on the menu.
Usually we are able to get certain values through the keys. But we cannot do it the other way around, we cannot get the keys only by knowing what the values are.

The way to do so is:
```Python
sorted(menu.items(), key = lambda t: t[1])
```
![[Pasted image 20230910141638.png]]
And we do get the desired output. 
We basically tell the `sorted` function that we want to change our sorting key (not the same key found in dictionaries) and by running a `lambda` function, we tell it to look at the index `[1]` instead of the first index inside the tuples. And thus, the sorted function knows to sort according to the second value that is inside the tuples.

```Python
sorted(menu.items(), key = lambda t: t[1], reverse = True)
```
If we want to reverse the order.


###### Copying a dictionary
```Python
new_menu = menu
```
Both menus will be pointing at the same location in memory. Meaning, changing the new menu will also affect the old menu. 

So instead, we can run the following code to make a new copy of a dictionary:
```Python
new_menu = menu.copy()
```
---
## Sets
Initializing a set:
```Python
empty_set = {} # This will create an empty dictionary

empty_set = set() # This will create an empty set
```

A set is unique in a way that it only contains unique values. Meaning, the value 'banana' will only appear once, even if we added it twice to our set:
```Python
fruit = {'Apple', 'Orange', 'Banana'}
fruits.add('Peach')
fruits.add('Banana'))
```
We have a Set that contains fruits. As we can see, despite having banana in the set and then adding it once again to the set, it still only appears once in the set:
![[Pasted image 20230910142903.png]]

```Error
print(fruits[0]) # Will return an error
```
One way to think about Sets is that Sets are similar to a Dictionary that only contains keys.

Another example in which shows that a set only contains unique values:
![[Pasted image 20230910143056.png]]


###### Removing a value from a Set
```Python
fruits.remove('Peach')
```
![[Pasted image 20230910143151.png]]

The problem with the `remove()` method is that it will return an error if a certain value does not exist in a Set while trying to remove the said value.

In order to not get an error that could disrupt our program, we could use the method `discard()` instead:
```Python
fruits.discard('Peach')
```
The discard method allows us to remove a value, similarly to remove, except it does not return an error in case a certain value does not exist in our Set.

###### Copying a Set
Similarly to Lists and Dictionaries, Sets uses the `copy()` method to make a new copy of an existing Set.
```Python
new_fruits = fruits.copy()
```

It also uses the `clear()` method in order to clear out all the values from an existing Set, leaving it all empty while also keeping the empty Set in memory without completely deleting it:
```Python
fruits.clear()
```
![[Pasted image 20230910143614.png]]
The above code returns an empty set.

A set can be particularly helpful in cases where we want to only store the unique values that are stored in a List:
```Python
unique_numbers = set([1,2,2,3,4,5,5,3,3,5,6,7,7,9,8,8,5,4,4,4,5,5,6,6,7,78,8,8,8,8,9,9,9,7,6,5,4])
print(unique_numbers)
```

#### Set Operations
```Python
dc_comics = {'Superman', 'Batman', 'Joker', 'Wonder Woman', 'Deadshot'}

bad_guys = {'Joker', 'Shredder', 'Rick Sanchez', 'Deadshot', 'Magneto', 'Captain Hook'}
```

###### Set union
Say we want to combine the two sets together. We can use the `union()` function:
```Python
characters = dc_comics.union(bad_guys)
```
The `characters` variable will contain all the heroes and the bad guys from both sets.

If we don't want to make a new variable and have it store the union of two sets, we can just update one of the sets instead. Updating one set will change the set instead of returning it.
```Python
dc_comics.update(bad_guys)
```
This code will update the `dc_comics` set without having to make a new variable to store the outcome because the `update()` method changes the `dc_comics` object itself instead of simply returning the union of both sets.

###### Set intersection
What if we wanted to check what values contain in both sets?
We can use the `intersection()` method:
```Python
dc_comics.intersection(bad_guys)
```
The intersection method will find the mutual values between the two sets. `intersection()` however, does not change the `dc_comics` object and it simply returns the intersection which we could then store in a new variable that we make.

If we wanted to change the `dc_comics` set itself without having to make a new variable in order to store the outcome, similarly to how `union` and `update` work, we can use `intersection_update()` instead of `intersection()` if we want to change the original set at hand without having to make a new set.

###### Set difference
Returns a set that contains values only found in A and not in B
```Python
dc_comics.difference(bad_guys)
```
![[Pasted image 20230910150736.png]]
`difference()`, much like the rest of the operations we have seen, only returns a set without making any changes to the original set. 
If we wanted the changes to happen to the original set, we use `difference_update()`
```Python
dc_comics.difference_update(bad_guys)
```

###### Symmetric Difference
Returns all values from Set A and Set B except for the values that are mutual to the two sets.
```Python
dc_comics.symmetric_difference(bad_guys)
```
![[Pasted image 20230910150942.png]]
Returns a Set that does not contain the values that the intersection method would return.
If we wanted to change the original set, we can use `symmetric_difference_update()`:
```Python
dc_comics.symmetric_difference_update(bad_guys)
```

###### Set sorting
We can sort a Set with the `sorted()` function, and the function will return a List that contains the values in a sorted manner:
```Python
sorted(dc_comics, reverse = True)
```
![[Pasted image 20230910151406.png]]
> The `sorted()` function will return a `list` and not a `set`


#### Set Boolean Methods
https://youtu.be/pbnTcCHGv0s?si=nzoE4m5ivx4HVh3p
```Python
video_games = {'Pacman', 'Super Mario', 'Space Invaders'}

games = {'Poker', 'Monopol', 'Pacman', 'Chess', 'Taki', 'Super Mario', 'Space Invaders'}
```

###### Sets: `issubset()`
```Python
video_games.issubset(games)
```
Checks whether a certain set is a subset of a bigger set. Meaning, checks if **all** values in a certain set exist in another set. The `issubset()` method checks whether `video_games` is contained within `games`.

###### Sets: `issuperset()`
```Python
games.issuperset(video_games)
```
Checks whether a Set is the superset of a given Set. Meaning, it checks if the given set is a subset of the superset or not.

###### Sets: `isdisjoint()`
```Python
games.isdisjoint(video_games)
```
Returns True if both sets have no mutual value whatsoever.
Returns false if there are mutual values between the two sets.

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
## Lambda **Λ**
Short YT video that explains about lambda functions in Python
https://www.youtube.com/watch?v=KR22jigJLok

https://youtu.be/xhN_xbMUAHU?si=jXx4lIlMX3VHI3Hd

Anonymous function.
Call a function without making an actual fully fledged function.
It can make the code easier to read. 

We can pass a Lambda function as a function argument to another function.

We also use it if we wanted to change the behavior of a pre-existing function in very specific cases.

Used for simpler things.
```Python
lamb = lambda n: n**2
lamb(5)
```
What does it expect? a number `n` and it returns `n**2`.
Usually, we do not give names/store lambda functions in variables. The example above is for demonstration only, and it is not a practical use case of the `lambda` function.

More examples:
```Python
lamb = lambda a,b: a*b
lamb(4,9)
```

```Python
lamb = lambda a,b: a if a > b else b
lamb(40,9)
```

If you recall, we used a lambda function when we wanted to sort a dictionary with the values being the sorting factor.
```Python
money_heist = {'Tokyo': 400,
			  'Nairobi': 590,
			  'El Profesor': 650,
			  'Denver': 530,
			  'Rio': 270,
			  'Bogota': 340,
			  'Berlin': 480}
```

When we wanted to sort our dictionary, we figured that we could just use the `sorted()` function:
```Python
print(sorted(money_heist))
```
But what we got instead, was the key values of the dictionary in a sorted manner. What we are looking for is to sort the dictionary according to the values of the keys, not the other way around.
The output should look like the following:
![[Pasted image 20230910190507.png]]

Since we want to sort our dictionary according to the amount of money each of the characters stole, we use the `key` option in `sorted()`:
```Python
print(sorted(money_heist.items(), key = lambda t: t[1]))
```
Since `money_heist.items()` returns a list of tuples, we use the `t[1]` notation to be able to access the value of each key (since the key exists at `t[0]`).
Output:
![[Pasted image 20230910191031.png]]

We are also able to sort according to the length of the keys of the dictionary:
```Python
print(sorted(money_heist), key = len)
```
![[Pasted image 20230910190710.png]]

---
## Map
Short video that explains what a map is
https://www.youtube.com/watch?v=8q2vICb89ys

https://youtu.be/-E3qKYwH7T0?si=z9dbacu01LEQz8m7

```Python
def sqr(number):
	return number ** 0.5
```
A function that calculates the square root of a number.

```Python
def sqr(number):
	return number ** 0.5

numbers = []

for i in range(20):
	numbers.append(rd.randint(1,100))

print(numbers)

squares = []
for number in numbers:
	squares.append((sqr(number)))
print(squares)
```
Output:
![[Pasted image 20230910202228.png]]
As we can see, it takes a lot of code in order to achieve something that is relatively simple.
We could use list comprehensions that will make our code much simpler and cleaner.

But in this chapter, we will be using the `map()` function.

```Python
def sqr(number):
	return number ** 0.5

numbers = []

for i in range(20):
	numbers.append(rd.randint(1,100))


list(map(sqr, numbers)) # We turned it into a map for demonstration purposes only
```
`map(sqr, numbers)` returns a `map` object.
![[Pasted image 20230910202142.png]]
> We only converted the map into a list for demonstration purposes only. But as we can see, we got the same output as our first code.

Sometimes, a certain function that we use in our code resides inside another `.py` file.
What if we do not remember what the `sqr` function does? What if we forgot how it was implemented?

In that case, we can use a `lambda` function instead. 
Since we already know what function we are looking for, and since we know that it is a simple function that only calculates the square root of a number, and possibly going to use it very few times, then it is a good idea to consider using a `lambda` function:
```Python
list(map(lambda n: n ** 0.5,numbers))
```
![[Pasted image 20230910202558.png]]
And as we can see, we get the same output as before.
And to make it a little easier to read, we add the `round()` function:
```Python
list(map(lambda n: round(n ** 0.5,2),numbers))
```
Output:
![[Pasted image 20230910202651.png]]

---
## Reduce
Video that shows the `map()`, `filter()` and `reduce()` functions
https://www.youtube.com/watch?v=nMS5ptwax08

https://youtu.be/Wce8vVezoTI?si=WOleLadSStOCKrkE

Reduce and Lambda functions work really well together.

As opposed to the `map()` function, `reduce()` helps us to reduce a list into a single value.

`reduce()` returns a single value as opposed to `map()` which returns a whole list that is as big as the original one.

`reduce()` *has* to receive two variables, and has to return only one value.

Say we have the following dictionary that contains marvel movies along with their profits:
![[Pasted image 20230910212143.png]]
And we wanted to make a function that calculates an average of two numbers:
```Python
def average(n1, n2):
	return (n1 + n2) / 2
```
```Python
average(100,200)
```

What if we wanted to run the function on a list that has more than just two values?
Then we would have to run with a `for` loop and calculate the sum etc.

Instead, we can use `reduce()`.
`reduce()` is imported from the `functools` library:
`from functools import reduce`

```Python
from functools import reduce

reduce(average, [100,200])
```
We have to remember that reduce will only work with functions that receive only two arguments, and also return a single value as well.

Instead of having to build a function that calculates the average of two numbers once at a time, we can just use an anonymous function, or as also called a `lambda` function.
```Python
from functools import reduce

reduce(lambda n1, n2: n1 + n2, movies.values())/len(movies)
```
As we can see, reduce and lambda both allow us to do the calculations that we need to run, without having to use a new function, list or loops.

We can also use conditionals inside our `lambda` function as we have seen before:
```Python
from functools import reduce

reduce(lambda n1, n2: n1 if n1 > n2 else n2, movies.values())/len(movies)
```

---
## Filter
https://youtu.be/TU0Chfdjm7g?si=IFzG3gVt_mvd3lrm
![[Pasted image 20230910214428.png]]
Helps us filter out a list according to criterions that we set.

The `filter()` function has to receive a Boolean function.
More specifically, a function that receives only one argument and returns either `True` or `False`.
Only those values that return `True` will be added to the list that `filter()` makes for us.
![[Pasted image 20230910215206.png]]

As for the movies sample up top, we are going to be checking which movies made a certain amount of time and then use the filter function to receive the movies that are relevant.

Firstly, we are going to do that without the use of `lambda` and `filter` functions.
```Python
def profit_range(amount):
	if amount >= 250 and amount <= 500:
		return True
	else:
		return False

for profit in movies.values():
	print(profit_range(profit))
```

Now we want to do the same, except for the movie names instead of the value fields of the movies:
```Python
def profit_range(amount):
	if amount >= 250 and amount <= 500:
		return True
	else:
		return False

filtered_movies = []

for name, profit in movies.items():
	if(profit_range(profit)):
		filtered_movies.append(name)

print(filtered_movies)
```
Output:
![[Pasted image 20230910220111.png]]
We received all the movies that are valid according to the criterion that we have set.

As we can see, the entire process is quite long. We had to use a for loop, conditionals and other things along the way only to achieve what is needed.
For that, the `filter()` makes it all so much simpler:
```Python
list(filter(profit_range, movies.values()))
```
The given example still does not fully do what is needed to be done. It returns a list of profit values as opposed to the movie names that have said profit. And we still had to build a function that does the boolean check to check whether a movie is within the profit range or not.

We can take that one step further and make it even more efficient and simpler:
```Python
list(filter(lambda movie: 250 <= movie[1] <= 500, movies.items()))
```
![[Pasted image 20230910220906.png]]
As we can see, we got the desired output that lists both the movie names and the profit of each movie, without using a fully fledged function, nor a loop.

---
## Reading Files with Python
https://youtu.be/lMK32yVcwNg?si=1KT_VAuGJH2H6siZ

---
### Keyword argument passing
As opposed to positional argument passing, the meaning of the argument is dedicated by its name and not by its position.
```Python
def test_function(first_arg, second_arg):
	print(f'First Arg: {first_arg}, Second arg: {second_arg}')

# We could run the function in two different ways:
test_function('first_arg', 'second_arg')

# Or; we could do it the keyword argument way:
test_function(second_arg = 'this is going to be the second argument', first_arg = 'this is going to be the first argument that is passed to the function')
```

We can also use both keyword and positional argument passing simultaneously; but under one condition: <mark style="background: #FFB86CA6;">positional arguments before keyword arguments.</mark>
```Python
def adding(a, b, c):
	print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3) #Positional
adding(c = 1, a = 2, b = 3) #Keyword Args

adding(3, c = 1, b = 2) #Mixing both positional and keyword argument passing
```

---
### Functions and scopes
**A variable existing outside a function has a scope inside the functions' bodies**.
```Python
def my_function():
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)
```

###### Global variables
``` python
global name
global name1, name2
```
Using this keyword inside a function with the name (or names separated with commas) of a variable(s), forces Python to refrain from creating a new variable inside the function - the one accessible from outside will be used instead.
```Python
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)
```
In other words, this name becomes global (it has a **global scope**, and it doesn't matter whether it's the subject of read or assign).

---
### Dictionaries
When you write a big or lengthy expression, it may be a good idea to keep it vertically aligned. This is how you can make your code more readable and more programmer-friendly, e.g.:

```Python
dictionary = {"cat": "chat",
			  "dog": "chien",
			  "horse": "cheval"} 
```

---
#### Functions from the `math` module
- `ceil(x)` → the ceiling of x (the smallest integer greater than or equal to x)
- `floor(x)` → the floor of x (the largest integer less than or equal to x)
- `trunc(x)` → the value of x truncated to an integer (be careful - it's not an equivalent either of ceil or floor)
- `factorial(x)` → returns x! (x has to be an integral and not a negative)
---
#### Selected functions from the random module: continued

The previous functions have one important disadvantage - they may produce repeating values even if the number of subsequent invocations is not greater than the width of the specified range.

Look at the code below - the program very likely outputs a set of numbers in which some elements are not unique:
```Python
from random import randint
for i in range(10):
print(randint(1, 10), end=',')
```

This is what we got in one of the launches:
```Output
9,4,5,4,5,8,9,4,8,4,
```

**The `choice` and `sample` functions**
As you can see, this is not a good tool for generating numbers in a lottery. Fortunately, there is a better solution than writing your own code to check the uniqueness of the "drawn" numbers.

It's a function named in a very suggestive way - `choice`:
- `choice(sequence)`
- `sample(sequence, elements_to_choose)`

The first variant chooses a "random" element from the input sequence and returns it.

The second one builds a list (a sample) consisting of the `elements_to_choose` element "drawn" from the input sequence.

In other words, the function chooses some of the input elements, returning a list with the choice. The elements in the sample are placed in random order. Note: the `elements_to_choose` must not be greater than the length of the input sequence.

Look at the code below:
```Python
from random import choice, sample my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(my_list))  print(sample(my_list, 5))  print(sample(my_list, 10))
```  

Again, the output of the program is not predictable. Our results looked like this:
```Output
4 
[3, 1, 8, 9, 10]
[10, 8, 5, 1, 6, 4, 3, 9, 7, 2]
```


---
# Exception Handling
Getting an error, or exception, in your python program means the entire program will crash.

Instead, we want the program to detect errors, handle them, and then continue to run.

> example of a divide-by-zero error down below:
![[Pasted image 20240109184538.png]]

Errors can be handled with `try` and `except` statements.
The code that could potentially have an error is put in a `try` clause. 
The program execution moves to the start of a following `except` clause if an error happens.

Consider the following code:
```python
def spam(divideBy):  
    try:  
        return 42 / divideBy  
    except ZeroDivisionError:  
        print('Error: Invalid argument.')  
  
print(spam(2))  
print(spam(12))  
print(spam(0))  
print(spam(1))
```
When code in a `try` clause causes an error, the program execution immediately moves to the code in the `except` clause. After running that code, the execution continues as normal. The output of the previous program is as follows:
```output
21.0  
3.5  
Error: Invalid argument.  
None  
42.0
```

Now, consider the following program, where the `spam()` calls are put in the `try` block instead of inside the funciton:
```python
def spam(divideBy):  
    return 42 / divideBy  
  
try:  
    print(spam(2))  
    print(spam(12))  
    print(spam(0))  
    print(spam(1))  
except ZeroDivisionError:  
    print('Error: Invalid argument.')
```
We get the following output:
```output
21.0  
3.5  
Error: Invalid argument.
```
The `print(spam(1))` is never executed because once the exception jumps to the code in the `except` clause, it does not return to the `try` clause. Instead, it just continues moving down the program as normal.

