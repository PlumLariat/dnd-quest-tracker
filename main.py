#!/usr/bin/env python

# external libs
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
import logging
from PIL import ImageTk, Image

# self created libs
from Quest import Quest

root = Tk()
root.title("D&D Quest Tracker")
icon = PhotoImage(file='./assets/dragon-head.png')
root.iconphoto(True, icon)
root.geometry("640x512")
root.resizable(width=False, height=False)
log = logging.getLogger("quest-tracker")
logging.basicConfig(level=logging.DEBUG)

active_quests = []


# quest menu functions
def add_quest_button_clicked(quest_title, quest_disc, quest_obj, is_basic_quest):
    if is_basic_quest:

        if quest_title == "peener":
            global img
            top = Toplevel()
            top.title("suprise!")
            img = ImageTk.PhotoImage(Image.open(r'./assets/other-head.png'))
            Label(top, image=img).pack()
            return

        log.debug("Title: " + quest_title)
        log.debug("Quest Disc: " + quest_disc)
        log.debug("Objectives: " + str(quest_obj))
        created_quest = Quest(quest_title, quest_disc, quest_obj)
        active_quests.insert(0, created_quest)

        log.info(str(active_quests))

    # else should be activated if the request came from a detailed quest
    else:
        messagebox.showerror("What", "How did you even get here?")


def add_quest():

    def add_objective_button_clicked():
        quest_objectives_combo['values'] += (quest_objectives_entry.get(), )
        quest_objectives.append(quest_objectives_entry.get())
        quest_objectives_entry.delete(0, END)

    # absolute unresolved chicanery
    # global quest_title
    # global quest_description
    # global quest_objectives

    is_basic_quest = True

    top = Toplevel()
    top.resizable(width=False, height=False)
    top.title('Add A Basic Quest')
    top.iconphoto(True, icon)

    add_quest_frame = Frame(top)
    add_quest_frame.pack()

    quest_title_frame = LabelFrame(add_quest_frame, text="Quest Title")
    quest_title_frame.grid(row=0, column=0)
    quest_title_label = Label(quest_title_frame, text="Title:")
    quest_title_label.grid(row=0, column=0)
    quest_title_entry = Entry(quest_title_frame, width=60)
    quest_title_entry.grid(row=0, column=1)

    quest_description_frame = LabelFrame(add_quest_frame, text="Description:")
    quest_description_frame.grid(row=1, column=0)
    quest_description_text = Text(quest_description_frame, width=60, height=10)
    quest_description_text.grid(row=2, column=0)

    # =OBJECTIVES=SECTION===============================================================================================
    quest_objectives = ['obj1', 'obj2', 'obj3']
    selection = StringVar()
    quest_objectives_frame = LabelFrame(add_quest_frame, text="Objectives:")
    quest_objectives_frame.grid(row=2, column=0)
    quest_objectives_combo = Combobox(quest_objectives_frame, values=quest_objectives, width=40, textvariable=selection)
    quest_objectives_combo.grid(row=0, column=0)
    quest_objectives_entry = Entry(quest_objectives_frame, bg='#D3F2EC')
    quest_objectives_entry.grid(row=0, column=1)

    quest_objectives_add_button = Button(quest_objectives_frame,
                                         text="Add",
                                         padx=10,
                                         command=lambda: add_objective_button_clicked())
    quest_objectives_add_button.grid(row=0, column=2)
    # =OBJECTIVES=SECTION===============================================================================================

    quest_dialog_button_frame = LabelFrame(add_quest_frame)
    quest_dialog_button_frame.grid(row=3, column=0, sticky='w')
    cancel_button = Button(quest_dialog_button_frame, text="Cancel", bg='red', command=top.destroy)
    cancel_button.grid(row=0,column=0)
    add_quest_button = Button(quest_dialog_button_frame,
                              text="Add Quest",
                              bg='green',
                              command=lambda: add_quest_button_clicked(quest_title_entry.get(),
                                                                       quest_description_text.get("1.0", 'end-1c'),
                                                                       quest_objectives,
                                                                       is_basic_quest))
    add_quest_button.grid(row=0, column=1)

    return


def add_detailed_quest():
    messagebox.showerror("Oops", "Get fucked I haven't made this part yet.")
    return


def view_deleted_quests():
    messagebox.showerror("Oops", "Double get fucked I haven't made this part yet either.")
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
canvas.pack(side="top", fill=BOTH, expand=1)
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

test_quest_label_frame = LabelFrame(second_frame, text="Testing")
test_quest_label_frame.pack(anchor='w')
test_quest_label = Label(test_quest_label_frame, text="Test Title")
test_quest_label.grid(row=0, column=0)
test_quest_Button = Button(test_quest_label_frame,  text="View")
test_quest_Button.grid(row=0, column=1)
# This is the button that is always there on first load to guide quest creation
Button(second_frame, text="Add A Basic Quest", background='red', command=add_quest).pack()


root.config(menu=menuBar)
root.mainloop()
