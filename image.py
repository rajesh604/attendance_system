from tkinter import *
root = Tk()

root.geometry('900x500')
photo = PhotoImage(".\Rs.jpg")
label = Label(image=photo)

label.pack()

root.mainloop()