from tkinter import *
import pygame

def main():
    main_window=Tk()
    main_window.title("soundboard")
    main_window.geometry("400x300")

    btn1=Button(main_window,text="btn1",height=1,width=7,command=lambda:play(1))
    btn2=Button(main_window,text="btn2",height=1,width=7,command=lambda:play(2))
    btn3=Button(main_window,text="btn3",height=1,width=7,command=lambda:play(3))
    btn4=Button(main_window,text="btn4",height=1,width=7,command=lambda:play(4))
    btn5=Button(main_window,text="btn5",height=1,width=7,command=lambda:play(5))
    btn6=Button(main_window,text="btn6",height=1,width=7,command=lambda:play(6))
    btn7=Button(main_window,text="btn7",height=1,width=7,command=lambda:play(7))
    btn8=Button(main_window,text="btn8",height=1,width=7,command=lambda:play(8))
    btn9=Button(main_window,text="btn9",height=1,width=7,command=lambda:play(9))
    btnexit=Button(main_window,text="exit",height=1,width=10,command=main_window.destroy)

    btn1.place(x=50,y=50)
    btn2.place(x=150,y=50)
    btn3.place(x=250,y=50)
    btn4.place(x=50,y=100)
    btn5.place(x=150,y=100)
    btn6.place(x=250,y=100)
    btn7.place(x=50,y=150)
    btn8.place(x=150,y=150)
    btn9.place(x=250,y=150)
    btnexit.place(x=275,y=250)

    main_window.mainloop()

def play(button_id):
    pygame.mixer.init()
    pygame.mixer.music.load("src/"+str(button_id)+".mp3")
    pygame.mixer.music.play()

main()