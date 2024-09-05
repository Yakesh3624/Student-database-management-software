from tkinter import *
from PIL import ImageTk,Image
import runpy
import mysql.connector as mc
from tkinter import messagebox

win=Toplevel()
win.focus_force()
win.geometry(f'{win.winfo_screenwidth()}x{win.winfo_screenheight()}')
win.title("Project")
#functions

def submit():
    h=''
    db=mc.connect(host='localhost',user='root',passwd='yakesh',database='yakesh')
    cursor=db.cursor()
    sqlform="Insert into students(Name,DOB,Standard,Section,Gender,Father_name,Address,Number,Blood_group) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=[(std_name_input.get()),(dob_input.get()),(std_input.get()),(sec_input.get()),(gender_input.get()),(fname_input.get()),(address_input.get()),(number_input.get()),(blood_group_input.get())]
    if len(number_input.get()) == 10:
        if h in values:
            messagebox.showwarning('Warning','Fill all details')
            win.focus_force() 
        else:
            cursor.execute(sqlform,values)
#create table summa (Name varchar(50),DOB varchar(50),Standard varchar(50),Section varchar(50),Gender varchar(50),Father_name varchar(50),Address varchar(100),Number varchar(10),Blood_group varchar(5))
            db.commit()
            messagebox.showinfo('','Sucessfully submited')
            std_name_input.delete(0, END)
            dob_input.delete(0,END)
            std_input.delete(0,END)
            sec_input.delete(0,END)
            gender_input.delete(0,END)
            fname_input.delete(0, END)
            address_input.delete(0,END)
            number_input.delete(0,END)
            blood_group_input.delete(0,END)
            std_name_input.focus_force()
    else:
        messagebox.showwarning('Warning','Not valid Mobile number')

def reset():
    std_name_input.delete(0, END)
    dob_input.delete(0,END)
    std_input.delete(0,END)
    sec_input.delete(0,END)
    gender_input.delete(0,END)
    fname_input.delete(0, END)
    address_input.delete(0,END)
    number_input.delete(0,END)
    blood_group_input.delete(0,END)

def back():
    win.destroy()
    runpy.run_path(r"C:\Users\Best\Desktop\class 12  project\Project\Students\students.py")

a=ImageTk.PhotoImage(Image.open(r'C:\Users\Best\Desktop\class 12  project\Project\Image\add.png'))
pic=Label(win,image=a)
pic.place(x=630,y=20)
#label

std_name=Label(win, text='Student name', font=('',14,'bold'))
std_name.place(x=400,y=180)

dob=Label(win, text='Date of Birth',font=('',14,'bold'))
dob.place(x=400,y=230)

std=Label(win, text='Standard', font=('',14,'bold'))
std.place(x=400,y=280)

sec=Label(win, text='Section', font=('',14,'bold'))
sec.place(x=400,y=330)

gender=Label(win, text='Gender', font=('',14,'bold'))
gender.place(x=400,y=380)

fname=Label(win, text='Father name',font=('',14,'bold'))
fname.place(x=400,y=430)

address=Label(win, text='Address', font=('',14,'bold'))
address.place(x=400,y=480)

number=Label(win, text='Mobile number', font=('',14,'bold'))
number.place(x=400,y=530)

blood_group=Label(win, text='Blood group', font=('',14,'bold'))
blood_group.place(x=400,y=580)


#entry box
std_name_input=Entry(win, width=50)
std_name_input.place(x=600,y=185)

dob_input=Entry(win, width=50)
dob_input.place(x=600,y=235)

std_input=Entry(win, width=50)
std_input.place(x=600,y=285)

sec_input=Entry(win, width=50)
sec_input.place(x=600,y=335)

gender_input=Entry(win, width=50)
gender_input.place(x=600,y=385)

fname_input=Entry(win, width=50)
fname_input.place(x=600,y=435)

address_input=Entry(win, width=50)
address_input.place(x=600,y=485)

number_input=Entry(win, width=50)
number_input.place(x=600,y=535)

blood_group_input=Entry(win, width=50)
blood_group_input.place(x=600,y=585)

#buttons
submit=Button(win, text='Submit',font=('',14,'bold'),padx=4,pady=3,command=submit)
submit.place(x=450,y=630)

reset=Button(win, text='Reset',font=('',14,'bold'),padx=4,pady=3,command=reset)
reset.place(x=630,y=630)

back=Button(win, text='Back',font=('',14,'bold'),padx=4,pady=3,command=back,cursor='spider')
back.place(x=800,y=630)












win.mainloop()
