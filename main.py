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


def render_menu(y=0, x=0, height_fraction=0, width_fraction=0, title='', border=True):
    global screen, WIDTH, HEIGHT

    window_width = int(WIDTH * width_fraction)
    window_height = int(HEIGHT * height_fraction)
    window = curses.newwin(window_height, window_width, y, x)
    if border:
        window.border()

    padding = (window_width - len(title) - 2) // 2
    if padding * 2 + len(title) + 2 < window_width:
        window.addstr(1, 1, (padding * ' ') + title + (padding + 1) * ' ', curses.A_UNDERLINE)
    else:
        window.addstr(1, 1, (padding * ' ') + title + padding * ' ', curses.A_UNDERLINE)
    window.refresh()
    return window


# TODO: render_menu() absolute width/height


def main(local_screen):
    global screen, WIDTH, HEIGHT
    screen = local_screen

    setup()

    sidebar_window = render_menu(y=0, x=0, height_fraction=1, width_fraction=1 / 6, title='SIDEBAR', border=True)
    feed_window = render_menu(y=HEIGHT // 15, x=WIDTH // 6, height_fraction=14 // 15, width_fraction=5 / 6, title='FEED', border=True)

    search_bar = curses.newwin(HEIGHT // 15, WIDTH * 5 // 6, 0, WIDTH // 6)
    search_bar.border()
    search_bar.addstr(1, 1, 'Search: ')
    search_bar.refresh()

    sidebar_text = ['Subscriptions', 'Watch later', 'Playlist A', 'Playlist B', 'Playlist C']
    for i, text in enumerate(sidebar_text):
        sidebar_window.addstr(2 + i, 1, text)
    sidebar_window.addstr(HEIGHT - 2, 1, '⚙ Settings')
    sidebar_window.refresh()

    videos = [['Video A title', 'Creator A', 1337],
              ['Video B title', 'Creator B', 10000],
              ['Video C title', 'Creator C', 345]]
    feed_window_height, feed_window_width = feed_window.getmaxyx()
    for i, video in enumerate(videos):
        string = video[0][:15] + '\t\t\t' + video[1][:15] + '\t\t\t👍' + str(video[2])
        feed_window.addstr(2 + i, 1, string)
    feed_window.refresh()

    screen.getch()


if __name__ == '__main__':
    wrapper(main)
