**Sessions** - top most layer in tmux and are a collection of one or more windows managed as a single unit.
We can have any number of sessions open at one time but typically only attached to one, each session has a single active window.
**Windows** - Windows are a container to one or more panes . We can think of windows as tabs in browsers or other software. Each window has a currently active pane and it allows us to switch between them.
At the bottom right of the screen in the Window, it marks which pane is currently active with an Asterisk.
**Panes** - panes are splits in the window and represent individual terminal session. There will only be one active pane at a time that we interact with. 

**PREFIX KEY**
Key combination that we use before the actual command itself. The default prefix is `ctrl + b`.
To create a new window, we press the prefix followed by the `c` key; as well as creating the new window this command will also set it as your current active window for the session. 
To change between windows, we pass the prefix and the window number which is shown at the bottom; or we can rotate between the windows using the prefix followed by either `p` or `n` keys which stand for previous and next respectively.

We can also move windows around by using the swap window command which is done by pressing the prefix and then entering the command which starts with a colon. 

To close a window, you can either kill all the panes inside or use the prefix followed by the `&`symbol.

There are also a number of commands to manage panes in tmux. We can split a window into panes either horizontally or vertically. 
To split a window horizontally we use the prefix followed by the `%` symbol, which will split our current pane into two.
To split a window vertically we use the prefix followed by the `"` (quotation mark) symbol.