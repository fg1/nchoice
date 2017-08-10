=======
nchoice
=======

``nchoice`` is a small python program and library using ncurses to ask the user for a question. This script is useful for building other scripts.

![Recording of nchoice](https://raw.githubusercontent.com/fg1/nchoice/master/data/nchoice-recording.gif)

Installation
============

From Github:

.. code-block:: shell

    $ pip install --upgrade https://github.com/fg1/nchoice/archive/master.tar.gz

Usage
=====

.. code-block:: shell

   usage: nchoice [-h] [-Q QUESTION] [-A] C [C ...]

   positional arguments:
     C            List of choices to ask for

     optional arguments:
       -h, --help   show this help message and exit
       -Q QUESTION  Add a question on top of the list of choices
       -A           Returns the choice itself instead of its index

