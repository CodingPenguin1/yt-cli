#!/usr/bin/env python

import curses
from curses import wrapper
from time import sleep


def main(screen):
    curses.use_default_colors()

    screen.clear()
    screen.refresh()
    screen.getch()


if __name__ == '__main__':
    wrapper(main)
