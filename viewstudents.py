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
heading=Label(win,text="Students details",font=('',50,'bold'))
heading.place(x=480,y=30)

db=mysql.connector.connect(host='localhost',user='root',password='yakesh',database='yakesh')

cursor=db.cursor()

cursor.execute('select * from students')

a=cursor.fetchall()
###################################

#tree view    
tree=ttk.Treeview(win,columns=(1,2,3,4,5,6,7,8),height='20')


tree.column('#0', width=130,minwidth=50)
tree.column('1', width=130,minwidth=50)
tree.column('2', width=130,minwidth=50)
tree.column('3', width=130,minwidth=50)
tree.column('4', width=130,minwidth=50)
tree.column('5', width=130,minwidth=50)
tree.column('6', width=130,minwidth=50)
tree.column('7', width=130,minwidth=50)
tree.column('8', width=130,minwidth=50)

tree.place(x=85,y=150)

scroll=ttk.Scrollbar(win, orient ='vertical',command=tree.yview)
scroll.place(x=1260,y=150,height=430)

tree.configure(yscrollcommand = scroll.set)

tree.heading('#0', text="Name")
tree.heading(1, text="DOB")
tree.heading(2, text="Standard")
tree.heading(3, text="Section")
tree.heading(4, text="Gender")
tree.heading(5, text="Father name")
tree.heading(6, text="Address")
tree.heading(7, text="Mobile number")
tree.heading(8, text="Blood group")


####################################
b=[]

for i in a:
    
    b.append(list(i))
#######################################
#b=[['a','b','c','d','e','f','g','h','i'],['j','k','l','m','n','o','p','q','r'],['s','t','u','v','w','x','y','z','a']]

name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1='','','','','','','','',''

for j in range(len(b)):
    i=b[j]
    name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
    tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))

#button
button=Button(win,text='Back',padx=10,pady=5,command=back)
button.place(x=650,y=600)


#name,dob,std,sec,gender,fname,address,number,boodgroup=b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8]
##########################################

win.mainloop()

    
