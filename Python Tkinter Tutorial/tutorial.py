import tkinter
from tkinter import *
import webbrowser

win = Tk()
win.iconbitmap("icon.ico")
win.geometry("420x420")
win.title("Tutorial Tkinter Python | BY HarleyB")

def subscribe():
    url = 'https://www.youtube.com/channel/UCNBmZMcEUa3MrBQ9ScpDAjQ'
    webbrowser.open(url)
    print("Opened Browser!")

def github():
    url = 'https://github.com/Harley2787/UpdateTimers'
    webbrowser.open(url)
    print("Opened Browser!")

def friend():
    url = 'https://lazyllama.xyz/'
    webbrowser.open(url)
    print("Opened Browser!")

sub2me = tkinter.Button(win, text=f"Sub To Me On Youtube!", command=subscribe)
git = tkinter.Button(win, text=f"Go Check out my Github Projects!", command=github)
sub2me.pack()
git.pack()
checkfriend = tkinter.Button(win, text=f"Go Check out My friend!", command=friend).pack()

win.mainloop()
