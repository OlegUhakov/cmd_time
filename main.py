import os
import time
from tkinter import *

root = Tk()
root.title('CMD')
root.geometry('200x120')
root.resizable(width=False, height=False)

str = "cmd /c date 01/01/2030"


def start(event):
    os.system(str)


def time_now(event):
    t = time.strftime("%d/%m/%Y")
    f = open('_.date', 'w')
    f.write(t)
    f.close()


def back(event):
    f = open('_.date', 'r')
    os.system('cmd /c date ' + f.read())


label = Label(root,
              text=time.ctime(),
              font=25
              )

label.pack()

btn_time = Button(root,
                  text="Time",
                  font=25,
                  width='40',
                  bg="white", fg="#555")

btn_time.bind("<Button-1>", time_now)

btn_time.pack()

btn = Button(root,
             text="Start",
             font=25,
             width='40',

             bg="white", fg="red")
btn.bind("<Button-1>", start)

btn.pack()

btn_back = Button(root,
                  text="Back",
                  font=25,
                  width='40',

                  bg="white", fg="green")
btn_back.bind("<Button-1>", back)

btn_back.pack()

root.mainloop()
