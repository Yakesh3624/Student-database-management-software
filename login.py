from tkinter import *
from PIL import ImageTk, Image
import runpy

win=Toplevel()
w=win.winfo_screenwidth()
h=win.winfo_screenheight()
#win.geometry(f'{w}x{h}')
win.attributes('-fullscreen',True)

def check():
    f=open(r"Project\Text file\pass.txt")
    d=f.readlines()
    d=''.join(d)
    d=d.split(' ')
    if d[0] == ent.get():
        win.destroy()
        runpy.run_path(r"Project\Menu\a_option.py")
    elif d[1] == ent.get():
        win.destroy()
        runpy.run_path(r"Project\Menu\l_option.py")
    
    ent.after(1,check)

def closewin():
	win.quit()
	win.destroy()

def show():
    global i
    if i =='closed':
        ent.config(show='')
        eye.config(image=e_open)
        i ='open'
    else:
        ent.config(show=u'\u2022')
        eye.config(image=e_closed)
        i ='closed'
        
i='closed'
#image
img0=Image.open(r'Project\Image\Untitled-1.jpg')
img0=img0.resize((win.winfo_screenwidth(),win.winfo_screenheight()),Image.ANTIALIAS)
logo=ImageTk.PhotoImage(img0)

img=Image.open(r'Project\Image\eye_open.png')
img=img.resize((35,22),Image.ANTIALIAS)
e_open=ImageTk.PhotoImage(img)


img1=Image.open(r'Project\Image\eye_closed.png')
img1=img1.resize((35,26),Image.ANTIALIAS)
e_closed=ImageTk.PhotoImage(img1)

img2=Image.open(r'Project\Image\l_bg.jpg')
img2=img2.resize((win.winfo_screenwidth(),win.winfo_screenheight()),Image.ANTIALIAS)
bg=ImageTk.PhotoImage(img2)

img3=Image.open(r'Project\Image\logo.png')
img3=img3.resize((300,200),Image.ANTIALIAS)
main_logo=ImageTk.PhotoImage(img3)

img4=Image.open(r"Project\Image\close1.png")
img4=img4.resize((40,40),Image.ANTIALIAS)
closeimg=ImageTk.PhotoImage(img4)
#label
L=Label(win,image=logo)
L.pack(side='left')

f=Frame(win,bg='gray76')
f.place(x=975,y=377)

head=Label(win,text='ADMIN',font=('Gill Sans',30,'bold'),bg='white')
#head.place(x=1150,y=380)

ml=Label(win,image=main_logo,bg='white')
#ml.place(x=160,y=250)
#entry
ent=Entry(f,width=18,show=u'\u2022',relief='flat',font=('',20,'bold'),bg='white')
ent.config(highlightbackground='white')
ent.pack(ipady=6)
ent.focus_force()
#button
eye=Button(win,image=e_closed,padx=5,pady=5,relief='flat',command=show,bg='white')
eye.place(x=1220,y=385)

close=Button(win,image=closeimg,relief='flat',command=closewin,bg='#7EFFC5')
close.place(x=1200,y=0)


check()

win.mainloop()
