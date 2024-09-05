from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector

def back():
    win.destroy()
   # 

win=Toplevel()
#win=Tk()
win.focus_force()
win.geometry('1350x730')
win.title("Project")

#image
img=Image.open(r'C:\Users\Best\Desktop\class 12  project\Project\Image\view.png')
img=img.resize((100,100), Image.ANTIALIAS)
image1=ImageTk.PhotoImage(img)
background1=Label(win,image=image1)
background1.place(x=350,y=20)
#heading
heading=Label(win,text="Books details",font=('',50,'bold'))
heading.place(x=480,y=30)

db=mysql.connector.connect(host='localhost',user='root',password='yakesh',database='yakesh')

cursor=db.cursor()

cursor.execute('select * from books')

a=cursor.fetchall()
###################################

#tree view    
tree=ttk.Treeview(win,columns=(1,2),height='20')


tree.column('#0', width=400)
tree.column('1', width=400)
tree.column('2', width=400)

tree.place(x=85,y=150)

scroll=ttk.Scrollbar(win, orient ='vertical',command=tree.yview)
scroll.place(x=1290,y=150,height=430)

tree.configure(yscrollcommand = scroll.set)

tree.heading('#0', text="Book number")
tree.heading(1, text="Book name")
tree.heading(2, text="Author")



####################################
b=[]

for i in a:
    
    b.append(list(i))
#######################################

number,name,author='','',''

for j in range(len(b)):
    i=b[j]
    number,name,author,=i[0],i[1],i[2]
    tree.insert('',END,text=number,values=(name,author))

#button
button=Button(win,text='Back',padx=10,pady=5,command=back)
button.place(x=650,y=600)


##########################################

win.mainloop()

    
