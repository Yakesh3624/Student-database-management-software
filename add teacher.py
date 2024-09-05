from tkinter import *
from PIL import ImageTk,Image
import runpy
import mysql.connector
from tkinter import messagebox

win=Toplevel()
win.focus_force()
win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenheight()}")
#functions

def submit():
    h=''
    db=mysql.connector.connect(host='localhost',user='root',password='yakesh',database='yakesh')
    cursor=db.cursor()
    sqlform="Insert into teachers(Name,Father_name,DOB,Gender,State,Religion_and_caste,Martial_status,Qualification,Class,Language_known,Address,Mobile_number) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=[(teac_name_input.get()),(fname_input.get()),(dob_input.get()),(gender_input.get()),(state_input.get()),(rc_input.get()),(status_input.get()),(quali_input.get()),(clas_input.get()),(lang_input.get()),(address_input.get()),(number_input.get())]
    if h in values:
        messagebox.showwarning('Warning','Fill all details')
        win.focus_force()
    else:
        cursor.execute(sqlform,values)
#create table summa (Name varchar(50),DOB varchar(50),Standard varchar(50),Section varchar(50),Gender varchar(50),Father_name varchar(50),Address varchar(100),Number varchar(10),Blood_group varchar(5))
        db.commit()
        messagebox.showinfo('','Sucessfully submited')
        teac_name_input.delete(0, END)
        fname_input.delete(0,END)
        dob_input.delete(0,END)
        gender_input.delete(0,END)
        state_input.delete(0,END)
        rc_input.delete(0, END)
        status_input.delete(0,END)
        quali_input.delete(0,END)
        clas_input.delete(0,END)
        lang_input.delete(0,END)
        address_input.delete(0,END)
        number_input.delete(0,END)
        
        
def reset():
    teac_name_input.delete(0, END)
    fname_input.delete(0,END)
    dob_input.delete(0,END)
    gender_input.delete(0,END)
    state_input.delete(0,END)
    rc_input.delete(0, END)
    status_input.delete(0,END)
    quali_input.delete(0,END)
    clas_input.delete(0,END)
    lang_input.delete(0,END)
    address_input.delete(0,END)
    number_input.delete(0,END)

def back():
    win.destroy()
    runpy.run_path(r"C:\Users\Best\Desktop\class 12  project\Project\Teachers\Teachers.py")

a=ImageTk.PhotoImage(Image.open(r'C:\Users\Best\Desktop\class 12  project\Project\Image\add.png'))
pic=Label(win,image=a)
pic.place(x=630,y=20)
#label

teac_name=Label(win, text='Teacher name', font=('',15,'bold'))
teac_name.place(x=100,y=210)

fname=Label(win, text='Father name',font=('',15,'bold'))
fname.place(x=100,y=260)

dob=Label(win, text='Date of birth', font=('',15,'bold'))
dob.place(x=100,y=310)

gender=Label(win, text='Gender', font=('',15,'bold'))
gender.place(x=100,y=360)

state=Label(win, text='State', font=('',15,'bold'))
state.place(x=100,y=410)

rc=Label(win, text='Religion and Caste',font=('',15,'bold'))
rc.place(x=100,y=460)

status=Label(win, text='Martial status', font=('',15,'bold'))
status.place(x=700,y=210)

quali=Label(win, text='Qualification', font=('',15,'bold'))
quali.place(x=700,y=260)

clas=Label(win, text='Class', font=('',15,'bold'))
clas.place(x=700,y=310)

lang=Label(win, text='Language known', font=('',15,'bold'))
lang.place(x=700,y=360)

address=Label(win, text='Address', font=('',15,'bold'))
address.place(x=700,y=410)

number=Label(win, text='Mobile number', font=('',15,'bold'))
number.place(x=700,y=460)

#entry box
teac_name_input=Entry(win, width=50)
teac_name_input.place(x=300,y=210)

fname_input=Entry(win, width=50)
fname_input.place(x=300,y=260)

dob_input=Entry(win, width=50)
dob_input.place(x=300,y=310)

gender_input=Entry(win, width=50)
gender_input.place(x=300,y=360)

state_input=Entry(win, width=50)
state_input.place(x=300,y=410)

rc_input=Entry(win, width=50)
rc_input.place(x=300,y=460)

status_input=Entry(win, width=50)
status_input.place(x=900,y=210)

quali_input=Entry(win, width=50)
quali_input.place(x=900,y=260)

clas_input=Entry(win,width=50)
clas_input.place(x=900,y=310)

lang_input=Entry(win, width=50)
lang_input.place(x=900,y=360)

address_input=Entry(win, width=50)
address_input.place(x=900,y=410)

number_input=Entry(win, width=50)
number_input.place(x=900,y=460)
#buttons
submit=Button(win, text='Submit',font=('',15,'bold'),padx=4,pady=3,command=submit)
submit.place(x=450,y=530)

reset=Button(win, text='Reset',font=('',15,'bold'),padx=4,pady=3,command=reset)
reset.place(x=660,y=530)

back=Button(win, text='Back',font=('',15,'bold'),padx=4,pady=3,command=back,cursor='spider')
back.place(x=850,y=530)

win.mainloop()
