https://youtu.be/DzNmUNvnB04?si=uSMnIP0OQTr2hYxF
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

To *close a window*, you can either kill all the panes inside or use the prefix followed by the `&`symbol.

There are also a number of commands to manage panes in tmux. We can split a window into panes either horizontally or vertically. 
To *split a window horizontally* we use the prefix followed by the `%` symbol, which will split our current pane into two.
To *split a window vertically* we use the prefix followed by the `"` (quotation mark) symbol.

Panes can be *navigated* by using the prefix along with one of the arrow keys.

We can also *swap panes* by using the prefix followed by the left or right brace symbol `{}`.

Panes also have numbers which we can toggle by using the prefix followed by `q`. And then we can select a pane by pressing the subsequent number once prompted.

One of the useful features is *zooming into a pane* to make it take up the full window. This can be done using the prefix followed by the `z` key.

Additionally we can *turn a pane into a window* by using the prefix followed by an exclamation point `!`. 

To close a pane, we can either close the shell that is running or use the prefix followed by the `x` key.

As well as panes and windows, we should also cover sessions. 
Sessions can be created by using the tmux command 