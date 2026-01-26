#linux/tools #vim 

## Normal Mode

### Movement

`h` -> move to left
`j` -> move to down
`k` -> move to up
`l` -> move to right
`gg` -> go to the first line of the file
`Shift + g` -> Jumps the cursor to the very last line of the file
`{Line Number} + Shift + G` -> Jumps to a specific line. Example: Typing `40G` takes you directly to line 40
`Shift + h` -> Move cursor to the High (top) of the current screen
`Shift + m` -> Move cursor to the middle of the current screen
`Shift + l` -> Move cursor to the low (bottom) of the current screen
`0` -> Move cursor to the **start** of the current line
`$` -> Move cursor to the **end** of the current line
`CTRL + f` -> Page down
`CTRL + b` -> Page up

### Deleting

`x` -> Delete a unique character
`dd` -> Delete the whole line

### Undo/Redo

`u` -> undo an action
`CTRL + r` -> redo an action

### Copy/Paste

`yy` -> "yank" (copy) a line
`yiw` -> it copies the word of where your cursor is positioned inside it (at the start, middle, or end)
`yaw` -> it copies the current word + trailing space
`diw` -> it deletes the current word
`ciw` -> Change current word (deletes it and drops you into Insert Mode)
`p` -> paste it (you need to copy first with one of the previous commands)

## Insert Mode
Press `i` to enter on Insert mode and type the text you want. To navigate through the file use the arrow keys

## Command-Line Mode
`:w` -> Write (save) the file
`:q` -> Quit VIM
`:wq` -> Write (save) the file and quit from VIM
`:q!` -> Quit without saving changes
`:%s/old/new/g` -> Find and replace all instances of "old" with "new"