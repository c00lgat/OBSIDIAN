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

The `-i` option lets everything to be done in place instead of simply printing it on the screen and not really changing the content of the file.

Now, the pizza place owner changed his mind again. He wants to change the newly introduced Feta cheese topping to something else. So indecisive. But luckily, we have the power of SED on our side. The owner wants olives instead, so we give him the following command:
`sed 's/Feta/Olives/' toppings.txt`
The command prints the following on our console:
`Pizza topping combos:`
`1. Spinach, Pepperoni, Olives`
`2. Pepperoni, Olives, Mushrooms`
`3. Bacon, Banana Peppers, Olives`
`4. Cheese, Olives`

Now, upon further research and discovery of the true powers of SED, we have noticed that the slashes, are in fact, the delimiter. 
`sed` `'s`<mark style="background: #FF5582A6;">/</mark>`Feta`<mark style="background: #FF5582A6;">/</mark>`Olives`<mark style="background: #FF5582A6;">/</mark>`'` `toppings.txt`
Or, more precisely, the character that follows the `s` is the delimiter. 

So, what happens if we change every occurrence of slash to a space? 
`sed 's Feta Olives ' toppings.txt`
... Nothing. It still works. Interesting

Well! What about replacing the slash with a pipe then? 
`sed 's|Feta|Olives|' toppings.txt`
And once again, nothing. Its fine. We get the same output.
After changing it to a period `.` it is also still fine!

Our hardworking researchers that are harnessing the power of SED and trying to understand it have announced that we are able to use any character as the delimiter. Good job guys.

Well then. Why not keep using the forward slash `/` as the delimiter? 
What if the character that we want to replace *is* a forward slash `/`?

What we can do in this case, we can just use another delimiter! Basically, a forward slash `/` will work pretty much in every other case, other than the case where we want to replace a forward slash.

Here is an example where using a forward slash `/` will cause chaos and unwanted results. Our hard working researchers hate chaos and unwanted results, very much like any other kind of researcher basically. Except for rocket science researchers maybe. They love explosions.

For example, we fetched a list of all rows under `/etc` after running the following command:
`find /etc -type f`
and we got the following results:

`/etc/snmp/snmp.conf`
`/etc/magic.mime`
`/etc/machine-id`
`/etc/console-setup/compose.KOI8-R.inc`
`/etc/console-setup/compose.ISO-8859-16.inc`
`/etc/console-setup/compose.KOI8-U.inc`
`/etc/console-setup/compose.ISO-8859-3.inc`
`/etc/console-setup/cached_UTF-8_del.kmap.gz`
`/etc/console-setup/compose.ARMSCII-8.inc`
`/etc/console-setup/compose.ISO-8859-2.inc`

And we wanted to save that list of paths into a file. 
But instead of the full path, we just want to save what is after `/etc`
How do we write a statement that includes a forward slash `/`?

Running the command `sed 's//etc//'` will return an error and will not word at all.
We are not really able to use the forward slash `/` as the delimiter in this case.

`sed 's/Feta/Olives/' toppings.txt`
This command that we ran earlier, it replaced the Feta topping with the Olives topping. But what if we did not want to replace it with anything and just wanted to remove it instead?
For that, we can run the following command:
`sed 's/Feta//' toppings.txt`
After running the command, we get the following output:
`Pizza topping combos:`
`1. Spinach, Pepperoni,` 
`2. Pepperoni, , Mushrooms`
`3. Bacon, Banana Peppers, `
`4. Cheese, `
Great! We removed Feta. 
So, we can use SED to remove something and not just to replace something.

