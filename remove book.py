from tkinter import *
from tkinter import messagebox
import mysql.connector
#import library

win=Toplevel()
win.focus_force()
win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenheight()}")

#sql connection
db=mysql.connector.connect(host='localhost',user='root', password='yakesh', database='yakesh')
cursor=db.cursor()


#functions

def Submit():
    query='delete from books where Book_number=%s and Book_name=%s and Author=%s'
    values=(b_number_input.get(),b_name_input.get(),b_author_input.get())
    cursor.execute(query,values)
    messagebox.showinfo('','Removed sucessfully')
    Reset()
    win.focus_force()
    b_number_input.focus()
    db.commit()

def Reset():
    b_number_input.delete(0, END)
    b_name_input.delete(0, END)
    b_author_input.delete(0, END)
    b_number_input.focus()

def Exi():
    win.destroy()

#heading
heading=Label(win,text="Delete books",font=('',50,'bold'))
heading.place(x=480,y=50)

#label
b_number=Label(win, text='Book number', font=('',20,'bold'))
b_number.place(x=400,y=200)

b_name=Label(win, text='Book name', font=('',20,'bold'))
b_name.place(x=400,y=275)

b_author=Label(win, text='Author', font=('',20,'bold'))
b_author.place(x=400,y=350)

#entry

b_number_input=Entry(win, width=50)
b_number_input.place(x=600,y=210)

b_name_input=Entry(win, width=50)
b_name_input.place(x=600,y=285)

b_author_input=Entry(win, width=50)
b_author_input.place(x=600,y=360)

#button

add=Button(win, text="-Delete-",font=('',15,'bold'), command=Submit)
add.place(x=480, y=410)

reset=Button(win, text="Reset",font=('',15,'bold'),command=Reset)
reset.place(x=630, y=410)

exi=Button(win, text="Exit",font=('',15,'bold'), command=Exi)
exi.place(x=780, y=410)


win.mainloop()

