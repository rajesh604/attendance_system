from tkinter import *

root = Tk()
root.geometry('443x233')
root.title("My Gui With Harry")

title_label = Label(text='''
Pinger is a multidisciplinary, cross-functional, equal-opportunity company that encourages a healthy work-life balance and hyphen-rich\nsentences.On the outside, we’re a tech company. On the inside, we’re a group of collaborative people building products\n that simplify communications for our customers—and having some fun while we’re at it.
''',bg="red")
title_label.pack()
root.mainloop()