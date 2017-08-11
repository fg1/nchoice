# nchoice

``nchoice`` is a small python program and library using ncurses to ask the user for a question. This script is useful for building other scripts.

![Recording of nchoice](https://raw.githubusercontent.com/fg1/nchoice/master/data/nchoice-recording.gif)

## Installation

From Github:

    $ pip install --upgrade https://github.com/fg1/nchoice/archive/master.tar.gz

## Usage

From the command line:

    usage: nchoice [-h] [-Q QUESTION] [-A] C [C ...]

    positional arguments:
      C            List of choices to ask for

      optional arguments:
        -h, --help   show this help message and exit
        -Q QUESTION  Add a question on top of the list of choices
        -A           Returns the choice itself instead of its index


In a script:

    from nchoice import ask_choice
    ask_choice(['Option 1', 'Option 2', 'Option 3'], 'Please make a choice:')

