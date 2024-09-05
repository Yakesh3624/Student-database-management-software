from tkinter import *
win=Tk()
win.geometry('1350x730')

#main frame

mainframe=LabelFrame(win,width=1250,height=600)
mainframe.place(x=50,y=120)

# information frame
info = LabelFrame(mainframe,width=1240,height=100)
info.place(x=5,y=5)

#sub info table

name=LabelFrame(info,width=127,height=90)
name.place(x=10,y=3)
name=Label(name,text='Name',padx=44,pady=34)
name.pack()

dob=LabelFrame(info,width=127,height=90)
dob.place(x=150,y=3)
dob=Label(dob,text='DOB',padx=48,pady=34)
dob.pack()

std=LabelFrame(info,width=127,height=90)
std.place(x=285,y=3)
std=Label(std,text='Standard',padx=36,pady=34)
std.pack()

sec=LabelFrame(info,width=127,height=90)
sec.place(x=420,y=3)
sec=Label(sec,text='Section',padx=39,pady=34)
sec.pack()

gender=LabelFrame(info,width=127,height=90)
gender.place(x=555,y=3)
gender=Label(gender,text='Gender',padx=40,pady=34)
gender.pack()

fname=LabelFrame(info,width=127,height=90)
fname.place(x=690,y=3)
fname=Label(fname,text='Father name',padx=26,pady=34)
fname.pack()

address=LabelFrame(info,width=127,height=90)
address.place(x=825,y=3)
address=Label(address,text='Address',padx=38,pady=34)
address.pack()

number=LabelFrame(info,width=127,height=90)
number.place(x=960,y=3)
number=Label(number,text='Number',padx=37,pady=34)
number.pack()

bloodgroup=LabelFrame(info,width=130,height=90)
bloodgroup.place(x=1095,y=3)
bloodgroup=Label(bloodgroup,text='Blood group',padx=28,pady=34)
bloodgroup.pack()

#value frame
value=LabelFrame(mainframe,width=1240,height=485)
value.place(x=5,y=110)

#sub value frame

name_value=LabelFrame(value,width=127,height=475)
name_value.place(x=10,y=3)

dob_value=LabelFrame(value,width=127,height=475)
dob_value.place(x=150,y=3)

std_value=LabelFrame(value,width=127,height=475)
std_value.place(x=285,y=3)

sec_value=LabelFrame(value,width=127,height=475)
sec_value.place(x=420,y=3)

gender_valuer=LabelFrame(value,width=127,height=475)
gender_valuer.place(x=555,y=3)

fname_value=LabelFrame(value,width=127,height=475)
fname_value.place(x=690,y=3)

address_value=LabelFrame(value,width=127,height=475)
address_value.place(x=825,y=3)

number_value=LabelFrame(value,width=127,height=475)
number_value.place(x=960,y=3)

bloodgroup_value=LabelFrame(value,width=130,height=475)
bloodgroup_value.place(x=1095,y=3)


win.mainloop()
