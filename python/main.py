from court import*
from tkinter import*
from ball import*

width,height=764,374
window=Tk()
window.title('Tennis Game')
window.geometry('764x374+150+150')
window.resizable(False,False)
img='court.png'

court=Court(window,width,height,img)

x1,y1=width/2,height/2
x2,y2=x1+30,y1+30

ball=Ball(court,x1,y1,x2,y2)

def play_game():

    ball.move_ball()

    window.after(50,play_game)

play_game()

window.mainloop()