Error handling
By default, bash does `set +e`
`set -e` on the other hand, tells bash to stop the script if an exit code different than 0 is received by one of the commands.

echo "anan" > /dev/null
Takes the output of left side to the right side. We are not writing inside a file, but rather, if the command returns an error, it redirects the stderror to the /dev/null path instead of displaying it to the terminal.

![[Pasted image 20240319182614.png]]
