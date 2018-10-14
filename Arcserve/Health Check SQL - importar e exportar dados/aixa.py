from tkinter import *

def get_selected_row(event):
#    global selected_tuple
    index=Listbox.curselection().self
    print(index)
#    selected_tuple=listbox.get(index)
def onselect(event):
#    global selected_tuple
    index=Listbox2.curselection()[0]
    print(index)

master = Tk()
title_text=StringVar()
e1=Entry(master,textvariable=title_text)
e1.grid(row=1,column=3)

author_text=StringVar()
e2=Entry(master,textvariable=author_text)
e2.grid(row=3,column=3)

listbox = Listbox(master)
#listbox.pack()
listbox.grid(row=0,column=0,rowspan=2,columnspan=2)
listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

listbox2 = Listbox(master)
#listbox2.pack()
listbox2.grid(row=2,column=0,rowspan=6,columnspan=2)
listbox2.insert(END, "a list entry")

for item in ["five", "six", "seven", "eight"]:
    listbox2.insert(END, item)

listbox.bind('<<ListboxSelect>>',get_selected_row)
listbox2.bind('<<ListboxSelect>>',onselect)
master.mainloop()
