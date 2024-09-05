from tkinter import *

win=Tk()
win.geometry('400x400')
b=[['Yakesh', '3/6/2004', 'XII', 'Cs', 'M', 'Pandiya raja', 'qwertyuiop', '9092210166', 'B+'], ['Balaji', '29/9/2004', 'XII', 'Cs', 'M', 'Pandiya raja', 'asdfghjkl', '6384065203', 'O+'], ['Raja', '3/2/2004', 'IX', 'A1', 'M', 'Fname', 'zxcvbnm', '9517538246', 'A+'], ['Shudharshan', '22/11/2007', 'VII', 'A10', 'M', 'Pandya', 'qscfthnnjilawwwwwwdctthniikm', '3214789650', 'O+'],['Ya'],['Yb']]
def summa():
	ins=[]
	if len(ent.get()) >0 and combo.get() =='Name':
		f.place(x=0,y=20,width=304,height=100)
		for i in b:
			ins.append(i[0])
		for j in ins:
			if ent.get()[0:len(ent.get())] == j[0:len(ent.get())]:
				label=Label(f,text=j,bg='white')
				label.pack(anchor='w')

ent=Entry(win,width=50)
ent.place(x=0,y=0)

f=Frame(win,bg='white')
while 1>0:
	win.update()
	for child in f.winfo_children():
		child.destroy()
	summa()

win.mainloop()