from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector as mc
import runpy
import string
import numpy
from tkinter import messagebox

win=Toplevel()
win.focus_force()
#win.attributes('-fullscreen', True)
win.geometry(f'{win.winfo_screenwidth()}x{win.winfo_screenheight()}')

#functions
def modify():
    curitem=tree.focus()
    item=tree.item(curitem)
    i=list(item.values())
    val=[i[0],i[2][0],i[2][1],i[2][2],i[2][3],i[2][4],i[2][5],i[2][6],i[2][7]]
    win.destroy()
    win1=Toplevel()
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
                sql='delete from students where Name=%s and DOB=%s and Standard=%s and Section=%s and Gender=%s and Father_name=%s and Address=%s and Number=%s and Blood_group=%s'
                cursor.execute(sql,val)
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
        win1.destroy()
        runpy.run_path(r"C:\Users\Best\Desktop\class 12  project\Project\Students\students.py")

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
    std_name_input.insert(0,val[0])

    dob_input=Entry(win1, width=50)
    dob_input.place(x=620,y=235)
    dob_input.insert(0,val[1])

    std_input=Entry(win1, width=50)
    std_input.place(x=620,y=285)
    std_input.insert(0,val[2])

    sec_input=Entry(win1, width=50)
    sec_input.place(x=620,y=335)
    sec_input.insert(0,val[3])

    gender_input=Entry(win1, width=50)
    gender_input.place(x=620,y=385)
    gender_input.insert(0,val[4])

    fname_input=Entry(win1, width=50)
    fname_input.place(x=620,y=435)
    fname_input.insert(0,val[5])

    address_input=Entry(win1, width=50)
    address_input.place(x=620,y=485)
    address_input.insert(0,val[6])

    number_input=Entry(win1, width=50)
    number_input.place(x=620,y=535)
    number_input.insert(0,val[7])

    blood_group_input=Entry(win1, width=50)
    blood_group_input.place(x=620,y=585)
    blood_group_input.insert(0,val[8])

    #buttons
    submit=Button(win1, text='Change',font=('',14,'bold'),padx=210,command=submit,relief='groove')
    submit.place(x=420,y=630)

    back=Button(win1, text='<---Back',command=back,cursor='spider')
    back.place(x=0,y=0)
    
    win1.mainloop()

def add_student():
    win.destroy()
    runpy.run_path(r"C:\Users\Best\Desktop\class 12  project\Project\Students\addstudent.py")

def back_win():
    win.destroy()
    runpy.run_path(r"C:\Users\Best\Desktop\class 12  project\Project\Menu\a_option.py")

def insert(event):
    temp=str(box.get(ACTIVE))
    ent.delete(0,END)
    ent.insert(0,temp)
    box.place_forget()

e=[]
def func(event):
    #global val
    #global val1
    if len(ent.get())>=0 and combo.get()=='Name':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=201,y=116,width=555)
        for i in b:
            val1.append(i[0])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get())>=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get())==1:
                            box.place_forget()
                if len(ent.get()) ==1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                        tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))                    

            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='DOB':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=201,y=116,width='555')
        for i in b:
            val1.append(i[1])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get())>=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get())==1:
                            box.place_forget()
                if len(ent.get()) ==1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                        tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))                    

            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='Standard':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=201,y=116,width='555')
        for i in b:
            val1.append(i[2])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get())>=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get())==1:
                            box.place_forget()
                if len(ent.get()) ==1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                        tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))                    

            ent.bind("<BackSpace>",func1)
    elif len(ent.get())>=0 and combo.get()=='Section':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=201,y=116,width='555')
        for i in b:
            val1.append(i[3])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get())>=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get())==1:
                            box.place_forget()
                if len(ent.get()) ==1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                        tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))                    

            ent.bind("<BackSpace>",func1)

    elif len(ent.get())>=0 and combo.get()=='Gender':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=201,y=116,width='555')
        for i in b:
            val1.append(i[4])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get())>=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get())==1:
                            box.place_forget()
                if len(ent.get()) ==1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                        tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))                    

            ent.bind("<BackSpace>",func1)

    elif len(ent.get())>=0 and combo.get()=='Father name':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=201,y=116,width='555')
        for i in b:
            val1.append(i[5])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get())>=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get())==1:
                            box.place_forget()
                if len(ent.get()) ==1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                        tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))                    

            ent.bind("<BackSpace>",func1)

    elif len(ent.get())>=0 and combo.get()=='Address':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=201,y=116,width='555')
        for i in b:
            val1.append(i[6])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get())>=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get())==1:
                            box.place_forget()
                if len(ent.get()) ==1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                        tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))                    

            ent.bind("<BackSpace>",func1)

    elif len(ent.get())>=0 and combo.get()=='Mobile number':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=201,y=116,width='555')
        for i in b:
            val1.append(i[7])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get())>=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get())==1:
                            box.place_forget()
                if len(ent.get()) ==1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                        tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))                    

            ent.bind("<BackSpace>",func1)

    elif len(ent.get())>=0 and combo.get()=='Blood group':
        e.append(str(event.char))
        box.delete(0,END)
        val1=[]
        box.place(x=201,y=116,width='555')
        for i in b:
            val1.append(i[8])
        val=numpy.unique(val1)
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
            def func1(event):
                if len(ent.get())>=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get())==1:
                            box.place_forget()
                if len(ent.get()) ==1:
                    tree.delete(*tree.get_children())
                    for i in b:
                        name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                        tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))                    

            ent.bind("<BackSpace>",func1)
def search_val():
    global tree
    if len(ent.get()) > 0:
        tree.delete(*tree.get_children())
        for i in b:
            if combo.get() =='Name':
                if ent.get() == i[0]:
                    name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                    tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))
            elif combo.get() == 'DOB':                                          
                if ent.get() == i[1]:
                    name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                    tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))
            elif combo.get() == 'Standard':
                if ent.get() == i[2]:
                    name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                    tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))
            elif combo.get() == 'Section':
                if ent.get() == i[3]:
                    name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                    tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))
            elif combo.get() == 'Gender':
                if ent.get() == i[4]:
                    name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                    tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))
            elif combo.get() == 'Father name':
                if ent.get() == i[5]:
                    name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                    tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))
            elif combo.get() == 'Address':
                if ent.get() == i[6]:
                    name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                    tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))
            elif combo.get() == 'Mobile number':
                if ent.get() == i[7]:
                    name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                    tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))
            elif combo.get() == 'Blood group':
                if ent.get() == i[8]:
                    name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
                    tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))

def mod():
    modify()
def dele():
    c=tree.focus()
    c1=tree.item(c)
    c2=list(c1.values())
    val1=[c2[0],c2[2][0],c2[2][1],c2[2][2],c2[2][3],c2[2][4],c2[2][5],c2[2][6],c2[2][7]]
    sql='delete from students where Name=%s and DOB=%s and Standard=%s and Section=%s and Gender=%s and Father_name=%s and Address=%s and Number=%s and Blood_group=%s'
    cursor.execute(sql,val1)
    db.commit()
    selected=tree.selection()
    tree.delete(selected)
    f.place_forget()

def sub_lab(event):
    for child in f.winfo_children():
        child.destroy()
    if len(tree.focus()) != 0:
        f.place(x=event.x,y=event.y)
        modify=Button(f,text='Modify',bg='white',relief='flat',command=mod)
        modify.pack(ipadx=20)
        delete=Button(f,text='Delete',bg='white',relief='flat',command=dele)
        delete.pack(ipadx=22)
    def sub_lab2(event):
        f.place_forget()
    tree.bind("<Button-1>",sub_lab2)

#sql connection
db=mc.connect(host='localhost',user='root',password='yakesh',database='yakesh')

cursor=db.cursor()

cursor.execute('select * from students')

a=cursor.fetchall()

b=[]

for i in a:
    
    b.append(list(i))

#heading
head=Label(win,text='Students',font=('Comic Sans MS',30,'bold'))
head.place(x=700,y=10)

#image
addres=Image.open(r"C:\Users\Best\Desktop\class 12  project\Project\Image\add.png")
addres=addres.resize((100,100),Image.ANTIALIAS)
addimg=ImageTk.PhotoImage(addres)

searchres=Image.open(r"C:\Users\Best\Desktop\class 12  project\Project\Image\search.png")
searchres=searchres.resize((22,22),Image.ANTIALIAS)
searchimg=ImageTk.PhotoImage(searchres)

#search
ent=Entry(win,width=50,font=('',15,''))
lower=list(string.ascii_lowercase)
upper=list(string.ascii_uppercase)
key=lower+upper
for k in key:
    ent.bind(f"<{str(k)}>",func)
number=['1','2','3','4','5','6','7','8','9','0','/']
for k1 in number:
    ent.bind(f"{k1}",func)

ent.place(x=200,y=90)


combo_values=['Name','DOB','Standard','Section','Gender','Father name','Address','Mobile number','Blood group']

combo=ttk.Combobox(win,width=30,value=combo_values)
combo.set(combo_values[0])
combo.place(x=800,y=90,height=27)

search=Button(win,image=searchimg,relief='groove',bg='white',command=search_val)
search.place(x=755,y=90)

#frame

tree=ttk.Treeview(win,columns=(1,2,3,4,5,6,7,8),height=33)
tree.bind("<Button-3>",sub_lab)

tree.column('#0', width=120,minwidth=50)
tree.column('1', width=120,minwidth=50)
tree.column('2', width=120,minwidth=50)
tree.column('3', width=120,minwidth=50)
tree.column('4', width=120,minwidth=50)
tree.column('5', width=120,minwidth=50)
tree.column('6', width=120,minwidth=50)
tree.column('7', width=120,minwidth=50)
tree.column('8', width=120,minwidth=50)

tree.place(x=200,y=123,width=1125)

#scroll bar

scroll=ttk.Scrollbar(win,orient='vertical',command=tree.yview)
scroll.place(x=1326,y=123,height=690)

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

name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1='','','','','','','','',''
for j in range(len(b)):
    i=b[j]
    name1,dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]
    tree.insert('',END,text=name1,values=(dob1,std1,sec1,gender1,fname1,address1,number1,bloodgroup1))

f=Frame(tree,relief='solid',borderwidth=1)
#add 
add=Button(win,image=addimg,bg='white',relief='flat',command=add_student)
add.place(x=1200,y=600)

#back
back=Button(win,text='<--- Back',command=back_win)
back.place(x=0,y=0)

box=Listbox(win,relief='flat')
box.bind("<Return>",insert)
box.bind("<Double-1>",insert)

win.mainloop()