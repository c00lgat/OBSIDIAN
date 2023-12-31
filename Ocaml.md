###### Video explaining Functional programming paradigm
https://www.youtube.com/watch?v=HlgG395PQWw

https://o1-labs.github.io/ocamlbyexample/
https://cs3110.github.io/textbook/cover.html

https://drive.google.com/file/d/11EBjuWNQ_wD-pGYXSwpxvt_Yb6B7YkTt/view?usp=sharing

Statically-typed: detects type errors at compile time; if a type error is detected, the language won't allow execution of the program.

Type-safe languages limit which kinds of operations can be performed on which kinds of data. Prevents a lot of silly errors, prevents a lot of security problems. Lots of reported break-ins were due to buffer overflows, something that is impossible in a type-safe language.

*Python* for example, is type-safe but is dynamically typed. Meaning, type errors are caught only at run time.

*C* and *C++* are statically typed but not type safe: they check for some type errors but do not guarantee the absence of all type errors.

*Java* uses a combination of static and dynamic typing to achieve type safety.

OCaml supports the following features: 
- **Algebraic datatypes**: sophisticated data structures without fussing with pointers and memory management. *Pattern matching*: enables examining the shape of a data structure, makes them even more convenient.
- **Type inference**: Do not have to type information down everywhere. Compiler automatically figures out most types. Can make code easier to read and maintain.
- **Parametric polymorphism**: Functions and data structures can be parameterized over types. Allows to reuse code.
- **Garbage collection**: Automatic memory management. No need to manually allocate and deallocate like in C.
- **Modules**: Modules help structuring large systems. They are used to encapsulate implementations behind interfaces. 

Manual annotation in OCaml: (3110 : int);;
Not a type cast! 

*Toplevel* is Ocaml's command-line interface. Similar to Python's IDLE, JShell for Java and LISP.
In a terminal, type `utop` to start the toplevel. `CTRL+D` to exit the toplevel. You can also type `#quit;;` and press enter.

### 2.1.1. Types and values
We can enter expressions into OCaml toplevel. End an expression with `;;` and press the enter key. OCaml will then evaluate the expression, tell you the resulting value and the value's type. For example:
``` toplevel
# 42;;
output: - : int = 42
```
