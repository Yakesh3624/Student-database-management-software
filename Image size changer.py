from tkinter import*
from PIL import ImageTk,Image
win=Tk()
width=win.winfo_screenwidth()
height=win.winfo_screenheight()
#img=Image.open('eye_open.png')
#img=img.resize((20, 20), Image.ANTIALIAS)

#img1= ImageTk.PhotoImage(img)
#l=Label(win,image=img1)
#l.pack(fill=BOTH)
print(width,'x',height)
win.mainloop()
