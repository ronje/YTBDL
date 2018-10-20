import os
import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image

root=tk.Tk()
root.resizable(0,0)
root.geometry('540x55')
root.title("YTBDL v2.0 By Rick20181020")
#bm = PhotoImage(file = 'Mario2.png')
#BACKG = Label(root, image = bm)

l1 = ttk.Label(text="Step.1 Add Address Here", width=25)
l2 = ttk.Label(text="Step.2 Choose Format", width=25)
Tpath = os.getcwd()
e = tk.Entry(root, show=None)
path = ".\Output"
if not os.path.isdir(path):
	os.mkdir(path)
	os.mkdir(path+"\\MP3")
	os.mkdir(path+"\\720P")
	os.mkdir(path+"\\1080P")
	os.mkdir(path+"\\4K")


def clickMP3():
	var = e.get()
	print( Tpath+"\\bin\youtube-dl.exe")
	os.system(Tpath+"\\bin\youtube-dl.exe --extract-audio --audio-format mp3 "+var)
	fend(0)
	
def click720():
	var = e.get()
	os.system(Tpath+"\\bin\youtube-dl.exe -f 136+140 "+var)
	fend(1)
def click1080():
	var = e.get()
	os.system(Tpath+"\\bin\youtube-dl.exe -f 137+140 "+var)
	fend(2)
def click4k():
	var = e.get()
	os.system(Tpath+"\\bin\youtube-dl.exe -f 313+251 "+var)
	fend(3)

def fend(ftype): #結束用
	if ftype == 0:
		os.system("move *.mp3 ./Output/MP3")
		messagebox.showinfo("Mission Completed", "The MP3 file is in Output\MP3 folder")
	elif ftype == 1:
		os.system("move *.mp4 ./Output/720P")
		messagebox.showinfo("Mission Completed", "The MP4 file is in Output\720P folder")
	elif ftype == 2:
		os.system("move *.mp4 ./Output/1080P")
		messagebox.showinfo("Mission Completed", "The MP4 file is in Output\1080P folder")
	else:
		os.system("move *.webm ./Output/4K")	
		messagebox.showinfo("Mission Completed", "The 4K WEBM file is in Output\4K folder")
		

button1=ttk.Button(root, text="720P", command=click720)
button2=ttk.Button(root, text="1080P", command=click1080)
button3=ttk.Button(root, text="4K", command=click4k)
button4=ttk.Button(root, text="MP3", command=clickMP3)

l1.grid(column=1,row=0)
l2.grid(column=1,row=1)
e.grid(column=2,row=0, columnspan=4, sticky=W+E)
#e.grid_columnconfigure(2, weight=1)
button1.grid(column=2,row=1)
button2.grid(column=3,row=1)
button3.grid(column=4,row=1)
button4.grid(column=5,row=1)
#BACKG.grid(columnspan=5)

root.mainloop()