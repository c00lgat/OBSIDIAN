awk '{print $1}' 
print the first column

awk '{print $0}' == awk '{print}'
print everything

awk -F ":" '{print $1}'
-F is field separator

awk -F ":" '{print $1 $6 $7}'
removes the : from the lines while printing the columns

awk -F ":" '{print $1"\\t"$6"\\t"$7}'
adds tab in between columns

FS = field separator
fills in the separators with a char of our choice

awk -F "/" '/^\//' {print $NF} /path/
looks for every line that starts with a slash
and prints the last field of each line


df | awk '/\/dev\/loop / {print $1}'


we could also do math between columns

awk 'length($0) > 7'
returns lines that have length greater than 7

ps -ef | awk '{ if($NF == "/bin/fish") print$0}'
looks for all processes that are running the fish process

awk 'BEGIN { for(i=1; i<=10; i++) print "The square root of ", i, "is", i\*i;}'

awk '{print substr($0, 4)}'
ignores until the fourth char and starts printing from there

file:///C:/Users/Anan/Downloads/Dougherty,%20Dale%20_%20Robbins,%20Arnold%20-%20sed%20&%20awk%20(2010,%20O'Reilly%20Media)%20-%20libgen.li.pdf

https://www.cs.unibo.it/~renzo/doc/awk/nawkA4.pdf

---
https://www.youtube.com/watch?v=oPEnvuj9QrI
How does AWK work?
We can use awk to create filters to write scrips to accept data from standard input, change it someway and then send it back through standard output in this changed form.

Usually, the standard input is a text file and the standard output is typically our screen.

The text file that we will be working with is called `tmnt.txt` which contains the following text:
`leonardo blue leader`
`raphael red hothead`
`michelangelo orange party-animal`
`donatello purple geek`

We have their names, bandana color and their personality. 

By default, awk sees spaces as delimiters for fields. If awk assumes that each space is the delimiter for each field then, we can conclude that field number one is their names, field number two is their bandana color and field number three is their personality/role.

`awk 'command' file.txt`

