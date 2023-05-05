from tkinter import*

win=Tk()
win.title('환경 시뮬레이터')
win.geometry('600x600')

f1=Frame(win,bg='white')
b1=Button(f1,text='Go f2',command=lambda:[f2.tkraise()])
f2=Frame(win,bg='blue')
b2=Button(f2,text='Go f1',command=lambda:[f1.tkraise()])

f1.grid(row=0,column=0)
f2.grid(row=0,column=0)
b1.pack()
b2.pack()
win.mainloop()