#!/usr/bin/python

import curses
import sys
import time

if len(sys.argv) != 2:
    print "Usage:"
    print "    python miniwriter.py <filename to write to>"
    quit()

stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.keypad(1)

try:
    stdscr.refresh()
    x = 0
    while True: 
        key = stdscr.getch()
        if key == curses.KEY_BACKSPACE or key == curses.KEY_DC:
            stdscr.delch(0,x-1) 
            x -= 1
        elif key == ord(' '):
            x = 0
            word = stdscr.instr(0,0).rstrip()
            with open(sys.argv[1], "a") as text_file:
                text_file.write(word + " ")
            stdscr.clear()
        elif key == curses.KEY_ENTER or key == curses.KEY_EOL or key == 10:
            x = 0
            word = stdscr.instr(0,0).rstrip()
            with open(sys.argv[1], "a") as text_file:
                text_file.write(word + "\n")
            stdscr.clear()
        else:
            stdscr.addch(0,x,key)
            x += 1
 
        stdscr.refresh()

finally:
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()
