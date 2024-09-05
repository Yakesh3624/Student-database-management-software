#functions
def delete():
    comp=[name.get(),dob.get(),quali.get(),clas.get(),number.get()]
    count=0
    for j in range(len(b)):
        k=[b[j][0] , b[j][2] , b[j][7] , b[j][8] , b[j][11]]
        if k[0] == comp[0]:
            count+=1
        if k[1] == comp[1]:
            count+=1
        if k[2] == comp[2]:
            count+=1
        if k[3] == comp[3]:
            count+=1
        if str(k[4]) == str(comp[4]):
            count+=1 
    if count == 5:
        sql='delete from teachers where Name=%s and DOB=%s and Qualification=%s and Class=%s and mobile_number=%s'
        values=[(name.get()),(dob.get()),(quali.get()),(clas.get()),(number.get())]
        cursor.execute(sql,values)
        db.commit()
        messagebox.showinfo('Deleted','Sucessfully removed')
        name.delete(0, END)
        dob.delete(0, END)
        quali.delete(0, END)
        clas.delete(0, END)
        number.delete(0, END)
        
        
    else:
        messagebox.showerror('Invalid','Data not found')
        win.focus_force()
        
       


def reset():
    name.delete(0, END)
    dob.delete(0,END)
    clas.delete(0,END)
    quali.delete(0,END)
    number.delete(0,END)

def back():
    win.destroy()
#######################################################
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
from tkinter import messagebox

win=Toplevel()
win.focus_force()
win.title("Project")
win.geometry('1350x730')

db=mysql.connector.connect(host='localhost',user='root',password='yakesh',database='yakesh')

cursor=db.cursor()

cursor.execute('select * from teachers')

val=cursor.fetchall()
b=[]
for i in val:
    b.append(list(i))

#b=[['Yakesh', '3/6/2004', 'XII', 'Computer science', 'M', 'Pandiya raja', '12,Abrami nagar,Sikkandar chavadi,Madurai-18', '9092210166', 'B+'], ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o']]



#image
img=Image.open(r'C:\Users\Best\Desktop\class 12  project\Project\Image\delete.png')
img=img.resize((90,95), Image.ANTIALIAS)

ai=ImageTk.PhotoImage(img)
pic=Label(win,image=ai)
pic.place(x=380,y=20)

heading=Label(win,text="Delete teacher",font=('',50,'bold'))
heading.place(x=500,y=35)


#label

namel=Label(win, text='Teacher name', font=('',14,'bold'))
namel.place(x=400,y=180)

dobl=Label(win, text='Date of Birth',font=('',14,'bold'))
dobl.place(x=400,y=230)

stdl=Label(win, text='Qualification', font=('',14,'bold'))
stdl.place(x=400,y=280)

secl=Label(win, text='Class', font=('',14,'bold'))
secl.place(x=400,y=330)

numberl=Label(win, text='Mobile number', font=('',14,'bold'))
numberl.place(x=400,y=380)

#entry box

name=Entry(win, width=50)
name.place(x=600,y=185)

dob=Entry(win, width=50)
dob.place(x=600,y=235)

quali=Entry(win, width=50)
quali.place(x=600,y=285)

clas=Entry(win, width=50)
clas.place(x=600,y=335)

number=Entry(win, width=50)
number.place(x=600,y=385)


#button
select=Button(win, text='Delete teacher',font=('',14,'bold'),padx=4,pady=3,command=delete)
select.place(x=420,y=440)

reset=Button(win, text='Reset',font=('',14,'bold'),padx=4,pady=3,command=reset)
reset.place(x=650,y=440)

back=Button(win, text='Back',font=('',14,'bold'),padx=4,pady=3,command=back,cursor='spider')
back.place(x=820,y=440)










win.mainloop()
