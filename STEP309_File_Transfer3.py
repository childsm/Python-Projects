"""
The Tech Academy - Python Course STEP 309 - File Transfer 3

Python:  3.9.0

Author:  Michelle Childs

Purpose: Make a user interface script that allows for user to specify source and destination folders
         for moving files that were modified or created in the last 24 hrs.

Tested OS: Code written and tested with Windows 10.
"""

#importing tkinter for GUI
from tkinter import *
from tkinter import filedialog as fd
import tkinter as tk

#import modules for moving files
import shutil
import os.path
import time

class ParentWindow(Frame): #the very first frame (or class)
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.title('Check Folders')
        self.master.configure(bg='#F0F0F0')

        self_myText = Text(self.master, width=40, height=3, font=('Helvetica', 12))
        self_myText.grid(row=0, column=0, padx=(20,20), pady=(20,10))

        self_getSrc = Button(self.master, text='Source Folder', command=lambda: source(self))
        self_getSrc.grid(row=1, column=0, pady=(0,10))

        self_myText2 = Text(self.master, width=40, height=5, font=('Helvetica', 12))
        self_myText2.grid(row=2, column=0, padx=(20,20), pady=(20,10))

        self_getDest = Button(self.master, text='Destination Folder', command=lambda: destination(self))
        self_getDest.grid(row=3, column=0, pady=(0,20))

        self_btn_chkFile = Button (self.master, text= 'File Check', font=('Helvetica', "12", 'bold italic'), command=lambda: moveFiles(self))
        self_btn_chkFile.grid(row=4, column=0, padx=(0,5), pady=(0,5), sticky=E)
           
        def source(self):
            self_myText.delete(1.0, END)
            src = fd.askdirectory(initialdir='/') #get file source folder
            self_myText.insert(1.0, src)
            return src

        def destination(self):
            self_myText2.delete(1.0, END)
            dest = fd.askdirectory(initialdir='/') #get file destination folder
            self_myText2.insert(1.0, dest)
            return dest

        def moveFiles(self):
            #see what's in source directory
            src = self_myText.get(1.0, END)
            srcUse = src[:-1]
            filesA = os.listdir(srcUse)
            print(filesA)
 
            #see what's in destination directory
            dest = self_myText2.get(1.0, END)
            destUse = dest[:-1]
            filesB = os.listdir(destUse)
            print(filesB)

            #change the directory (so I don't have to enter the full path)
            os.chdir(srcUse)

            #use seconds to easily find files that were modified in the last 24 hrs
            oneDay = 24*60*60
            now = time.time()
            before = now - oneDay
            #last_mod_time()

            def last_mod_time(fname):
                return os.path.getmtime(fname)

            for fname in filesA:
                if last_mod_time(fname) > before:
                    shutil.move(fname, destUse)
                    print(fname) #see which files were moved


if __name__ == '__main__':
    root = tk.Tk() 
    App = ParentWindow(root)
    root.mainloop()


