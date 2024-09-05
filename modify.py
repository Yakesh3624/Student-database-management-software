from tkinter import *
from PIL import ImageTk,Image
import runpy
import mysql.connector as mc
from tkinter import messagebox
def modify():
    win1=Tk()
    win1.focus_force()
    win1.geometry(f'{win1.winfo_screenwidth()}x{win1.winfo_screenheight()}')
    win1.title("Project")
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
                win1.focus_force() 
            else:
                cursor.execute(sqlform,values)
                #create table summa (Name varchar(50),DOB varchar(50),Standard varchar(50),Section varchar(50),Gender varchar(50),Father_name varchar(50),Address varchar(100),Number varchar(10),Blood_group varchar(5))
                db.commit()
                messagebox.showin1fo('','Sucessfully submited')
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
        win1.destroy()

    #label
    head=Label(win1,text='Modify',font=('Comic Sans MS',40,'bold'))
    head.place(x=650,y=20)

    std_name=Label(win1, text='Student name', font=('',14,'bold'))
    std_name.place(x=420,y=180)

    dob=Label(win1, text='Date of Birth',font=('',14,'bold'))
    dob.place(x=420,y=230)

    std=Label(win1, text='Standard', font=('',14,'bold'))
    std.place(x=420,y=280)

    sec=Label(win1, text='Section', font=('',14,'bold'))
    sec.place(x=420,y=330)

    gender=Label(win1, text='Gender', font=('',14,'bold'))
    gender.place(x=420,y=380)

    fname=Label(win1, text='Father name',font=('',14,'bold'))
    fname.place(x=420,y=430)

    address=Label(win1, text='Address', font=('',14,'bold'))
    address.place(x=420,y=480)

    number=Label(win1, text='Mobile number', font=('',14,'bold'))
    number.place(x=420,y=530)

    blood_group=Label(win1, text='Blood group', font=('',14,'bold'))
    blood_group.place(x=420,y=580)


    #entry box
    std_name_input=Entry(win1, width=50)
    std_name_input.place(x=620,y=185)

    dob_input=Entry(win1, width=50)
    dob_input.place(x=620,y=235)

    std_input=Entry(win1, width=50)
    std_input.place(x=620,y=285)

    sec_input=Entry(win1, width=50)
    sec_input.place(x=620,y=335)

    gender_input=Entry(win1, width=50)
    gender_input.place(x=620,y=385)

    fname_input=Entry(win1, width=50)
    fname_input.place(x=620,y=435)

    address_input=Entry(win1, width=50)
    address_input.place(x=620,y=485)

    number_input=Entry(win1, width=50)
    number_input.place(x=620,y=535)

    blood_group_input=Entry(win1, width=50)
    blood_group_input.place(x=620,y=585)

    #buttons
    submit=Button(win1, text='Change',font=('',14,'bold'),padx=210,command=submit,relief='groove')
    submit.place(x=420,y=630)

    back=Button(win1, text='<---Back',command=back,cursor='spider')
    back.place(x=0,y=0)
    
    win1.mainloop()
modify()