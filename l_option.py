from tkinter import *
import runpy

win=Toplevel()
win.focus_force()
win.geometry('400x400')

#function

def ab():
    runpy.run_path(r'C:\Users\Best\Desktop\class 12  project\Project\Books\add books.py')
def rb():
    runpy.run_path(r'C:\Users\Best\Desktop\class 12  project\Project\Books\remove book.py')
def vb():
    runpy.run_path(r'C:\Users\Best\Desktop\class 12  project\Project\Books\view books.py')

#label

l=Button(win,text='Add books',command=ab)
l.place(x=0,y=0)

l=Button(win,text='Remove books',command=rb)
l.place(x=30,y=30)

l=Button(win,text='View books',command=vb)
l.place(x=60,y=60)

win.mainloop()
