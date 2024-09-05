from tkinter import *
import runpy

win=Toplevel()
win.focus_force()
win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenwidth()}")

#function
def backmenu():
	win.destroy()
	runpy.run_path(r'C:\Users\Best\Desktop\class 12  project\Project\Login\login.py')
def t():
	win.destroy()
	runpy.run_path(r'C:\Users\Best\Desktop\class 12  project\Project\Teachers\Teachers.py')
def s():
	win.destroy()
	runpy.run_path(r'C:\Users\Best\Desktop\class 12  project\Project\Students\students.py')

#label
l=Button(win,text='Teachers',command=t,font=("",50,"bold"),relief='groove')
l.place(x=400,y=300)

l1=Button(win,text='Students',command=s,font=("",50,"bold"),relief='groove')
l1.place(x=760,y=300)

back=Button(win,text='<<---Back',command=backmenu)
back.place(x=0,y=0)

win.mainloop()
