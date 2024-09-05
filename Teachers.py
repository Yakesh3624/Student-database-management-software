from tkinter import *
from tkinter import ttk
import mysql.connector as mc
from PIL import ImageTk,Image
import string
import runpy
import numpy
from tkinter import messagebox

win=Toplevel()
win.focus_force()
win.geometry(F"{win.winfo_screenwidth()}x{win.winfo_screenheight()}")

db = mc.connect(host='localhost',user='root',password='yakesh',database='yakesh')

cursor=db.cursor()
cursor.execute("select * from teachers")

a=cursor.fetchall()
b=[]

for i in a:
    b.append(list(i))

#functions
def add_teachers():
	win.destroy()
	runpy.run_path(r"C:\Users\Best\Desktop\class 12  project\Project\teachers\add teacher.py")

def search_val():
    global tree 
    if len(ent.get()) >0:
        tree.delete(*tree.get_children())
        for i in b:
            if combo.get()=='Name':
                if ent.get() == i[0]:
                    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            elif combo.get()=='Father name':
                if ent.get() == i[1]:
                    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            elif combo.get()=='DOB':
                if ent.get() == i[2]:
                    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            elif combo.get()=='Gender':
                if ent.get() == i[3]:
                    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            elif combo.get()=='State':
                if ent.get() == i[4]:
                    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            elif combo.get()=='Religion & caste':
                if ent.get() == i[5]:
                    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            elif combo.get()=='Martial status':
                if ent.get() == i[6]:
                    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            elif combo.get()=='Qualification':
                if ent.get() == i[7]:
                    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            elif combo.get()=='Class':
                if ent.get() == i[8]:
                    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            elif combo.get()=='Language known':
                if ent.get() == i[9]:
                    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            elif combo.get()=='Address':
                if ent.get() == i[10]:
                    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            elif combo.get()=='Mobile number':
                if str(ent.get()) == str(i[11]):
                    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))

def modify():
    curitem=tree.focus()
    item=tree.item(curitem)
    i=list(item.values())
    val=[i[0],i[2][0],i[2][1],i[2][2],i[2][3],i[2][4],i[2][5],i[2][6],i[2][7],i[2][8],i[2][9],i[2][10]]
    win.destroy()
    win1=Toplevel()
    win1.focus_force()
    win1.geometry(f"{win1.winfo_screenwidth()}x{win1.winfo_screenheight()}")
    #functions

    def submit():
        h=''
        db=mc.connect(host='localhost',user='root',password='yakesh',database='yakesh')
        cursor=db.cursor()
        sqlform="Insert into teachers(Name,Father_name,DOB,Gender,State,Religion_and_caste,Martial_status,Qualification,Class,Language_known,Address,Mobile_number) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values=[(teac_name_input.get()),(fname_input.get()),(dob_input.get()),(gender_input.get()),(state_input.get()),(rc_input.get()),(status_input.get()),(quali_input.get()),(clas_input.get()),(lang_input.get()),(address_input.get()),(number_input.get())]
        if len(number_input.get())==10:
            if h in values:
                messagebox.showwarning('Warning','Fill all details')
                win1.focus_force()
            else:
                sql='delete from teachers where Name=%s and Father_name=%s and DOB=%s and Gender=%s and State=%s and Religion_and_caste=%s and Martial_status=%s and Qualification=%s and Class=%s and Language_known=%s and Address=%s and Mobile_number=%s'
                cursor.execute(sql,val)
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
        else:
            messagebox.showwarning('Warning','Not a valid Mobile number')
        
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
        win1.destroy()
        runpy.run_path(r"C:\Users\Best\Desktop\class 12  project\Project\Teachers\teachers.py")

    a=ImageTk.PhotoImage(Image.open(r'C:\Users\Best\Desktop\class 12  project\Project\Image\add.png'))
    pic=Label(win1,image=a)
    pic.place(x=630,y=20)
    #label

    teac_name=Label(win1, text='Teacher name', font=('',15,'bold'))
    teac_name.place(x=100,y=210)

    fname=Label(win1, text='Father name',font=('',15,'bold'))
    fname.place(x=100,y=260)

    dob=Label(win1, text='Date of birth', font=('',15,'bold'))
    dob.place(x=100,y=310)

    gender=Label(win1, text='Gender', font=('',15,'bold'))
    gender.place(x=100,y=360)

    state=Label(win1, text='State', font=('',15,'bold'))
    state.place(x=100,y=410)

    rc=Label(win1, text='Religion and Caste',font=('',15,'bold'))
    rc.place(x=100,y=460)

    status=Label(win1, text='Martial status', font=('',15,'bold'))
    status.place(x=700,y=210)

    quali=Label(win1, text='Qualification', font=('',15,'bold'))
    quali.place(x=700,y=260)

    clas=Label(win1, text='Class', font=('',15,'bold'))
    clas.place(x=700,y=310)

    lang=Label(win1, text='Language known', font=('',15,'bold'))
    lang.place(x=700,y=360)

    address=Label(win1, text='Address', font=('',15,'bold'))
    address.place(x=700,y=410)

    number=Label(win1, text='Mobile number', font=('',15,'bold'))
    number.place(x=700,y=460)

    #entry box
    teac_name_input=Entry(win1, width=50)
    teac_name_input.place(x=300,y=210)
    teac_name_input.insert(0,val[0])

    fname_input=Entry(win1, width=50)
    fname_input.place(x=300,y=260)
    fname_input.insert(0,val[1])

    dob_input=Entry(win1, width=50)
    dob_input.place(x=300,y=310)
    dob_input.insert(0,val[2])

    gender_input=Entry(win1, width=50)
    gender_input.place(x=300,y=360)
    gender_input.insert(0,val[3])

    state_input=Entry(win1, width=50)
    state_input.place(x=300,y=410)
    state_input.insert(0,val[4])

    rc_input=Entry(win1, width=50)
    rc_input.place(x=300,y=460)
    rc_input.insert(0,val[5])

    status_input=Entry(win1, width=50)
    status_input.place(x=900,y=210)
    status_input.insert(0,val[6])

    quali_input=Entry(win1, width=50)
    quali_input.place(x=900,y=260)
    quali_input.insert(0,val[7])

    clas_input=Entry(win1,width=50)
    clas_input.place(x=900,y=310)
    clas_input.insert(0,val[8])

    lang_input=Entry(win1, width=50)
    lang_input.place(x=900,y=360)
    lang_input.insert(0,val[9])

    address_input=Entry(win1, width=50)
    address_input.place(x=900,y=410)
    address_input.insert(0,val[10])

    number_input=Entry(win1, width=50)
    number_input.place(x=900,y=460)
    number_input.insert(0,val[11])
    #buttons
    submit=Button(win1, text='Submit',font=('',15,'bold'),padx=4,pady=3,command=submit)
    submit.place(x=450,y=530)

    reset=Button(win1, text='Reset',font=('',15,'bold'),padx=4,pady=3,command=reset)
    reset.place(x=660,y=530)

    back=Button(win1, text='Back',font=('',15,'bold'),padx=4,pady=3,command=back,cursor='spider')
    back.place(x=850,y=530)

    win1.mainloop()

def dele():
    c=tree.focus()
    c1=tree.item(c)
    c2=list(c1.values())
    val1=[c2[0],c2[2][0],c2[2][1],c2[2][2],c2[2][3],c2[2][4],c2[2][5],c2[2][6],c2[2][7],c2[2][8],c2[2][9],c2[2][10]]
    sql='delete from teachers where Name=%s and Father_name=%s and DOB=%s and Gender=%s and State=%s and Religion_and_caste=%s and Martial_status=%s and Qualification=%s and Class=%s and Language_known=%s and Address=%s and mobile_number=%s'
    cursor.execute(sql,val1)
    db.commit()
    selected=tree.selection()
    tree.delete(selected)
    f.place_forget()
e=[]
def func(event):
    if len(ent.get())>=0 and combo.get()=='Name':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=96,y=116,width='665')
        for i in b:
            val1.append(i[0])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get()) >=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get()) == 1:
                            box.place_forget()
                if len(ent.get()) == 1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                        tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            
            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='Father name':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=96,y=116,width='665')
        for i in b:
            val1.append(i[1])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get()) >=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get()) == 1:
                            box.place_forget()
                if len(ent.get()) == 1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                        tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='DOB':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=96,y=116,width='665')
        for i in b:
            val1.append(i[2])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get()) >=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get()) == 1:
                            box.place_forget()
                if len(ent.get()) == 1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                        tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='Gender':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=96,y=116,width='665')
        for i in b:
            val1.append(i[3])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get()) >=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get()) == 1:
                            box.place_forget()
                if len(ent.get()) == 1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                        tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='State':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=96,y=116,width='665')
        for i in b:
            val1.append(i[4])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get()) >=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get()) == 1:
                            box.place_forget()
                if len(ent.get()) == 1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                        tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='Religion & caste':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=96,y=116,width='665')
        for i in b:
            val1.append(i[5])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get()) >=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get()) == 1:
                            box.place_forget()
                if len(ent.get()) == 1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                        tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='Martial status':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=96,y=116,width='665')
        for i in b:
            val1.append(i[6])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get()) >=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get()) == 1:
                            box.place_forget()
                if len(ent.get()) == 1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                        tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='Qualification':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=96,y=116,width='665')
        for i in b:
            val1.append(i[7])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get()) >=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get()) == 1:
                            box.place_forget()
                if len(ent.get()) == 1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                        tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='Class':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=96,y=116,width='665')
        for i in b:
            val1.append(i[8])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get()) >=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get()) == 1:
                            box.place_forget()
                if len(ent.get()) == 1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                        tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='Language known':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=96,y=116,width='665')
        for i in b:
            val1.append(i[9])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get()) >=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get()) == 1:
                            box.place_forget()
                if len(ent.get()) == 1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                        tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='Address':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=96,y=116,width='665')
        for i in b:
            val1.append(i[10])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get()) >=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get()) == 1:
                            box.place_forget()
                if len(ent.get()) == 1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                        tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='Mobile number':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=96,y=116,width='665')
        for i in b:
            val1.append(str(i[11]))
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == str(j[0:len(str(''.join(e)))]):
                box.insert(END,j)
            def func1(event):
                if len(ent.get()) >=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == str(j[0:len(str(''.join(e)))]):
                            box.insert(END,j)
                        if len(ent.get()) == 1:
                            box.place_forget()
                if len(ent.get()) ==1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
                        tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
            ent.bind("<BackSpace>",func1)

def insert(event):
    temp=str(box.get(ACTIVE))
    ent.delete(0,END)
    ent.insert(0,temp)
    box.place_forget()

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

def back_win():
    win.destroy()
    runpy.run_path(r"C:\Users\Best\Desktop\class 12  project\Project\Menu\a_option.py")

def mod():
    modify()
#heading
head=Label(win,text='Teachers',font=('Comic Sans MS',30,'bold'))
head.place(x=700,y=10)


#image
addres=Image.open(r"C:\Users\Best\Desktop\class 12  project\Project\Image\add.png")
addres=addres.resize((100,100),Image.ANTIALIAS)
addimg=ImageTk.PhotoImage(addres)

searchres=Image.open(r"C:\Users\Best\Desktop\class 12  project\Project\Image\search.png")
searchres=searchres.resize((22,22),Image.ANTIALIAS)
searchimg=ImageTk.PhotoImage(searchres)

#search
ent=Entry(win,width=60,font=('',15,''))
lower=list(string.ascii_lowercase)
upper=list(string.ascii_uppercase)
key=lower+upper
for k in key:
    ent.bind(f"<{str(k)}>",func)
number=['1','2','3','4','5','6','7','8','9','0','/']
for k1 in number:
    ent.bind(f"{k1}",func)

ent.place(x=95,y=90)


combo_values=['Name','Father name','DOB','Gender','State','Religion & caste','Martial status','Qualification','Class','Language known','Address','Mobile number']

combo=ttk.Combobox(win,width=30,value=combo_values)
combo.set(combo_values[0])
combo.place(x=800,y=90,height=27)

search=Button(win,image=searchimg,relief='groove',bg='white',command=search_val)
search.place(x=761,y=90)

#tree view    
tree=ttk.Treeview(win,columns=(1,2,3,4,5,6,7,8,9,10,11),height='33')
tree.bind('<Button-3>',sublab)

tree.column('#0', width=110,minwidth=30)
tree.column('1', width=110,minwidth=30)
tree.column('2', width=110,minwidth=30)
tree.column('3', width=110,minwidth=30)
tree.column('4', width=110,minwidth=30)
tree.column('5', width=110,minwidth=30)
tree.column('6', width=110,minwidth=30)
tree.column('7', width=110,minwidth=30)
tree.column('8', width=110,minwidth=30)
tree.column('9', width=110,minwidth=30)
tree.column('10', width=110,minwidth=30)
tree.column('11', width=110,minwidth=30)

tree.place(x=95,y=123)

scroll=ttk.Scrollbar(win, orient ='vertical',command=tree.yview)
scroll.place(x=1418,y=123,height=690)

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

name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1='','','','','','','','','','','',''

for j in range(len(b)):
    i=b[j]
    name1,fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
    tree.insert('',END,text=name1,values=(fname1,dob1,gender1,state1,rc1,status1,quali1,clas1,lang1,address1,number1))
f=Frame(tree,relief='solid',borderwidth=1)
#add 
add=Button(win,image=addimg,bg='white',relief='flat',command=add_teachers)
add.place(x=1200,y=600)

#back
back=Button(win,text='<--- Back',command=back_win)
back.place(x=0,y=0)

box=Listbox(win,relief='flat')
box.bind("<Return>",insert)
box.bind("<Double-1>",insert)

win.mainloop()