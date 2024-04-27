
import pygame
import tkinter as tkr
import PySimpleGUI as psg
from tkinter.filedialog import askdirectory
import os
from tkinter import *

# from tkinter.ttk import *
 
# creating Tk window
master = Tk()
master.title('Music Player')
master.geometry("800x600")
master.resizable(False,False)


def add():

    directory = askdirectory()

    os.chdir(directory)

    song_list = os.listdir()

    for item in song_list:
        pos = 0
        play_list.insert(pos, item)
        pos += 1
    pygame.init()
    pygame.mixer.init()



def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()



# creating a Fra, e which can expand according
# to the size of the window
def helloCallBack():
    psg.popup("About",'This Application Was Devoloped By \n RAGHUL V \n\nPython Version 3.10 \nApplication Version 1.0')
    
   
l = tkr.Label(master,text="Music Player By RAGHUL V",anchor='nw').pack(side='top',pady=0)
B = tkr.Button(master , text =" About ", command = helloCallBack).pack(side='top',anchor='ne',padx=15,pady=0)
pane = Frame(master)

pane.pack(fill = BOTH, expand = True)
 
# button widgets which can also expand and fill
# in the parent widget entirely
# Button 1

fs = Frame(pane)
fs.pack()

play_list = tkr.Listbox(fs, font="Helvetica 12 bold", bg= 'DarkGrey', selectmode=tkr.SINGLE,height=22,width=300)
play_list.pack(padx=10,pady=10)

var = tkr.StringVar() 
song_title = tkr.Label(pane, font="Helvetica 12 bold", textvariable=var)
song_title.pack(padx=5,pady=5)

b1 = Button(pane, background = "DarkGrey", fg = "Black", text="Brouse", command=add,)
b1.pack(side = LEFT, expand = True, fill = BOTH,pady=10,padx=10)
 
# Button 2
b2 = Button(pane, background = "DarkGrey", fg = "Black",text="PLAY", command=play)
b2.pack(side = LEFT, expand = True, fill = BOTH,pady=10,padx=10)
 
# Button 3
b3 = Button(pane, background = "DarkGrey", fg = "Black", text="STOP", command=stop)
b3.pack(side = LEFT, expand = True, fill = BOTH,pady=10,padx=10)

b4 = Button(pane, background = "DarkGrey", fg = "Black",text="PAUSE", command=pause)
song_title.pack(padx=5,pady=5)
b4.pack(side = LEFT, expand = True, fill = BOTH,pady=10,padx=10)
 
# Button 2
b5 = Button(pane, background = "DarkGrey", fg = "Black",text="UPAUSE", command=unpause)
b5.pack(side = LEFT, expand = True, fill = BOTH,pady=10,padx=10)
 
 
# Execute Tkinter
master.mainloop()
