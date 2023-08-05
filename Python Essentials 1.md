https://realpython.com/
[[Important Links]]
https://realpython.com/learning-paths/python3-introduction/
file:///C:/Users/Anan/Downloads/Learn%20Python%20the%20right%20way.pdf
https://pymbook.readthedocs.io/en/latest/
https://www.guru99.com/python-tutorials.html
https://books.goalkicker.com/PythonBook/
https://cs50.harvard.edu/python/2022/
https://exercism.org/tracks/python

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

###  Print() Keyword Arguments
The `print()` function has two keyword arguments that can be used. 
First one is called `end`.

A keyword argument consists of three things:
A keyword identifying the argument `end` in this case, an equal sign `=` and a value assigned to that argument.
Keyword arguments are usually put at the end.

