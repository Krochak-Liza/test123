from tkinter import*
tk = Tk()
tk.geometry('400x300')
def btn1_click():
    lbl2=Label(text='Привіт, '+ent.get()+'!')
    lbl2.place(x=150,y=150)
def btn2_click():
    lbl1=Label(text='До зустрчі, '+ent.get()+'!')
    lbl1.place(x=150,y=150)
btn1= Button(text='Привітання',command=btn1_click)
btn1.place(x=75,y=75,width=100,height=50)
btn2=Button(text='Прощавання', command=btn2_click)
btn2.place(x=225,y=75,width=100,height=50)
ent=Entry(bd=1)
ent.place(x=225,y=30,width=100,height=30)
lbl1=Label(text="Ваше ім'я:")
lbl1.place(x=75,y=25,width=100,height=30)
lbl2=Label(text='Привіт, ' +ent.get()+'!')
lbl2.place(x=150,y=150)

