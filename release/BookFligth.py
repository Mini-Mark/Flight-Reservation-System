#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 11, 2022 11:40:40 PM +07  platform: Windows NT

from sqlite3 import Date
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from unicodedata import name
import backend
from datetime import datetime
import BookFlight_support
from PIL import Image, ImageTk

import payment
import SearchFlight

import main


class ViewFlight_page:
    def __init__(self, Source, FlightID, Date, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (800/2))
        y_cordinate = int((screen_height/2) - (600/2))

        top.geometry(f"800x600+{x_cordinate}+{y_cordinate}")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Flight")
        top.configure(background="#64afdd")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=-0.003, rely=0.0, height=600, width=803)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(foreground="#000000")

        photo_location = Image.open("Viewflight.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(photo_location)
        self.Label1.configure(image=_img0)

        waitflightid = FlightID
        Des = backend.Flight.getFlightById(waitflightid)['name']
        waitsource = Source
        waituserid = backend.Account.getLoginUser()
        self.Button_back = tk.Button(self.top)
        self.Button_back.place(relx=0.188, rely=0.067, height=34, width=67)
        self.Button_back.configure(activebackground="#145954")
        self.Button_back.configure(activeforeground="white")
        self.Button_back.configure(activeforeground="#ffffff")
        self.Button_back.configure(background="#ffffff")
        self.Button_back.configure(compound='left')
        self.Button_back.configure(
            font="-family {Arial} -size 12 -weight bold")
        self.Button_back.configure(pady="0")
        self.Button_back.configure(text='''Back''')
        self.Button_back.configure(command=self.back)

        self.Button_book = tk.Button(self.top)
        self.Button_book.place(relx=0.575, rely=0.317, height=54, width=207)
        self.Button_book.configure(activebackground="#ffffff")
        self.Button_book.configure(activeforeground="#000000")
        self.Button_book.configure(background="#145954")
        self.Button_book.configure(compound='left')
        self.Button_book.configure(
            font="-family {Arial} -size 18 -weight bold")
        self.Button_book.configure(pady="0")
        self.Button_book.configure(text='''Book Now''')
        self.Button_book.configure(command=(backend.Book_Flight.book(
            waitsource, Des, Date, waitflightid, waituserid, 'Pending')))
        self.Button_book.configure(command=self.payment)

        self.Label_price = tk.Label(self.top)
        self.Label_price.place(relx=0.25, rely=0.35, height=21, width=148)
        self.Label_price.configure(anchor='w')
        self.Label_price.configure(background="#87bedd")
        self.Label_price.configure(compound='left')
        self.Label_price.configure(font="-family {Arial} -size 14")
        self.Label_price.configure(
            text=backend.Flight.getFlightById(waitflightid)['price'])

        self.Label_date = tk.Label(self.top)
        self.Label_date.place(relx=0.25, rely=0.4, height=21, width=148)
        self.Label_date.configure(anchor='w')
        self.Label_date.configure(background="#90bfdd")
        self.Label_date.configure(compound='left')
        self.Label_date.configure(font="-family {Arial} -size 14")
        self.Label_date.configure(text=Date)

        self.Label_totaltime = tk.Label(self.top)
        self.Label_totaltime.place(
            relx=0.394, rely=0.567, height=21, width=148)
        self.Label_totaltime.configure(background="#9ac3e5")
        self.Label_totaltime.configure(compound='left')
        self.Label_totaltime.configure(font="-family {Arial} -size 14")
        t1 = datetime.strptime(backend.Flight.getFlightById(
            waitflightid)['start'], '%H:%M')
        t2 = datetime.strptime(backend.Flight.getFlightById(
            waitflightid)['end'], '%H:%M')
        time = (t2-t1)
        time = str(time)
        datem = datetime.strptime(time, "%H:%M:%S")
        time = datem.hour, "hour", datem.minute, "minute"
        self.Label_totaltime.configure(text=time)

        self.Label_start = tk.Label(self.top)
        self.Label_start.place(relx=0.163, rely=0.667, height=21, width=148)
        self.Label_start.configure(background="#A2C5E1")
        self.Label_start.configure(compound='left')
        self.Label_start.configure(font="-family {Arial} -size 14")
        self.Label_start.configure(
            text=backend.Flight.getFlightById(waitflightid)['start'])

        self.Label_arrival = tk.Label(self.top)
        self.Label_arrival.place(relx=0.625, rely=0.667, height=21, width=148)
        self.Label_arrival.configure(background="#A2C5E1")
        self.Label_arrival.configure(compound='left')
        self.Label_arrival.configure(font="-family {Arial} -size 14")
        self.Label_arrival.configure(
            text=backend.Flight.getFlightById(waitflightid)['end'])

        self.Label_origin = tk.Label(self.top)
        self.Label_origin.place(relx=0.163, rely=0.733, height=21, width=148)
        self.Label_origin.configure(background="#A2C5E1")
        self.Label_origin.configure(compound='left')
        self.Label_origin.configure(font="-family {Arial} -size 14")
        self.Label_origin.configure(text=waitsource)

        self.Labe_destination = tk.Label(self.top)
        self.Labe_destination.place(
            relx=0.575, rely=0.733, height=21, width=240)
        self.Labe_destination.configure(background="#A2C5E1")
        self.Labe_destination.configure(compound='left')
        self.Labe_destination.configure(font="-family {Arial} -size 14")
        self.Labe_destination.configure(
            text=backend.Flight.getFlightById(waitflightid)['name'])

    def payment(self):
        main.changePage(self.top, payment.payment_page)

    def back(self):
        main.changePage(self.top, SearchFlight.search_page)


def start_up():
    BookFlight_support.main()


if __name__ == '__main__':
    BookFlight_support.main()
