import os
import time
from tkinter import *

root = Tk()
root.title('CMD')
root.geometry('200x120')
root.resizable(width=False, height=False)

str = "cmd /c date 01/01/2030"

def time_now():
    t = time.strftime("%d/%m/%Y")
    f = open('_.date', 'w')
    f.write(t)
    f.close()

time_now()



def start(event):
    os.system(str)




def back(event):
    f = open('_.date', 'r')
    os.system('cmd /c date ' + f.read())


label = Label(root,
              text=time.ctime(),
              font=25
              )

label.pack()

label.pack(ipadx=5, ipady=5)


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


label2 = Label(root,
              text='Ver 2.0',
              
              )


label2.pack(ipadx=10, ipady=10, )
label2.place(x=0, y=100)
label.pack()

root.mainloop()
