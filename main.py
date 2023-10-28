#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("D&D Quest Tracker")
root.geometry("640x512")


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

# scrollbar def
sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)


root.config(menu=menuBar)
root.mainloop()
