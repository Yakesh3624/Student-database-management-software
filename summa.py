from tkinter import *
win=Tk()
win.geometry("400x400")

b=[['Yakesh', '3/6/2004', 'XII', 'Cs', 'M', 'Pandiya raja', 'qwertyuiop', '9092210166', 'B+'], ['Balaji', '29/9/2004', 'XII', 'Cs', 'M', 'Pandiya raja', 'asdfghjkl', '6384065203', 'O+'], ['Raja', '3/2/2004', 'IX', 'A1', 'M', 'Fname', 'zxcvbnm', '9517538246', 'A+'], ['Shudharshan', '22/11/2007', 'VII', 'A10', 'M', 'Pandya', 'qscfthnnjilawwwwwwdctthniikm', '3214789650', 'O+'],['Y'],['YB']]
limit=0
def func():
	global limit
	val=[]
	l=Listbox(win)
	if len(ent.get()) >0:
		l.place(x=0,y=30)
		for i in b:
			val.append(i[0])
		for j in val:
			if ent.get()[0:len(ent.get())] == j[0:len(ent.get())]:
				l.insert(END,j)
		limit+=1

ent=Entry(win)
ent.place(x=0,y=0)
l=Listbox(win)
while 1>0:
	win.update()
	l.destroy()
	if limit >= len(b):
		limit=0
	func()
win.mainloop()