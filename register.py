def save():
    with open("idpass.txt",'w') as f:
        a=str(username_input.get())
        b=str(password_input.get())
        f.write(a)
        f.write(' ')
        f.write(b)
        '''win.destroy()
        root=Tk()
        root.geometry('1350x730')
        sucess=Label(root, text='You have sucessfully registered',font=('',40,'bold'),)
        sucess.place(x=250,y=260)
        bu=Button(root, text='close',font=('',12,'underline'), fg='grey',relief='groove',command=root.destroy)
        bu.place(x=600,y=350)'''
        messagebox.showinfo('','You have been sucessfully registred')
        win.destroy()
        

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import runpy
win=Toplevel()

win.title("Project")
width=win.winfo_screenwidth()
height=win.winfo_screenheight()
win.geometry(f'{width}x{height}')

#image
img=Image.open('bg2.jpg')
img=img.resize((width, height))

img1=ImageTk.PhotoImage(img)
bg=Label(win,image=img1)
bg.pack()


#Labels
heading=Label(win, text="Register",font=('Comic Sans MS',30,'bold'))
heading.place(x=625,y=150)

username=Label(win, text='User name',font=('',20,'bold'))
username.place(x=450,y=250)

password=Label(win, text='Password',font=('',20,'bold'))
password.place(x=450,y=300)

#Entry
username_input=Entry(win, width=35,relief='groove',bd=1)
username_input.place(x=600,y=260)
username_input.focus()

password_input=Entry(win,width=35,relief='groove',bd=1)
password_input.place(x=600,y=310)

#button
save=Button(win, text='Save',padx=10,pady=5,command=save)
save.place(x=630,y=350)



win.mainloop()
    
