**Task Description:**

1. Open a terminal and create a new file named `vim_practice.txt`.
2. Write the following text in the file:
	Hello, this is a Vim practice file.

Please edit this file using Vim to complete the tasks below.

3. Save and close the file.
	- `ESC + :wq`

4. Reopen the `vim_practice.txt` file in Vim.
5. Use the following commands to perform the tasks:

- Move the cursor to the end of the first line.
	- `gg + $`
- Insert a new line below the first line and add the text: "This is task 1."
	- `o`
- Move the cursor to the end of the second line.
	- `$`
- Insert a new line below the second line and add the text: "This is task 2."
	- `o`
- Move the cursor to the end of the third line.
	- `$`
- Insert a new line below the third line and add the text: "This is task 3."
	-  `o`
- Move the cursor to the beginning of the file.
	- `gg`
- Search for the text "task 2" and replace it with "second task".
	- `:/task 2 + ENTER + n` Searches for task 2
	- `:%s/task 2/second task/g`
- Move the cursor to the end of the file.
	- `G`
- Append the following text at the end of the file: "Congratulations! You have completed the Vim practice tasks."
	- `a`
- Save the file and exit Vim.
	- `:wq`

