#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

### A GUI interface using Tkinter to do data backups of MySQL###

import os, sys, datetime
from tkinter import filedialog
from tkinter import *


###This is the primary window every other frame will fit into###

###class MainContainerWindow(Tk):
    
def __init__(self, master=None):
	tkinter.Tk.__init__(self, master)

def initialize(self):
	self.grid()
	self.grid_columnconfigure(0, weight=1)
   
      ###The file menu here to build.###

def onExit(self):
	self.quit()        
        
def OnPressTab(self, event):
	self.textvariable.get()
	text = self.textvariable
        
def NewFile():
	name = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
	text = textvariable
	name.write(text)
	name.close()
	print ("name")
    
def OpenFile():
	name = filedialog.askopenfilename()
	print ("name")

def saveAs():
	name = filedialog.SaveAs(mode = 'w', defaultextension = ".txt")

    
MainContainerWindow = Tk()
menubar = Menu(MainContainerWindow)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command = NewFile)
filemenu.add_command(label = "Open", command = OpenFile)
filemenu.add_command(label = "Save", command = NewFile)
filemenu.add_command(label = "Save as...", command = NewFile)
filemenu.add_command(label = "Close", command = MainContainerWindow.quit)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = MainContainerWindow.quit)
menubar.add_cascade(label = "File", menu = filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label = "Undo", command = NewFile)

editmenu.add_separator()

editmenu.add_command(label = "Cut", command = ("<<Cut>>"))
editmenu.add_command(label = "Copy", command = NewFile)
editmenu.add_command(label = "Paste", command = NewFile)
editmenu.add_command(label = "Delete", command = NewFile)
editmenu.add_command(label = "Select All", command = NewFile)

menubar.add_cascade(label = "Edit", menu = editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Help Index", command = NewFile)
helpmenu.add_command(label = "About...", command = NewFile)
menubar.add_cascade(label = "Help", menu = helpmenu)






MainContainerWindow.config(menu = menubar)
MainContainerWindow.title("MySQL Database Backup")
MainContainerWindow.mainloop()