from tkinter import *
from PIL import ImageTk,Image
import time
import pygame
from tkinter import messagebox
import datetime

# for creating basic window
root = Tk()
root.title("Alarm Clock")
root.geometry("800x470+0+0")
root.configure(bg='aqua')
root.resizable(False, False)

# image
bg = ImageTk.PhotoImage(Image.open("ABD.png"))

# label for image
la = Label(root,image=bg)
la.place(x=0, y=0, relwidth=1, relheight=1)

# creating Current Time And Current Day and Date
currentT = Label(root, text="", font=("roboto mono", 23), fg="red", bg="black", width=8, height=2)
currentT.grid(row=1, column=2, columnspan=3)

currentD = Label(root, text="", font=("comic sans", 11), fg="red")
currentD.grid(row=3, column=1, pady=20)

# for string var
alarmtime = StringVar()
msgi = StringVar()

# function for current Time
def clock():
    ti = time.strftime("%H:%M:%S")
    day = time.strftime("%x, %A")
    timezone = time.strftime("%Z")
    currentT.config(text=ti)
    currentT.after(1000,clock)
    currentD.config(text=day +" ; "+timezone)
clock()

# for sound
pygame.mixer.init()

# for alarm working
def al():
    AlarmT= alarmtime.get()

    CurrentT= time.strftime("%H:%M:%S")

    while AlarmT != CurrentT:
        CurrentT = time.strftime("%H:%M:%S")


    if AlarmT == CurrentT:
        pygame.mixer.music.load('tone.mp3')
        pygame.mixer.music.play(3)
        pygame.mixer.music.set_volume(0.2)
        message = messagebox.askquestion('Alert',f'{msgi.get()}')

        if message == "yes":
            pygame.mixer.music.stop()
        if message == "no":
            message1 = messagebox.showerror('Error','Wake up!')

#for input
inp=Label(root,text="Enter Time",font=("comic sans",18),bg="spring green",width=10,relief=SUNKEN)
inp.grid(row=4,column=1,columnspan=3)


# for submit button
submit = Button(root,text="Set Alarm",font=("comic sans",18),bg="brown",activebackground="white",relief=RAISED,cursor="hand2",command=al)
submit.grid(row=5,column=2,columnspan=2,pady=24)

# for messagebox
msg = Label(root,text="Message",font=("comic sans",18),bg="gray64")
msg.grid(row=8,column=3,columnspan=2)

# for entering time
ent_time = Entry(root,textvariable=alarmtime,font=("comic sans",18),width=20,borderwidth=4)
ent_time.grid(row=4,column=4,columnspan=2)

msgi.set("Select any message")
# for entering message
msginput = Entry(root,textvariable=msgi,font=("comic sans",18),borderwidth=4)
msginput1 = OptionMenu(root,msgi,"Good Morning","Guten Morgan","Ohayo","Wake up to reality!!","Ara Ara","MoshiMosh")
msginput.grid(row=9,column=3,columnspan=2)
msginput1.grid(row=9,column=1,columnspan=2)

# to close program
def st():
    root.destroy()

# reset button
def cl():
    ent_time.delete(0,"end")
def cl1():
    msginput.delete(0,"end")

# for close button
close = Button(root,text="Close",font=("comic sans",18),bg="brown",activebackground="white",width=8,relief=RAISED,command=st,cursor="hand2")
close.grid(row=5,column=1,columnspan=2)

# for delete button
delete = Button(root,text="Reset",font=("comic sans",18),bg="brown",activebackground="white",width=8,relief=RAISED,command=cl,cursor="hand2")
delete.grid(row=5,column=5)

delete1 = Button(root,text="X",font=("comic sans",18),bg="brown",activebackground="white",width=3,height=1,relief=RAISED,command=cl1,cursor="hand2")
delete1.grid(row=9,column=5)

root.mainloop()