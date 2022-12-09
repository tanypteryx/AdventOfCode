import curses
from curses import wrapper
import time

def init_screen():
    return curses.initscr()

def update_screen(scr, stacks):
    scr.clear()
    [scr.addstr(58,35+3*i,f' {i} ',curses.A_BOLD) for i in range(1,10)]
    for ii in range(9):
        tmp = stacks[ii]
        for jj in range(len(tmp)):
            scr.addstr(57-jj,38+3*ii,f'[{tmp[jj]}]')
            if jj > 55: 
                break
    scr.refresh()
    time.sleep(0.1)
    #scr.getch()

def end_screen():
    curses.endwin()
