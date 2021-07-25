import tkinter as tk
from tkinter import *
from sqlite3  import *
import sqlite3
import os
from tkinter import messagebox


def New():
    listbox.delete(0, END)
    #getFile= FILEentry.get()
    #con2 = sqlite3.connect(getFile+'.db')
    getEntry= str(FILEentry.get())
    cur.execute('''INSERT INTO examfilename (namesoffile)
                    VALUES(?)''',(FILEentry.get(),))
    cur.execute("SELECT * FROM examfilename")
    rows = cur.fetchall()
    con.commit()
    for row in rows:
        listbox.insert(END, row)
    
    Newwin()

def Open():
    #getFile= FILEentry.get()
    #con2 = sqlite3.connect(getFile+'.db')
    Newwin()

class Newwin():
    def __init__(self):
        #window
        self.newwin = Toplevel(window)
        #connect sqlite
        self.con = sqlite3.connect(FILEentry.get()+'.db')
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS
        Exam(qnames TEXT NOT NULL,
        questions TEXT NOT NULL,
        answers TEXT NOT NULL)''')
        #title name
        self.newwin.title(FILEentry.get())
        #label
        self.qlabel= Label(self.newwin, text='Questions:')#,command=self.RunInNewwin)
        self.qlabel.grid(row=0,column=0)
        #buttons
        self.runbutton= Button(self.newwin, text='RUN',command=RunExam)
        self.runbutton.grid(row=0,column=3)
        #self.savebutton= Button(self.newwin, text='SAVE')
        #self.savebutton.grid(row=0,column=4)
        self.addbutton= Button(self.newwin, text='+',width=7,command=self.NewQ)
        self.addbutton.grid(row=7, column=0)
        self.subbutton= Button(self.newwin, text='-',width=7, command=self.DELNW)
        self.subbutton.grid(row=7, column=1)
        #listbox
        self.listbox= Listbox(self.newwin, width=15, height=19)
        self.listbox.grid(rowspan=6, columnspan=2, row=1, column=0)
        self.listbox.bind('<<ListboxSelect>>',self.CurSelet)
        # create a vertical scrollbar to the right of the listbox
        self.yscroll= Scrollbar(self.newwin, command=self.listbox.yview, orient=VERTICAL)
        self.yscroll.grid(rowspan=6,row=1, column=2, sticky='ns')
        self.listbox.configure(yscrollcommand=self.yscroll.set)
        #dunno
        self.content1= StringVar()
        self.qname= Entry(self.newwin, width=30, textvariable=self.content1)
        self.qname.grid(row=1,column=3,columnspan=4)
        self.question= Text(self.newwin)
        self.question.grid(row=2,column=3,columnspan=4)
        self.content2= StringVar()
        self.answer= Entry(self.newwin, width=30, textvariable=self.content2)
        self.answer.grid(row=3,column=3,columnspan=4)
        self.question.insert(END,"""click here to put your question here\n
then press(+) button to add your work into the list box""")
        self.qname.insert(END,"click to put your question name here")
        self.answer.insert(END,"click to put your correct answer here")
        #other thingz
        self.cur.execute("SELECT * FROM Exam")
        self.rows = self.cur.fetchall()
        for row2 in self.rows:
            self.listbox.insert(END, row2)
            
    def CurSelet(self,event):
        #self.value=self.listbox.curselection()[0]
        self.selected_tuple=self.listbox.get(ANCHOR)
        self.qname.delete(0, END)
        self.qname.insert(END, self.selected_tuple[0])
        self.question.delete('1.0', END)
        self.question.insert(END, self.selected_tuple[1])
        self.answer.delete(0, END)
        self.answer.insert(END, self.selected_tuple[2])
        
    def NewQ(self):
        self.listbox.delete(0, END)
        self.getqname= str(self.qname.get())
        self.getq= str(self.question.get("1.0","end-1c"))
        self.getans= str(self.answer.get())
        self.cur.execute('''INSERT INTO Exam (qnames,questions,answers)
                    VALUES(?,?,?)''',(self.getqname,self.getq,self.getans))
        self.cur.execute("SELECT * FROM Exam")
        #self.cur.execute("SELECT * FROM Exam")
        self.rows= self.cur.fetchall()
        self.con.commit()
        for self.row2 in self.rows:
            self.listbox.insert(END, self.row2)

    def DELNW(self):
        self.listbox.delete(ANCHOR)
        self.cur.execute("DELETE FROM Exam WHERE qnames=(?)",
                         (self.qname.get(),))
        self.cur.execute("DELETE FROM Exam WHERE questions=(?)",
                         (self.question.get("1.0","end-1c"),))
        self.cur.execute("DELETE FROM Exam WHERE answers=(?)",
                         (self.answer.get(),))
        self.con.commit()

    def RUN(self):
        RunExam()

class RunExam():
    def __init__(self):
        #window
        self.newwin = Toplevel(window)
        #title name
        self.newwin.title(FILEentry.get())
        #connect sqlite
        self.con = sqlite3.connect(FILEentry.get()+'.db')
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS
        Exam(qnames TEXT NOT NULL,
        questions TEXT NOT NULL,
        answers TEXT NOT NULL)''')
        #title name
        self.newwin.title(FILEentry.get())
        #listbox
        self.listbox= Listbox(self.newwin, width=15, height=19)
        self.listbox.grid(rowspan=6, row=1, column=0)
        self.listbox.bind('<<ListboxSelect>>',self.CurSelet)
        # create a vertical scrollbar to the right of the listbox
        self.yscroll= Scrollbar(self.newwin, command=self.listbox.yview, orient=VERTICAL)
        self.yscroll.grid(rowspan=6,row=1, column=1, sticky='ns')
        self.listbox.configure(yscrollcommand=self.yscroll.set)
        #dunno
        self.qname= Text(self.newwin,height=3,width=15)
        self.qname.grid(row=0,column=2)
        self.question= Text(self.newwin,height=10,width=30)
        self.question.grid(row=1,column=2,columnspan=5)
        self.content2= StringVar()
        self.answer= Entry(self.newwin, width=30, textvariable=self.content2)
        self.answer.grid(row=2,column=2)
        self.RealAns= Text(self.newwin,height=10,width=30)
        self.RealAns.grid(row=3,column=2,rowspan=3)
        self.answerB= Button(self.newwin, text='Check', command=self.CHECK)
        self.answerB.grid(row=2,column=3)
        self.scorelabel= Label(self.newwin,text='/')
        self.scorelabel.grid(row=3,column=3)
        self.wronglabel= Label(self.newwin,text='X')
        self.wronglabel.grid(row=3,column=4)
        self.score= Text(self.newwin,height=1,width=3)
        self.score.grid(row=4,column=3)
        self.score.insert(END,int("0"))
        self.wrong= Text(self.newwin,height=1,width=3)
        self.wrong.grid(row=4,column=4)
        self.wrong.insert(END,int("0"))
        self.EndExam= Button(self.newwin, text='End Exam ', command=self.EndExam)
        self.EndExam.grid(row=0,column=3)
        self.selected_tuple=str(self.listbox.get(ANCHOR))
        #other thingz
        self.cur.execute("SELECT qnames, questions FROM Exam")
        self.rows = self.cur.fetchall()
        for row2 in self.rows:
            self.listbox.insert(END, row2)

    def CurSelet(self,event):
        #self.value=self.listbox.curselection()[0]
        self.selected_tuple=self.listbox.get(ANCHOR)
        self.qname.delete('1.0', END)
        self.qname.insert(END, self.selected_tuple[0])
        self.question.delete('1.0', END)
        self.question.insert(END, self.selected_tuple[1])
        


    def CHECK(self):
        #self.questionn = self.cur.execute(f"SELECT questions FROM Exam where qnames like '{self.selected_tuple}%'")
        self.con2 = sqlite3.connect('test.db')
        self.cur2 = self.con.cursor()
        self.getans = self.qname.get("1.0",'end-1c')
        self.cur2.execute(f"SELECT answers FROM Exam WHERE qnames='{self.getans}'")
        self.rows2 = self.cur2.fetchall()
        if self.answer.get()==self.rows2[0][0]:
            self.getscore1=int(self.score.get("1.0","end-1c"))
            self.s1=self.getscore1+1
            self.score.delete("1.0",END)
            self.score.insert(END,self.s1)
            self.RealAns.delete("1.0",END)
            self.RealAns.insert(END,'Correct\nasnswer:\n'+self.rows2[0][0])
            self.listbox.delete(ANCHOR)
        else:
            self.getscore2=int(self.wrong.get("1.0","end-1c"))
            self.s2=self.getscore2+1
            self.wrong.delete("1.0",END)
            self.wrong.insert(END,self.s2)
            self.RealAns.delete("1.0",END)
            self.RealAns.insert(END,'Correct\nasnswer:\n'+self.rows2[0][0])
            self.listbox.delete(ANCHOR)
            
    def EndExam(self):
        self.createFile=open(FILEentry.get()+".txt","w")
        self.createFile.write("Your Corrects of Exam:"+self.score.get("1.0","end-1c"))
        self.createFile.write("\nYour Wrongs of Exam:"+self.wrong.get("1.0","end-1c"))
        messagebox.showinfo("Info(?):", "This will end and create Txt File:\n(File Path):\n"+
                                 os.path.abspath(FILEentry.get()+'.txt'), icon="info")
        self.newwin.destroy()

def DEL():
    listbox.delete(ANCHOR)
    fname= FILEentry.get()+'.db'
    TOwatpat=str(os.path.abspath(fname))
    os.remove(TOwatpat)
    cur.execute("DELETE FROM examfilename WHERE namesoffile=(?)", (FILEentry.get(),))
    con.commit()

def CurSelet(evt):
    FILEentry.delete(0,END)
    #value=listbox.get(0, END)
    value=listbox.get(ANCHOR)
    FILEentry.insert(END, value)

window= tk.Tk()
window.title("Simulation Exam")
con = sqlite3.connect('aaaapy.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS
examfilename(namesoffile TEXT NOT NULL)''')

#listbox widget
listbox= Listbox(window, width=15, height=19)
listbox.grid(rowspan=20,row=0, column=0)
listbox.bind('<<ListboxSelect>>',CurSelet)
# create a vertical scrollbar to the right of the listbox
yscroll= Scrollbar(command=listbox.yview, orient=VERTICAL)
yscroll.grid(rowspan=20,row=0, column=1, sticky='ns')
listbox.configure(yscrollcommand=yscroll.set)

#forr entry
content= StringVar()
FILEentry= Entry(window, textvariable=content)
FILEentry.grid(row=1, column=2)

#forr buttonz
label= Label(window, text='Exam Filename:')
label.grid(row=0, column=2)
buttonOPEN= Button(window, text="OPEN", command=Open)
buttonOPEN.grid(row=2, column=2)
buttonADD= Button(window, text="NEW", command=New)
buttonADD.grid(row=3, column=2)
buttonDEL= Button(window,text="DELETE", command=DEL)
buttonDEL.grid(row=4, column=2)

#gui
cur.execute("SELECT * FROM examfilename")
rows = cur.fetchall()
for row in rows:
    listbox.insert(END, row)


window.mainloop()
