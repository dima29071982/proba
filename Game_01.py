from tkinter import *
from random import random
import time
from tkinter import messagebox as mb


def move_ball(event):
    key=event.keysym
    x1,y1,x2,y2=canvas.coords(ball)
    if key=="Up" and y1>10:
        canvas.move(ball,0,-20)
    elif key=="Down" and y2<300:
        canvas.move(ball,0,20)
    elif key=="Left" and x1>0:
        canvas.move(ball,-20,0)
    elif key=="Right" and x2<400:
        canvas.move(ball,20,0)
    check_collision()


def check_collision():
    b=canvas.coords(ball)
    s=canvas.coords(square)
    if b[2] > s[0] and b[0] < s[2] and b[3] > s[1] and b[1] < s[3]:#проверяем касание фигур
        move_square()
        update_score()

def update_score():
    global score
    score+=1
    score_label.config(text=f"Счет: {score}")
    if score>=10:
        end_game()


def end_game():
    end_time=time.time()
    if end_time-start_time<=20:
        mb.showinfo("Победа!",f"Счет: {score}. Время: {(end_time-start_time):.0f}")
    else:
        mb.showinfo("Поражение",
                    f"Вы проиграли, вам не хваатило {end_time-start_time-20} секунд до победы")
    if mb.askyesno("Игра окончена","Хотите сыграть еще?"):
        start_game()
    else:
        window.destroy()

def move_square():
    x1,y1=randint(0,380),randint(0,280)
    x2,y2=x1+20,y1+20
    canvas.coords(square,x1,y1,x2,y2)


def start_game():
    global score, start_time
    score = 0
    start_time = time.time()
    score_label.config(text=f"Счет: {score}")
    canvas.coords(ball,180,130,220,170)


score=0
window=Tk()
window.title("Игра с шариком")
window.geometry("400x340")
window.focus_set()#устанафливаем фокус на главном окне



score_label=Label(text=f"Счет: {score}", font="Courier 30 bold")
score_label.pack()


canvas=Canvas(width=400, height=300, bg='black')
canvas.pack()



ball=canvas.create_oval(180,130,220,170,fill="red")
square=canvas.create_rectangle(150,150,170,170,fill="green")

start_game()

window.bind("<KeyPress>",move_ball)


window.mainloop()
