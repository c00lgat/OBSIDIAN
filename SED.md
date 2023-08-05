file:///C:/Users/Anan/Downloads/Dougherty,%20Dale%20_%20Robbins,%20Arnold%20-%20sed%20&%20awk%20(2010,%20O'Reilly%20Media)%20-%20libgen.li.pdf


https://www.youtube.com/watch?v=nXLnx8ncZyE

SED is short for Stream Editor. Used to filter and modify text.
Change things in text files and more.

We are going to create a file called `topping.txt` that contains the following text and manipulate it using SED.

`Pizza topping combos:`
`1. Spinach, Pepperoni, Pineapple`
`2. Pepperoni, Pineapple, Mushrooms`
`3. Bacon, Banana Peppers, Pineapple`
`4. Cheese, Pineapple`

Now, we are going to use SED to remove the pineapple toppings, since obviously, pineapples do not belong on pizza.

`sed 's/Pineapple/Feta/' toppings.txt`
Looks for `Pineapple` and replaces it with `Feta`
`s` searches for a stream (a specific combination of a string).
The output we get is:

`Pizza topping combos:`
`1. Spinach, Pepperoni, Feta`
`2. Pepperoni, Feta, Mushrooms`
`3. Bacon, Banana Peppers, Feta`
`4. Cheese, Feta`

One thing that did not happen though, is that the file itself did not get modified. The original file still has the Pineapple toppings. 
What happened here is that the command did not override the file.

What we could do is that we can redirect the output to a new file using the `>` operator.

Or, we could just modify our command a bit and we can override our file!
`sed -i 's/Pineapple/Feta/' toppings.txt`
After running the command, we do not get an output this time around. But after running `cat toppings.txt`, we can see that the content of the file was indeed modified and pineapple is no longer on the menu, instead we have Feta cheese.

The `