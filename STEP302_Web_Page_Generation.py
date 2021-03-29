"""
The Tech Academy - Python Course STEP 302 & 303 - Web Page Generator Part 1 & 2

Python:  3.9.0

Author:  Michelle Childs

Tested OS: Code written and tested with Windows 10.
"""

import webbrowser #necessary to open an html file in a browser from python
from tkinter import *
from tkinter import filedialog as fd
import tkinter as tk


class ParentWindow(Frame): 
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.title('Post What\'s on Your Mind')
        self.master.configure(bg='#F0F0F0')

#creating the text box for user input
        self_myText = Text(self.master, width=40, height=10, font=('Helvetica', 12))
        self_myText.grid(row=0, column=0, columnspan=2, padx=(20,20), pady=(20,20))

#creating button for clearing text box
        self_clear = Button(self.master, text='Clear Screen', command=lambda: clear(self))
        self_clear.grid(row=1, column=0, pady=(0,10))

#creating button to get text and 'post' it to web
        self_get_text = Button(self.master, text='Post Text', command=lambda: postText(self))
        self_get_text.grid(row=1, column=1, pady=(0,10))


#function for clearing text box if user changes mind on what they want to say
        def clear(self): 
            self_myText.delete(1.0, END)
            return

        def postText(self):
            userPost = self_myText.get(1.0, END)
            web = open("STEP302_WebPage.html","w")
            web.write("<html>\n<body>\n<h1> \n{} \
                        </h1>\n</body>\n</html>".format(userPost))
            web.close()
            edge = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
            webbrowser.get(edge).open_new_tab("STEP302_WebPage.html")


if __name__ == '__main__':
    root = tk.Tk() 
    App = ParentWindow(root) 
    root.mainloop()
