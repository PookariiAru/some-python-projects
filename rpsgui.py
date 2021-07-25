import random
from tkinter import *
from tkinter import messagebox
import re

window=Tk()

#things
rps=['rock','paper','scissors']
#score
def WINorLOSE():
    if text1.get("1.0","end-1c") == text2.get("1.0","end-1c"):
        winorlose.delete("1.0",END)
        winorlose.insert(END,"TIE")
        #for tie
    elif text1.get("1.0","end-1c") == 'rock':
        #....
        if text2.get("1.0","end-1c") == 'paper':
            winorlose.delete("1.0",END)
            winorlose.insert(END,"YOU LOSE")
        else:
            winorlose.delete("1.0",END)
            winorlose.insert(END,"YOU WIN")
    elif text1.get("1.0","end-1c") == 'paper':
        #....
        if text2.get("1.0","end-1c") == 'scissors':
            winorlose.delete("1.0",END)
            winorlose.insert(END,"YOU LOSE")
        else:
            winorlose.delete("1.0",END)
            winorlose.insert(END,"YOU WIN")
    elif text1.get("1.0","end-1c") == 'scissors':
        #....
        if text2.get("1.0","end-1c") == 'rock':
            winorlose.delete("1.0",END)
            winorlose.insert(END,"YOU LOSE")
        else:
            winorlose.delete("1.0",END)
            winorlose.insert(END,"YOU WIN")

def score():
    if winorlose.get("1.0","end-1c") == "YOU WIN":
        getscore1=int(scorep1.get("1.0","end-1c"))
        s1=getscore1+1
        scorep1.delete("1.0",END)
        scorep1.insert(END,s1)
    elif winorlose.get("1.0","end-1c") == "YOU LOSE":
        getscore2=int(scorep2.get("1.0","end-1c"))
        s2=getscore2+1
        scorep2.delete("1.0",END)
        scorep2.insert(END,s2)
        
#defining buttons
def rock():
    text1.delete("1.0",END)
    text1.insert(END,"rock")
    text2.delete("1.0",END)
    text2.insert(END,random.choice(rps))
    WINorLOSE()
    score()

def paper():
    text1.delete("1.0",END)
    text1.insert(END,"paper")
    text2.delete("1.0",END)
    text2.insert(END,random.choice(rps))
    WINorLOSE()
    score()

def scissors():
    text1.delete("1.0",END)
    text1.insert(END,"scissors")
    text2.delete("1.0",END)
    text2.insert(END,random.choice(rps))
    WINorLOSE()
    score()
    
#gui
label1=Label(window,text="YOU:")
label1.grid(row=0,column=0)

label2=Label(window,text="COMPUTER:")
label2.grid(row=0,column=2)

winorlose=Text(window,height=1,width=10)
winorlose.grid(row=1,column=1)

text1=Text(window,height=1,width=10)
text1.grid(row=1,column=0)

text2=Text(window,height=1,width=10)
text2.grid(row=1,column=2)

label3=Label(window,text="TAKE A PICK!")
label3.grid(row=3,column=1)

button1=Button(window,text='ROCK',command=rock)
button1.grid(row=4,column=0)

button2=Button(window,text='PAPER',command=paper)
button2.grid(row=4,column=1)

button3=Button(window,text='SCISSORS',command=scissors)
button3.grid(row=4,column=2)

label4=Label(window,text="YOUR\nSCORE:")
label4.grid(row=5,column=0)

label5=Label(window,text="COMPUTER'S\nSCORE")
label5.grid(row=5,column=2)

scorep1=Text(window,height=2,width=3)
scorep1.grid(row=6,column=0)
scorep1.insert(END,int("0"))

scorep2=Text(window,height=2,width=3)
scorep2.grid(row=6,column=2)
scorep2.insert(END,int("0"))

#final one
window.mainloop()
