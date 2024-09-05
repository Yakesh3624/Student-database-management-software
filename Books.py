from tkinter import *
from tkinter import ttk
import runpy
from PIL import ImageTk,Image
import mysql.connector
import string
import numpy

def back():
    win.destroy()
    runpy.run_path(r"C:\Users\Best\Desktop\class 12  project\Project\Login\login.py")
def add_book():
	win.destroy()
	runpy.run_path(r"C:\Users\Best\Desktop\class 12  project\Project\Books\add books.py")

def insert(event):
	temp=str(box.get(ACTIVE))
	ent.delete(0,END)
	ent.insert(0,temp)
	box.place_forget()

e=[]
def func(event):
	if len(ent.get()) >=0 and combo.get() =='Book number':
		e.append(str(event.char))
		box.delete(0,END)
		val1=[]
		box.place(x=151,y=146,width=555)
		for i in b:
			val1.append(i[0])
		val=numpy.unique(val1)
		for j in val:
			if str (''.join(e)) == j[0:len(str(''.join(e)))]:
				box.insert(END,j)
			def func1(event):
				if len(ent.get())>=0:
					try:
						e.pop()
					except:
						pass
					box.delete(0,END)
					for j in val:
						if str(''.join(e))== j[0:len(str(''.join(e)))]:
							box.insert(END,j)
						if len(ent.get())==1:
							box.place_forget()
				if len(ent.get()) ==1:
					tree.delete(*tree.get_children())
					for i in b:
						number,name,author=i[0],i[1],i[2]
						tree.insert('',END,text=number,values=(name,author))
			ent.bind("<BackSpace>",func1)
	elif len(ent.get()) >=0 and combo.get() =='Book name':
		e.append(str(event.char))
		box.delete(0,END)
		val1=[]
		box.place(x=201,y=116,width=555)
		for i in b:
			val1.append(i[1])
		val=numpy.unique(val1)
		for j in val:
			if str (''.join(e)) == j[0:len(str(''.join(e)))]:
				box.insert(END,j)
			def func1(event):
				if len(ent.get())>=0:
					try:
						e.pop()
					except:
						pass
					box.delete(0,END)
					for j in val:
						if str(''.join())== j[0:len(str(''.join(e)))]:
							box.insert(END,j)
						if len(ent.get())==1:
							box.place_forget()
				if len(ent.get()) ==1:
					tree.delete(*tree.get_children())
					for i in b:
						number,name,author=i[0],i[1],i[2]
						tree.insert('',END,text=number,values=(name,author))
			ent.bind("<BackSpace>",func1)

	elif len(ent.get()) >=0 and combo.get() =='Author':
		e.append(str(event.char))
		box.delete(0,END)
		val1=[]
		box.place(x=201,y=116,width=555)
		for i in b:
			val1.append(i[2])
		val=numpy.unique(val1)
		for j in val:
			if str (''.join(e)) == j[0:len(str(''.join(e)))]:
				box.insert(END,j)
			def func1(event):
				if len(ent.get())>=0:
					try:
						e.pop()
					except:
						pass
					box.delete(0,END)
					for j in val:
						if str(''.join())== j[0:len(str(''.join(e)))]:
							box.insert(END,j)
						if len(ent.get())==1:
							box.place_forget()
				if len(ent.get()) ==1:
					tree.delete(*tree.get_children())
					for i in b:
						number,name,author=i[0],i[1],i[2]
						tree.insert('',END,text=number,values=(name,author))
			ent.bind("<BackSpace>",func1)

def search_val():
	global tree
	if len(ent.get())>0:
		tree.delete(*tree.get_children())
		for i in b:
			if combo.get() =='Book number':
				if ent.get()==i[0]:
					number,name,author=i[0],i[1],i[2]
					tree.insert('',END,text=number,values=(name,author))
			elif combo.get() =='Book name':
				if ent.get()==i[1]:
					number,name,author=i[0],i[1],i[2]
					tree.insert('',END,text=number,values=(name,author))
			elif combo.get() =='Author':
				if ent.get()==i[2]:
					number,name,author=i[0],i[1],i[2]
					tree.insert('',END,text=number,values=(name,author))

def mod():
	modif()
def dele():
	c=tree.focus()
	c1=tree.item(c)
	c2=list(c1.values())
	val1=[c2[0],c2[2][0],c2[2][1]]
	sql='delete form books where Number=%s and Name=%s and Author=%s'
	cursor.execute(sql,val1)
	db.commit()
	selected=tree.selection()
	tree.delete(selected)
	f.place_forget()

def sublab(event):
	for child in f.winfo_children():
		child.destroy()
	if len(tree.focus()) !=0:
		f.place(x=event.x,y=event.y)
		modify=Button(f,text='Modify',bg='white',relief='flat',command=mod)
		modify.pack(ipadx=20)
		delete=Button(f,text='Delete',bg='white',relief='flat',command=dele)
		delete.pack(ipadx=22)
	def sub_lab2(event):
		f.place_forget()
		tree.bind("<Button-1>",sub_lab2)

win=Toplevel()
win.focus_force()
win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenheight()}")
win.title("Project")


#heading
heading=Label(win,text="Books",font=('',50,'bold'))
heading.place(x=600,y=30)

db=mysql.connector.connect(host='localhost',user='root',password='yakesh',database='yakesh')

cursor=db.cursor()

cursor.execute('select * from books')

a=cursor.fetchall()

#search
#image
addres=Image.open(r"C:\Users\Best\Desktop\class 12  project\Project\Image\add.png")
addres=addres.resize((100,100),Image.ANTIALIAS)
addimg=ImageTk.PhotoImage(addres)

searchres=Image.open(r"C:\Users\Best\Desktop\class 12  project\Project\Image\search.png")
searchres=searchres.resize((22,22),Image.ANTIALIAS)
searchimg=ImageTk.PhotoImage(searchres)

ent=Entry(win,width=50,font=("",15,""))
lower=list(string.ascii_lowercase)
upper=list(string.ascii_uppercase)
key=lower+upper
for k in key:
    ent.bind(f"<{str(k)}>",func)
number=['1','2','3','4','5','6','7','8','9','0','/']
for k1 in number:
    ent.bind(f"{k1}",func)
ent.place(x=150,y=120)

serbut=Button(win,image=searchimg,relief='groove',command=search_val)
serbut.place(x=706,y=120)

values=["Book number",'Book name',"Author"]
combo=ttk.Combobox(win,value=values)
combo.set(values[0])
combo.place(x=750,y=120,height=27)

#tree view    
tree=ttk.Treeview(win,columns=(1,2),height='30')
tree.bind('<Button-3>',sublab)

tree.column('#0', width=400)
tree.column('1', width=400)
tree.column('2', width=400)

tree.place(x=150,y=150)

scroll=ttk.Scrollbar(win, orient ='vertical',command=tree.yview)
scroll.place(x=1353,y=150,height=630)

tree.configure(yscrollcommand = scroll.set)

tree.heading('#0', text="Book number")
tree.heading(1, text="Book name")
tree.heading(2, text="Author")
b=[]

for i in a:
    
    b.append(list(i))

number,name,author='','',''

for j in range(len(b)):
    i=b[j]
    number,name,author,=i[0],i[1],i[2]
    tree.insert('',END,text=number,values=(name,author))

box=Listbox(win,relief='flat')
box.bind("<Return>",insert)
box.bind("<Double-1>",insert)

addbut=Button(win,image=addimg,relief='flat',bg='white',command=add_book)
addbut.place(x=1200,y=600)
#button
button=Button(win,text='<--Back',padx=10,command=back)
button.place(x=0,y=0)

aa='select * from books '

##########################################

win.mainloop()

    
