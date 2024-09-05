from tkinter import *
import string

win=Tk()
win.geometry("200x200")
e=[]
def func(event):
    if len(ent.get())>=0:
        global e
        e.append(event.char)
        box.delete(0,END)
        val=[]
        box.pack()
        for i in b:
            val.append(i[0])
        for j in val:
            if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                box.insert(END,j)
                print(''.join(e),'==', j[0:len(str(''.join(e)))])
            def func1(event):
                if len(ent.get())>=0:
                    try:
                        e.pop()
                    except:
                        pass
                    box.delete(0,END)
                    for j in val:
                        #print(ent.get(),'==', j[0:len(ent.get())])
                        if str(''.join(e)) == j[0:len(str(''.join(e)))]:
                            box.insert(END,j)
                        if len(ent.get())==1:
                            box.forget()

            ent.bind("<BackSpace>",func1)
            


b=[['ya'],['yb'],['yc'],['yd']]

ent=Entry(win)
lower=string.ascii_lowercase
upper=string.ascii_uppercase
key=lower+upper
for k in key:
    ent.bind(f"<{k}>",func)
ent.pack()

box=Listbox(win)

win.mainloop()