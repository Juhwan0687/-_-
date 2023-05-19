from tkinter import*

def change_frame(x):
    print(x)
    if x==1:
        start.grid(row=0,column=0)
        f1.pack()
    elif x==2:
        f1.grid(row=0,column=0)
        f1_f.pack()
    #elif x==3:
        #f1.grid(row=0,column=0)
        #f1_f2.pack()

win=Tk()
win.title('환경 시뮬레이터')
win.geometry('600x600')
a=PhotoImage(file='pla.png')

start=Frame(win,bg='white')
f1=Frame(win,bg='white')
f1_f=Frame(win,bg='white')
f1_f2=Frame(win,bg='white')

start_img=PhotoImage(file='earth.png')
lb1=Label(start,image=start_img,width=600,bg='white',height=500)
one_btn=Button(f1,text='일회용품 사용',height=13,width=250,bg='light coral',font=('consolas',15,'bold'),command=lambda:change_frame(2))
start_btn=Button(start,text='START',width=600,height=100,font=('consolas',30,'bold'),relief='solid',bg='orange',command=lambda:change_frame(1))
many_btn=Button(f1,text='다회용품 사용',width=250,bg='light skyblue',height=13,font=('consolas',15,'bold'),command=lambda:change_frame(3))
lb2=Label(f1,text='VS',width=600,font=('consolas',15,'bold'))
lb3=Label(f1_f,image=a,width=600,height=384)
end_btn=Button(f1_f,text='END',font=('consolas',20,'bold'),width=600,height=600-384,bg='orange',relief='solid',command=lambda:win.quit())

start.pack()
f1.pack()
f1_f.pack()
lb1.pack()
one_btn.pack()
start_btn.pack()
lb2.pack()
many_btn.pack()
lb3.pack()
end_btn.pack()
f1_f2.pack()

win.mainloop()