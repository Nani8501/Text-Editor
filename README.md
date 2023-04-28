# Project Documentation: Text Editor using tkinter

## Introduction
This project is a simple text editor built using the tkinter library in Python. The editor provides basic functionality like creating a new file, opening an existing file, saving the contents of the file, undo and redo operations, and a toggle-able dark mode.

## Requirements
The project has been built using Python 3.x and the following modules:

- tkinter
- filedialog

## Installation

The tkinter module is available as part of the Python standard library and hence no additional installation is required.

## Usage

To use the text editor, simply run the `TextEditor` class from the Python interpreter or a Python IDE.

## Features
### Menu bar
The text editor provides a menu bar with the following options:

- **File**
  - `New`: Creates a new file.
  - `Open`: Opens an existing file.
  - `Save`: Saves the contents of the current file.
  -` Exit`: Closes the text editor.

- **Edit**
  - `Undo`:Undoes the last operation.
  - `Redo`: Redoes the last operation.
 
-**View**
  -`Toggle Dark Mode`: Toggles the background color between white and dark grey.

### Status bar
The text editor also has a status bar which displays the number of words and lines in the file.

### Keyboard shortcuts
The following keyboard shortcuts are available:

- Ctrl + N: Creates a new file.
- Ctrl + O: Opens an existing file.
- Ctrl + S: Saves the contents of the current file.
- Ctrl + Z: Undoes the last operation.
- Ctrl + Y: Redoes the last operation.
## Limitations
The text editor is a basic implementation and has the following limitations:

- It can only handle plain text files.
- It does not support formatting or styling of text.
- It does not support searching or replacing text.
- It does not support copying or pasting text.
## Conclusion
This project provides a simple yet functional text editor using the tkinter library in Python. It can be used for basic text editing tasks and can be extended further to include more advanced functionality.





