#!/usr/bin/env python

import curses
from curses import wrapper
from math import floor

screen = None
WIDTH, HEIGHT = 0, 0


def setup():
    global screen, WIDTH, HEIGHT

    curses.use_default_colors()
    curses.curs_set(0)
    screen.erase()
    screen.refresh()
    HEIGHT, WIDTH = screen.getmaxyx()


def render_sidebar(y=0, x=0):
    global screen, WIDTH, HEIGHT

    sidebar_width = floor((WIDTH // 7) / 2) * 2
    sidebar_win = curses.newwin(HEIGHT, sidebar_width, y, x)
    sidebar_win.border()

    title = 'SIDEBAR'
    padding = (sidebar_width - len(title) - 2) // 2
    if padding * 2 + len(title) + 2 < sidebar_width:
        sidebar_win.addstr(y + 1, x + 1, padding * ' ' + title + (padding + 1) * ' ', curses.A_UNDERLINE)
    else:
        sidebar_win.addstr(y + 1, x + 1, padding * ' ' + title + padding * ' ', curses.A_UNDERLINE)
    sidebar_win.refresh()
    return sidebar_width, HEIGHT


def render_feed(y=0, x=0):
    global screen, WIDTH, HEIGHT

    feed_width = floor((5 * WIDTH // 7) / 2) * 2
    feed_win = curses.newwin(HEIGHT, feed_width, y, x)
    feed_win.border()

    title = 'FEED'
    padding = (feed_width - len(title) - 2) // 2
    if padding * 2 + len(title) + 2 < feed_width:
        feed_win.addstr(y + 1, x + 1, padding * ' ' + title + (padding + 1) * ' ', curses.A_UNDERLINE)
    else:
        feed_win.addstr(y + 1, x + 1, padding * ' ' + title + padding * ' ', curses.A_UNDERLINE)
    feed_win.refresh()
    return feed_width, HEIGHT


def main(local_screen):
    global screen, WIDTH, HEIGHT
    screen = local_screen

    setup()

    # back_win = curses.newwin(HEIGHT, WIDTH, 0, 0)
    # back_win.border()
    # back_win.refresh()

    sidebar_width, sidebar_height = render_sidebar()
    feed_width, feed_height = render_feed(0, sidebar_width + 1)

    screen.getch()


if __name__ == '__main__':
    wrapper(main)
