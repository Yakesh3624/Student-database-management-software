from tkinter import *
import string
win=Tk()
win.geometry("200x200")

def func(event):
	def func1(event):
		print("BackSpace")
	print("hi")
	ent.bind("<BackSpace>",func1)
ent=Entry(win)
a=string.ascii_lowercase
b=string.ascii_uppercase
c=a+b
for i in c:
	ent.bind(f"<{i}>",func)
ent.pack()
win.mainloop()