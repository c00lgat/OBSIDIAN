Error handling
By default, bash does `set +e`
`set -e` on the other hand, tells bash to stop the script if an exit code different than 0 is received by one of the commands.

echo "anan" > /dev/null
Takes the output of left side to the right side. We are not writing inside a file, but rather, if the command returns an error, it redirects the stderror to the /dev/null path instead of displaying it to the terminal.

![[Pasted image 20240319182614.png]]
 https://github.com/nirsht/DevOpsCourseINT2024/blob/main/Tutorials/Linux/5_bash_and_other_shells.md

`env` in the terminal is going to print all of the current environment variables.
`printenv` does the same thing.

`export` allows us to set an environment variable.
`export TEMP=2`
`echo $TEMP` is going to print the value of the `TEMP` environment variable.
Underscores, lowercases and numbers are allowed into the environment variables. `export TEMP2_` for example.

To remove an environment variable, run the `unset` command: `unset TEMP` is going to remove `TEMP` as an environment variable. 

In order to have the environment variable available for all future sessions of the terminal, we have to add it to the `./bashrc` file.

`$PATH` - specifies the directories in which the shell looks for executable files. It is a colon-separated list of directories (e.g., /usr/bin:/bin:/usr/local/bin)
