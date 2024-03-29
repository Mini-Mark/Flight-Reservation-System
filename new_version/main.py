#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 12, 2022 12:07:39 AM +07  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import main
import login

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = login.Login_page(_top1)
    root.mainloop()
    
def changePage(oldpage,newpage):
    oldpage.destroy()
    root = tk.Tk()
    newpage(root)
    
if __name__ == '__main__':
    main()




