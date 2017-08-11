#!/usr/bin/env python3
# coding: utf-8

import curses


def ask_choice(choices, question=None):
    scr = curses.initscr()
    y, x = scr.getmaxyx()
    curses.noecho()
    curses.curs_set(0)
    scr.keypad(1)

    nchoices = len(choices)
    position = 0
    offset = 0

    def refresh_opts(position):
        k = 0
        if question != None:
            scr.addstr(0, 0, question[:x], curses.A_BOLD)
            k += 1
        for i in xrange(offset, nchoices):
            o = choices[i]
            if len(o) < x:
                o += ' ' * (x - len(o))
            else:
                o = o[:x - 1] + '-'
            if i == position:
                scr.addstr(k, 0, o, curses.A_REVERSE)
            else:
                scr.addstr(k, 0, o)
            k += 1
            if k == y - 1:
                break
        scr.refresh()

    def scroll(position, offset, n):
        position = max(0, min(nchoices - 1, position + n))
        if question != None and position >= y - 2:
            offset = max(0, min(nchoices - y + 2, offset + n))
        elif position - offset >= y - 1:
            offset = max(0, min(nchoices - y + 1, offset + n))
        elif position - offset < 0:
            offset = position
        return position, offset

    refresh_opts(position)

    KEY_g = ord('g')
    KEY_G = ord('G')
    KEY_q = ord('q')
    while 1:
        c = scr.getch()
        if c == curses.KEY_RESIZE:
            y, x = scr.getmaxyx()
            if question != None and offset + position > y - 2:
                offset = min(nchoices - y + 3, position - y + 3)
            elif offset + position > y - 1:
                offset = min(nchoices - y + 2, position - y + 2)
            else:
                offset = 0
        elif c == curses.KEY_UP:
            position, offset = scroll(position, offset, -1)
        elif c == curses.KEY_PPAGE:
            position, offset = scroll(position, offset, -5)
        elif c == curses.KEY_DOWN:
            position, offset = scroll(position, offset, 1)
        elif c == curses.KEY_NPAGE:
            position, offset = scroll(position, offset, 5)
        elif c in [10, 13, curses.KEY_ENTER]:
            break
        elif c == KEY_g:
            position, offset = (0, 0)
        elif c == KEY_G:
            position, offset = scroll(position, offset, nchoices - 1)
        elif c == KEY_q:
            position = -1
            break

        scr.erase()
        refresh_opts(position)

    curses.endwin()
    return position


def main():
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('choices', metavar='C', nargs='+', type=str, help='List of choices to ask for')
    parser.add_argument('-Q', dest='question', type=str, help='Add a question on top of the list of choices')
    parser.add_argument('-A', dest='output_arg', action='store_true', help='Returns the choice itself instead of its index')
    args = parser.parse_args()

    position = ask_choice(args.choices, args.question)
    if position == -1:
        sys.exit(1)

    if args.output_arg:
        print(args.choices[position])
    else:
        print(position)


if __name__ == "__main__":
    main()
