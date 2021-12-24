# Mods
import tkinter
from tkinter import *
import webbrowser

win = Tk()
win.iconbitmap("icon.ico") # Any icon file rename it but file must be .ico
win.geometry("420x420") # 420 Obv
win.title("Tutorial Tkinter Python | BY HarleyB")

def subscribe():
    url = 'https://www.youtube.com/channel/UCNBmZMcEUa3MrBQ9ScpDAjQ'
    webbrowser.open(url)
    print("Opened Browser!")
    # Put more code here if you want :D

def github():
    url = 'https://github.com/Harley2787/UpdateTimers'
    webbrowser.open(url)
    print("Opened Browser!")
    # Put more code here if you want :D

def friend():
    url = 'https://lazyllama.xyz/'
    webbrowser.open(url)
    print("Opened Browser!")
    # Put more code here if you want :D

sub2me = tkinter.Button(win, text=f"Sub To Me On Youtube!", command=subscribe) # Button Creating Needs packed see line 29
git = tkinter.Button(win, text=f"Go Check out my Github Projects!", command=github) # Button Creating Needs packed see line 30
sub2me.pack() # Packing Them Into the GUI
git.pack() # Packing Them into the GUI
checkfriend = tkinter.Button(win, text=f"Go Check out My friend!", command=friend).pack() # automatically packs the check friend how ever you cannot .config this

win.mainloop()
# I Hope this tutorial helps you develop some awesome gui's using tkinter!
