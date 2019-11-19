import os
import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
#from PIL import Image, ImageTk #png用的

root=tk.Tk()
root.resizable(0,0)
root.geometry('540x55')
root.title("YTBDL v2.1 By Rick20191119")
#root.configure(background='black') #改視窗底色


#文字Label
step1 = ttk.Label(text="Step.1 Add Address Here", width=25)
step2 = ttk.Label(text="Step.2 Choose Format", width=25)

#取得當前目錄路徑
Tpath = os.getcwd()

#產生輸入資料用的Entry
e = tk.Entry(root, show=None)

#第一次執行沒有OUTPUT資料夾時，建立所有輸出用資料夾
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
		messagebox.showinfo("Mission Completed", "The MP3 file is in Output - MP3 folder")
	elif ftype == 1:
		os.system("move *.mp4 ./Output/720P")
		messagebox.showinfo("Mission Completed", "The MP4 file is in Output - 720P folder")
	elif ftype == 2:
		os.system("move *.mp4 ./Output/1080P")
		messagebox.showinfo("Mission Completed", "The MP4 file is in Output - 1080P folder")
	else:
		os.system("move *.webm ./Output/4K")	
		messagebox.showinfo("Mission Completed", "The 4K WEBM file is in Output - 4K folder")
		
						
#定義各按鈕文字及呼叫程式
button1=ttk.Button(root, text="720P", command=click720)
button2=ttk.Button(root, text="1080P", command=click1080)
button3=ttk.Button(root, text="4K", command=click4k)
button4=ttk.Button(root, text="MP3", command=clickMP3)

#定義各區塊放置位置
step1.grid(column=1,row=0)
step2.grid(column=1,row=1)
e.grid(column=2,row=0, columnspan=4, sticky=W+E)#w+e為左右延展
#e.grid_columnconfigure(2, weight=1)
button1.grid(column=2,row=1)
button2.grid(column=3,row=1)
button3.grid(column=4,row=1)
button4.grid(column=5,row=1)


root.mainloop()