#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("D&D Quest Tracker")
root.geometry("640x512")
root.resizable(width=False, height=False)


# quest menu functions
def add_quest():
    return


def add_detailed_quest():
    return


def view_deleted_quests():
    return


# help menu segments
def help_menu_help():
    messagebox.showinfo("Help", "You don't need any help.\nBe self reliant for once, it's really not that hard.")


def help_menu_about():
    messagebox.showinfo("About", "D&D Quest Tracker \nVersion 1.00\nEricSoft™")


# menubar segment
menuBar = Menu(root)
# quest menu segment
questMenu = Menu(menuBar, tearoff=0)
questMenu.add_command(label="Add Basic Quest", command=add_quest)
questMenu.add_command(label="Add Detailed Quest", command=add_detailed_quest)
questMenu.add_command(label="View Deleted Quests", command=view_deleted_quests)
questMenu.add_separator()
questMenu.add_command(label="Exit", command=root.destroy)
menuBar.add_cascade(label="Quests", menu=questMenu)

# help menu segment
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=help_menu_about)
helpMenu.add_command(label="Help", command=help_menu_help)
menuBar.add_cascade(label="Help", menu=helpMenu)

# Scrollbar Segment
# Create a main frame
mf = Frame(root)
mf.pack(fill=BOTH, expand=1)
# Create a canvas
canvas = Canvas(mf)
canvas.pack(side=LEFT, fill=BOTH, expand=1)
# Add a scrollbar to the canvas
sb = ttk.Scrollbar(mf, orient=VERTICAL, command=canvas.yview)
sb.pack(side=RIGHT, fill=Y)
# configure the canvas
canvas.configure(yscrollcommand=sb.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
# create another frame inside canvas
second_frame = Frame(canvas)    # When adding an item to the scrollbar add it to the second frame
# add new frame to a window in the canvas
canvas.create_window((0, 0), window=second_frame, anchor="nw")

# This is the button that is always there on first load to guide quest creation
Button(second_frame, text="Add A Basic Quest").pack()

root.config(menu=menuBar)
root.mainloop()
