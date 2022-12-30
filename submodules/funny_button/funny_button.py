# -*- coding: utf-8 -*-


W = "Vijay Khalate"

from tkinter import *
from random import *


def do_event(event):
    print("{},{}".format(event.x,event.y))


def fix_limits(value):  # Avoid button position outside of window
    offset = 0.03
    if value == 0:
        value = value + offset
    if value == 1:
        value = value - offset
    return value


def jump(event):
    app.hello_b.place(relx=fix_limits(random()), rely=fix_limits(random()))


class App:
    def __init__(self,master):
        frame = Frame(master)
        master.geometry("250x250")
        master.title("Funny Button")
        master.bind("<Button-1>",do_event)
        master.bind("<Button-1>",do_event)
        frame.pack()

        self.hello_b = Button(master, text="Quit", command=sys.exit)
        self.hello_b.bind("<Enter>", jump)
        self.hello_b.pack()


root = Tk()

app = App(root)

root.mainloop()
