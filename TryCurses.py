import curses
import curses.textpad
import time

stdscr = curses.initscr()

def draw_background_window():
    begin_x = 0
    begin_y = 0
    height,width = stdscr.getmaxyx()
    win = curses.newwin(height, width, begin_y, begin_x)
    win.box()
    stdscr.refresh()
    win.refresh()
    helper_window()
    command_windows()
    
def helper_window():
    max_y,max_x = stdscr.getmaxyx()
    begin_x = max_x - max_x // 3
    begin_y = 0
    height = max_y - max_y // 5
    width = max_x // 3
    helper_win = curses.newwin(height, width, begin_y, begin_x)
    helper_win.box()
    text_y, text_x  = helper_win.getmaxyx()
    text_x = text_x // 5 
    text_y = text_y // 12 
    helper_win.addstr(text_y,text_x,"Enabled commands: ")
    stdscr.refresh()
    helper_win.refresh()

def command_windows():
    max_y,max_x = stdscr.getmaxyx()
    begin_x = 0
    begin_y = max_y - max_y // 5
    height = max_y // 5
    width = max_x
    command_win = curses.newwin(height, width, begin_y, begin_x)
    command_win.box()
    stdscr.refresh()
    command_win.refresh()
    enter_text(command_win)
    
def enter_text(window):
    #tb = curses.textpad.Textbox(windows)
    #command = tb.edit()
    #curses.addstr(1,1,command.encode('utf_8'))
    text_y, text_x  = window.getmaxyx()
    text_x = text_x // 20 
    text_y = text_y // 2 
    window.addstr(text_y,text_x,"Enter command: ")
    window.getch()
    
#curses.noecho()
#curses.echo()

draw_background_window()


