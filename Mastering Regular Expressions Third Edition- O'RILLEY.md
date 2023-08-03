[[Regex]]

file:///C:/Users/Anan/Downloads/Jeffrey%20Friedl%20-%20Mastering%20Regular%20Expressions,%20Third%20Edition-O'Reilly%20(2006).pdf

![[Pasted image 20230720105558.png]]
![[Pasted image 20230720105610.png]]
![[Pasted image 20230720105623.png]]

<p>^ (caret) and $ (dollar) are the easiest to understand.
represent the start and end of the line of text.</p>
<p>^cat matches only if the c ⋅ a ⋅ t is at the beginning of the line. 
cat$ finds c ⋅ a ⋅ t only at the end of the line, such as as line ending with scat.</p>
<p>The caret and dollar are special in that they match a position in the line rather than any actual text characters themselves.</p>
<br> <br>

---

## Character Class

The regular-expression construct [˙˙˙], usually called a character class, lets you list the characters you want to allow at that point in the match.

While e matches just an e, and a matches just an a, the regular expression [ea] matches either. So, then, consider gr[ea]y: this means to find g, followed by r, followed by either an e or an a, all followed by y. The implication is OR.
"[Ss]mith" allows us to find either "smith" or "Smith" embedded within another word such as *blacksmith*.

We can list in the class as many characters as we want. For example: [123456] matches any of the listed digits. For example: <H[123456]> which matches <code>\<H1>, \<H2>, \<H3></code>, etc. This can be useful when searching for HTML headers.

Within a character class, the metacharacter '-' (dash) indicates a range of characters: <code>\<H[1-6]></code> is identical to the previous example. <code>[0-9]</code> and <code>[a-z]</code> are common for classes to match digits and English lowercase letters.
Multiple ranges such as <code>[0123456789abcdefABCDEF]</code> can be written as <code>[0-9a-fA-F]</code> (or <code>[A-Fa-f0-9]</code> since the order does not matter). Can be useful while processing [[Hexadecimal Numbers]].

You can freely combine ranges with literal characters: <code>[0-9A-ZR!.?]</code> matches a digit, uppercase letter, underscore, exclamation point, period, or a question mark.

<font color="red"> Note that a dash is a metacharacter only within a character class — otherwise it matches the normal dash character. In fact, it is not even always a metacharacter within a character class. </font>

We can consider character classes as their own mini language. 

A dash inside character classes is only valid as a range when its not in the beginning of the line. Otherwise, it will be considered as a character to look for.

ls -l [a-f]\*


<br>

---

## Negated character classes

^ is an anchor outside a character-class. But inside a class, it will match any character that *isn't* listed.
The ^ is only considered a character-class metacharacter only if it is used immediately after the class's opening bracket.

<code>grep -e q\[^u]</code> will list English words that have *q* followed by something other than *u*.

A negated character-class means "match a character that's not listed" and not "don't match what is listed".


## Matching any character with Dot

Used for "any character here". For example, while looking for a specific date such as 03/19/76, 03-19-76, or even 03.19.76, we could use a regular expression that uses character-classes to allow '/', '-' or '.' between each number: <code>03[-./]19[-./]76</code>.

>The Iraq example is somewhat of a trick question. The regular expression calls for q followed by a character that’s not u, which precludes matching q at the end of the line. Lines generally have newline characters at the very end, but a little fact I neglected to mention (sorry!) is that egrep strips those before checking with the regular expression, so after a line-ending q, there’s no non-u to be matched.
<br>

---


## Alternation
### Matching any one of several subexpressions

The character |, which means OR. Allows us to combine multiple expressions into a single expression that matches any of the individual ones. 
"<code>Bob</code>" and "<code>Robert</code>" are separate expressions. but "<code>Bob|Robert</code>" is one expression that matches either. When combined that way, the subexpressions are called *alternatives*.

Looking at a previous example <code>gr[ea]y</code>, it can be written as <code>gray|grey</code> and even <code>gr(a|e)y</code>.
<font color=red> Note that something like <code>gr[a|e]y</code> is not what we want. Within a class, the <code>|</code> is just a normal character.</font>

With <code>gr(a|e)y</code>, the parenthesis are required because without them, <code>gra|ey</code> would match *gra* or *ey*.

Another example: <code>(First|1st)\_[Ss]treet</code>, actually, <code>(First|1st)</code> can be shortened to <code>(Fir|1)st\_[Ss]treet</code> since both First and 1st end with st.

These three expressions are effectively the same:
<code>Jeffrey|Jeffery</code>
<code>Jeff(rey|ery)</code>
<code>Jeff(er|re)y</code>

To have them match the British spellings as well, they could be:
<code>(Geoff|Jeff)(rey|ery)</code>
<code>(Geo|Je)ff(rey|ery)</code>
<code>(Geo|Je)ff(re|er)y</code>

Finally, note that these three match effectively the same as the longer (but simpler): <code>Jeffrey|Geoffery|Jeffery|Geoffrey</code>.
They’re all different ways to specify the same desired matches.

We have to be careful using alternations, such as in the following example: compare <code>From|Subject|Date:_</code> with <code>^(From|Subject|Date):\_</code>
The alternation is constrained by the parenthesis. So the second regex means:
1. start-of-line, followed by F ⋅ r ⋅ o ⋅ m, followed by <code>:\_</code> *OR*
2. start-of-line, followed by S ⋅ u ⋅ b ⋅ j ⋅ e ⋅ c ⋅ t, followed by <code>:\_</code> *OR*
3. start-of-line, followed by D ⋅ a ⋅ t ⋅ e, followed by <code>:\_</code>![[Pasted image 20230722214538.png]]

### Ignoring Differences in Capitalization
The REGEX expression previously mentioned is not case sensitive, which could be a bad thing since emails have both capitalized headers and some are not capitalized. So we could miss out on a few matches.

The <code>*-i*</code> option in egrep's list of options tells it to do a case-insensitive match. Placing the <code>*-i*</code> on the command line before the regular expressions as the following:
<code>% egrep -i ’ˆ(From;Subject;Date): ’ mailbox</code>

This brings up all the lines we matched before, but also includes lines such as: SUBJECT: MAKE MONEY FAST.

### Word Boundaries
A common problem with regular expressions is that they can match words that are embedded into larger words. And for that reason, egrep offers the ability to match the boundary of a word (where a word begins or ends).

For that, we use the *metasequences*: *\\&lt* and *\\&gt;*, we can think of them as word-based versions of *^* and *$* that match the position at the start and end of a word, respectively. 

The expression *\\&lt**cat**\\&gt;* literally means "match if we can find a start-of-word position, followed immediately by c ⋅ a ⋅ t, followed immediately by an end-of-word position".
It means "find the word cat". If we wanted, we could use *\\&lt*cat or cat*\\&gt;* to find words starting and ending with cat. 

![[Pasted image 20230723194101.png]]

>A negated character class is simply a notational convenience for a normal character class that matches everything not listed. Thus, [ˆx] doesn’t mean match unless there is an x, but rather match if there is something that is not x. The difference is subtle, but important. The first concept matches a blank line, for example, while [ˆx] does not.


>The useful -i option discounts capitalization during a match.

### Optional Items
When we want to match *color* or *colour* for example. One has a "u" and the other doesn't. And for that, we can use <code>colou?r</code> to match either. 
The metacharacter *?* (question mark) means *optional*. Placed after the character that is allowed to appear at that point in the expression, but whose existence is not required to be considered a successful match.
The question mark attaches only to the immediately-preceding item.
Thus, <code>colou?r</code> is interpreted as is interpreted as “*c* then *o* then *l* then *o* then *u?* then *r*.

Example: For 4th of July, we could use <code>(July|Jul)_(fourth|4th|4)</code>. But since we now know about the question mark metacharacter, we can do it differently.

---

/e+/g
one or more than one e

/e+a?/g
the a? means a is optional

/ea*/g
\* match zero or more

/.at/g
the dot character will match any character. cant match a new line

/\./g
meaning look for a normal period. the \ is an escape character

/\w/ search any word letter 
/\W/ not 

/\s/ any form of white space
/\S/ no white spaces

/\w{4,}/
get any more digits or more

/\w{4,5}/

/[fc]at/g
any characters that we want to match
matches anything that starts with f or c and ends with at

/[a-zA-Z]at/g
/[0-9]at/g

/(t|T)/g
search for t OR T 

/(t|T){2,3}/g
place holder for 2 or 3 letters in a row where t and T are placed in these place holders in a row

/(re){2,3}/g
match rere or rerere

/^I/gm 
m is for multiline, looks at all lines that start with capital i

/\.$/gm
looks for lines that end with a dot

/\d{10}/g
\d is saved for digit. look for 10 digits in a row

/\d{3}-?\d{3}-?\d{4}/gm
-? means dash is optional
looks for 1234567890
and also matches 123-456-7890

/\d{3}[ -]?\d{3}[ -]?\d{4}/gm
matches numbers that have white spaces or dashes in the middle

/(\d{3})[ -]?(\d{3})[ -]?(\d{4})/gm
matches only the numbers if the number has white spaces or dashes in the middle

/(?<areacode>\d{3})[ -]?(\d{3})[ -]?(\d{4})/gm


---





