#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 12, 2022 12:07:35 AM +07  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from unicodedata import name
from datetime import datetime

import main
import backend
import login_support
from tkinter import messagebox
from PIL import Image, ImageTk
import searchGUI

import register


class Login_page:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("800x600+672+197")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Login")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=-0.003, rely=0.0, height=600, width=803)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        photo_location = Image.open("Login.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(photo_location)
        self.Label1.configure(image=_img0)

        self.Entry_user = tk.Entry(self.top)
        self.Entry_user.place(relx=0.313, rely=0.317, height=20, relwidth=0.38)
        self.Entry_user.configure(background="white")
        self.Entry_user.configure(font="TkFixedFont")
        self.Entry_user.configure(insertbackground="black")

        self.Entry_pass = tk.Entry(self.top)
        self.Entry_pass.place(relx=0.313, rely=0.483, height=20, relwidth=0.38)
        self.Entry_pass.configure(background="white")
        self.Entry_pass.configure(font="TkFixedFont")
        self.Entry_pass.configure(insertbackground="black")
        self.Entry_pass.configure(show="*")

        self.Button_login = tk.Button(self.top)
        self.Button_login.place(relx=0.313, rely=0.567,
                                height=44, relwidth=0.38)
        self.Button_login.configure(activebackground="#376D8A")
        self.Button_login.configure(activeforeground="#ffffff")
        self.Button_login.configure(background="#ffffff")
        self.Button_login.configure(compound='left')
        self.Button_login.configure(
            font="-family {Arial} -size 17 -weight bold")
        self.Button_login.configure(foreground="#5792b2")
        self.Button_login.configure(pady="0")
        self.Button_login.configure(text='''Login''')
        self.Button_login.configure(command=self.login)
        self.Button_login.configure(highlightthickness=0, bd=0)

        self.Button_register = tk.Button(self.top)
        self.Button_register.place(
            relx=0.313, rely=0.66, height=44, relwidth=0.38)
        self.Button_register.configure(activebackground="#376D8A")
        self.Button_register.configure(activeforeground="#E0E0E0")
        self.Button_register.configure(background="#ffffff")
        self.Button_register.configure(compound='left')
        self.Button_register.configure(
            font="-family {Arial} -size 17 -weight bold")
        self.Button_register.configure(foreground="#5792b2")
        self.Button_register.configure(pady="0")
        self.Button_register.configure(text='''Register''')
        self.Button_register.configure(command=self.register)
        self.Button_register.configure(highlightthickness=0, bd=0)

        self.Button_guest = tk.Button(self.top)
        self.Button_guest.place(
            relx=0.313, rely=0.753, height=44, relwidth=0.38)
        self.Button_guest.configure(activebackground="#376D8A")
        self.Button_guest.configure(activeforeground="#E0E0E0")
        self.Button_guest.configure(background="#ffffff")
        self.Button_guest.configure(compound='left')
        self.Button_guest.configure(
            font="-family {Arial} -size 17 -weight bold")
        self.Button_guest.configure(foreground="#5792b2")
        self.Button_guest.configure(pady="0")
        self.Button_guest.configure(text='''Guest''')
        self.Button_guest.configure(command=self.guest)
        self.Button_guest.configure(highlightthickness=0, bd=0)

    def login(self):
        user = backend.Account().login(self.Entry_user.get(), self.Entry_pass.get())

        if(user != False):
            messagebox.showinfo("SUCCESS", "Login Success !!")
            main.changePage(self.top, searchGUI.search_page)
        else:
            messagebox.showerror(
                "ERROR", "Username or password have something wrong!")

    def register(self):
        main.changePage(self.top, register.Register_page)
        
    def guest(self):
        main.changePage(self.top, searchGUI.search_page)
