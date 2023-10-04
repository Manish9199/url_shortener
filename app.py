import pyshorteners
from tkinter import *
win = Tk()
win.geometry("500x400")
win.configure(bg="pink")

#Button Function
def short():
    URL = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(URL)

    entry2.insert(END,s)

#Level For Entering User URL
Label(win,text="Enter Your URL Link",font = "impack 17 bold",bg = "black",fg = "white").pack(fill="x")

# #Entry 
entry1 = Entry(win,font="10",bd = 3, width = 40)
entry1.pack(pady = 30)

# #Button
Button(win,text = "Click Me", font = "impack 12 bold",bg = "blue",fg = "white",width ="14",command = short).pack()

# #Entry
entry2=Entry(win,font="impack 16 bold", bg="pink",width = 24, bd = 3)
entry2.pack(pady = 30)

mainloop()