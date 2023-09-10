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
The discard method allows us to remove a value, similarly to remove, except it does not return an error in case a certain value does not already




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
