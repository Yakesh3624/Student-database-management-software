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

#image
img=Image.open(r'C:\Users\Best\Desktop\class 12  project\Project\Image\view.png')
img=img.resize((100,100), Image.ANTIALIAS)
image1=ImageTk.PhotoImage(img)
background1=Label(win,image=image1)
background1.place(x=350,y=20)
#heading
heading=Label(win,text="Teachers  details",font=('',50,'bold'))
heading.place(x=480,y=30)

db=mysql.connector.connect(host='localhost',user='root',password='yakesh',database='yakesh')

cursor=db.cursor()

cursor.execute('select * from teachers')

a=cursor.fetchall()
###################################

#tree view    
tree=ttk.Treeview(win,columns=(1,2,3,4,5,6,7,8,9,10,11),height='20')


tree.column('#0', width=100,minwidth=30)
tree.column('1', width=100,minwidth=30)
tree.column('2', width=100,minwidth=30)
tree.column('3', width=100,minwidth=30)
tree.column('4', width=100,minwidth=30)
tree.column('5', width=100,minwidth=30)
tree.column('6', width=100,minwidth=30)
tree.column('7', width=100,minwidth=30)
tree.column('8', width=100,minwidth=30)
tree.column('9', width=100,minwidth=30)
tree.column('10', width=100,minwidth=30)
tree.column('11', width=100,minwidth=30)

tree.place(x=75,y=150)

scroll=ttk.Scrollbar(win, orient ='vertical',command=tree.yview)
scroll.place(x=1278,y=150,height=430)

tree.configure(yscrollcommand = scroll.set)

tree.heading('#0', text="Name")
tree.heading(1, text="Father name")
tree.heading(2, text="DOB")
tree.heading(3, text="Gender")
tree.heading(4, text="State")
tree.heading(5, text="Religion and caste")
tree.heading(6, text="Martial status")
tree.heading(7, text="Qualification")
tree.heading(8, text="Class")
tree.heading(9, text="Language known")
tree.heading(10, text="Address")
tree.heading(11, text="Mobile number")


####################################
b=[]

for i in a:
    
    b.append(list(i))
#######################################
#b=[['a','b','c','d','e','f','g','h','i'],['j','k','l','m','n','o','p','q','r'],['s','t','u','v','w','x','y','z','a']]

name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1='','','','','','','','','','','',''

for j in range(len(b)):
    i=b[j]
    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))

#button
button=Button(win,text='Back',padx=10,pady=5,command=back)
button.place(x=650,y=600)


#name,dob,std,sec,gender,fname,address,number,boodgroup=b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8]
##########################################

win.mainloop()

    
