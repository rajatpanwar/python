from tkinter import *
top = Tk()
top.geometry("300x300")

uname = Label(top,text="Name").place(x=30,y=50)
email = Label(top,text="Email").place(x=30,y=90)
password = Label(top,text="Password").place(x=30,y=130)

btn = Button(top,text="Submit",activebackground="pink",activeforeground="blue").place(x=30,y=170)

e1 = Entry(top,width =20).place(x=80,y=50)

e2 = Entry(top,width = 20).place(x=80,y=90)

e1 = Entry(top,width = 20).place(x=95,y=130)

top.mainloop()
