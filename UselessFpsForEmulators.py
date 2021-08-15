from tkinter import *
import pyautogui
import keyboard
import subprocess

window = Tk()

s = subprocess.check_output('tasklist', shell=True)

def start_fps():
    before = pyautogui.position()
    if "<insert android emulating program here>.exe".encode() in s:
        print("<insert android emulating program here>.exe is running")
        while True:
            current = pyautogui.position()
            if before != current:
                pyautogui.mouseDown(button='left')
                pyautogui.moveTo(pyautogui.size()[0]/2,pyautogui.size()[0]/4)
            before = current
            if keyboard.is_pressed('ctrl+c'):
                print('ctrl+c was pressed!')
                break

startbutton = Button(window, text="Start", command=start_fps)
startbutton.pack()
endbutton = Label(window, text="ctrl+c to end")
endbutton.pack()

if __name__ == "__main__":
    window.mainloop()
