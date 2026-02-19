#linux/tools #concepts #vim 

## The VIM Modes

VIM has three more often used modes (there are others too, but those are more useful) They are:
* Normal Mode
* Insert Mode
* Line Mode (Command Line Mode)

### Normal Mode

When you enter on VIM editor, you're in the normal mode. In this mode you **CAN'T** write anything. In this mode, the keys are commands. In other words, this mode is useful to edit existing texts or moving through the file. Check the keybindings below
[[VIM keybindings#Normal Mode|Normal Mode Keybindings]]

**OBS:** If you're in another mode, to return to normal mode you press ESC.

### Insert Mode

This is the mode where VIM acts like a regular editor. In this mode, when you press a key, it writes in the file as normal editor. This is the mode you must use to write code, for example. When you're in this mode, you'll see `--INSERT--` at the bottom left of your terminal.  Check the keybindings here:
[[VIM keybindings#Insert Mode|Insert Mode Keybindings]]

**OBS:** From Normal Mode, press `i` (to insert before the cursor position) or `a` (to append after the cursor position). To leave out this mode, press *ESC*. You should always return to the Normal Mode as soon as you finish writing

### Command-Line Mode

This is a "big-picture" mode where you make things like saving files, quitting from VIM, performing search and replacing operations and stuff like that. Check the shortcuts below
[[VIM keybindings#Command-Line Mode|Command-Line Keybindings]]

**OBS:** You need to press `:` to enter on command-line mode

### Navigating tips
You can use this file to practice navigating  
  
To move down a line, press "j"  
  
To move up a line, press "k"  
  
To move to the right, press "l"  
  
To move to the left, press "h"  
  
You can also press and hold a navigation key so that it repeats.  
  
To move all the way to the top of the file, press and hold "k".  
To move all the way to the bottom of the file, press and hold "j"  
  
To move forward in the file, use CTRL+f to page down and CTRL+b to page up