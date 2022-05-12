#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 12, 2022 12:27:49 AM +07  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from unicodedata import name
from datetime import datetime

import main
import login
import backend
from tkinter import messagebox

import register_support

from PIL import Image, ImageTk
def changePage(oldpage,newpage):
        oldpage.destroy()
        root = tk.Tk()
        newpage(root)

class Register_page:
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (800/2))
        y_cordinate = int((screen_height/2) - (600/2))

        top.geometry(f"800x600+{x_cordinate}+{y_cordinate}")
        # top.geometry("800x600+601+203")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Register")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=-0.004, rely=0.0, height=600, width=803)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = Image.open("register.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(text='''bg''')


        self.Entry_ID = tk.Entry(self.top)
        self.Entry_ID.place(relx=0.138, rely=0.267, height=20, relwidth=0.443)
        self.Entry_ID.configure(background="white")
        self.Entry_ID.configure(disabledforeground="#a3a3a3")
        self.Entry_ID.configure(font="TkFixedFont")
        self.Entry_ID.configure(foreground="#000000")
        self.Entry_ID.configure(insertbackground="black")

        self.Entry_phone = tk.Entry(self.top)
        self.Entry_phone.place(relx=0.138, rely=0.367, height=20, relwidth=0.443)
        self.Entry_phone.configure(background="white")
        self.Entry_phone.configure(disabledforeground="#a3a3a3")
        self.Entry_phone.configure(font="TkFixedFont")
        self.Entry_phone.configure(foreground="#000000")
        self.Entry_phone.configure(insertbackground="black")

        self.Entry_user = tk.Entry(self.top)
        self.Entry_user.place(relx=0.138, rely=0.483, height=20, relwidth=0.443)
        self.Entry_user.configure(background="white")
        self.Entry_user.configure(disabledforeground="#a3a3a3")
        self.Entry_user.configure(font="TkFixedFont")
        self.Entry_user.configure(foreground="#000000")
        self.Entry_user.configure(insertbackground="black")

        # self.Entry_ID = tk.Entry(self.top)
        # self.Entry_ID.place(relx=0.138, rely=0.267, height=20, relwidth=0.443)
        # self.Entry_ID.configure(background="white")
        # self.Entry_ID.configure(disabledforeground="#a3a3a3")
        # self.Entry_ID.configure(font="TkFixedFont")
        # self.Entry_ID.configure(foreground="#000000")
        # self.Entry_ID.configure(insertbackground="black")

        self.Entry_pass = tk.Entry(self.top)
        self.Entry_pass.place(relx=0.138, rely=0.6, height=20, relwidth=0.443)
        self.Entry_pass.configure(background="white")
        self.Entry_pass.configure(disabledforeground="#a3a3a3")
        self.Entry_pass.configure(font="TkFixedFont")
        self.Entry_pass.configure(foreground="#000000")
        self.Entry_pass.configure(insertbackground="black")
        self.Entry_pass.configure(show="*")

        self.Entry_confirmpass = tk.Entry(self.top)
        self.Entry_confirmpass.place(relx=0.138, rely=0.717, height=20
                , relwidth=0.443)
        self.Entry_confirmpass.configure(background="white")
        self.Entry_confirmpass.configure(disabledforeground="#a3a3a3")
        self.Entry_confirmpass.configure(font="TkFixedFont")
        self.Entry_confirmpass.configure(foreground="#000000")
        self.Entry_confirmpass.configure(insertbackground="black")
        self.Entry_confirmpass.configure(show="*")

        self.Button_register = tk.Button(self.top)
        self.Button_register.place(relx=0.175, rely=0.8, height=54, width=287)
        self.Button_register.configure(activebackground="#ffffff")
        self.Button_register.configure(activeforeground="#d4b1c2")
        self.Button_register.configure(background="#d4b1c2")
        self.Button_register.configure(compound='left')
        self.Button_register.configure(disabledforeground="#a3a3a3")
        self.Button_register.configure(font="-family {Arial} -size 17 -weight bold")
        self.Button_register.configure(foreground="#ffffff")
        self.Button_register.configure(highlightbackground="#d9d9d9")
        self.Button_register.configure(highlightcolor="black")
        self.Button_register.configure(pady="0")
        self.Button_register.configure(relief="flat")
        self.Button_register.configure(text='''Register''')
        self.Button_register.configure(command=self.register)

        self.Button_back = tk.Button(self.top)
        self.Button_back.place(relx=0.063, rely=0.067, height=44, width=47)
        self.Button_back.configure(activebackground="#ececec")
        self.Button_back.configure(activeforeground="#000000")
        self.Button_back.configure(background="#d9d9d9")
        self.Button_back.configure(compound='left')
        self.Button_back.configure(disabledforeground="#a3a3a3")
        self.Button_back.configure(foreground="#000000")
        self.Button_back.configure(highlightbackground="#d9d9d9")
        self.Button_back.configure(highlightcolor="black")
        self.Button_back.configure(pady="0")
        self.Button_back.configure(text='''Back''')
        self.Button_back.configure(command=self.back)


    def back(self):
        main.changePage(self.top,login.Login_page)
        
    def register(self):
        id_card = self.Entry_ID.get()
        phone = self.Entry_phone.get()
        username = self.Entry_user.get()
        password = self.Entry_pass.get()
        repassword = self.Entry_confirmpass.get()
        if (id_card == "" or phone == "" or username == "" or password == "" or repassword == ""):
            messagebox.showerror("EROR", "Please input all field")
            return False
        
        if(password != repassword):
            messagebox.showerror("ERROR", "Password and repassword have something wrong")
            return False
        else:
            user = backend.Account().register(username,password,id_card,phone)
            
            if(user != False):
                messagebox.showinfo("SUCCESS","Register Success !!!")
                changePage(self.top)
            else:
                messagebox.showerror("ERROR", "Data have something wrong can't create new user")
                return False


def start_up():
    register_support.main()

if __name__ == '__main__':
    register_support.main()



