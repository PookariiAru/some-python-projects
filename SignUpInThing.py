from tkinter import *
#from tkinter import messagebox, Label, Button, FALSE, Tk, Entry
from tkinter import messagebox

#it's getting better
#users={'Andrew': 'Jandrew', 'Athena': 'Athena3rd'}
users={}
window = Tk()

def try_login():
    print("Trying to login...")
    #getuser=username_guess.get()
    #getpass=password_guess.get()
    if users.get(username_guess.get()) == password_guess.get():
        messagebox.showinfo("-- COMPLETE --", "WELCOME TO JUMANJI :D", icon="info")
    else:
        messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")
        
class add_user():
    def __init__(self):
        #window
        self.newwin = Toplevel(window)
        #entry boxes
        self.newusername_text = Label(self.newwin, text="New Username:")
        self.newusername = Entry(self.newwin)
        self.newpassword_text = Label(self.newwin, text="New Password:")
        self.newpassword = Entry(self.newwin, show="*")
        #button
        self.createbutton = Button(self.newwin, text ="create", command=self.newuser)
        #pack
        self.newusername_text.pack()
        self.newusername.pack()
        self.newpassword_text.pack()
        self.newpassword.pack()
        self.createbutton.pack()

    def newuser(self):
        print("Making new user...")
        if users.get(self.newusername.get()):
            messagebox.showinfo("-- ERROR --", "Username already exist!", icon="warning")
        else:
            users[self.newusername.get()] = self.newpassword.get()
            messagebox.showinfo("-- COMPLETE --", "WELCOME TO JUMANJI :D", icon="info")
            print(users)
            self.newwin.destroy()
             
#Gui Things
window.resizable(width=FALSE, height=FALSE)
window.title("SomeSignThingy")
window.geometry("200x150")

#Login the username & password entry boxes
username_text = Label(window, text="Username:")
username_guess = Entry(window)
password_text = Label(window, text="Password:")
password_guess = Entry(window, show="*")

#attempt to login button
attempt_login = Button(window, text="Login", command=try_login)
create_user = Button(window, text="New User?", command=add_user)

username_text.pack()
username_guess.pack()
password_text.pack()
password_guess.pack()
attempt_login.pack()
create_user.pack()

#Main Starter
window.mainloop()

