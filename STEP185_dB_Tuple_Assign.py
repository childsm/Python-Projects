"""
STEP 185 - Write a script that creates a database & adds new data

Python:  3.9.0

Author:  Michelle Childs

Purpose: The Tech Academy - Python Course
         Create a database with a table. Then sort through a list and add
         specific owns into the database.         
"""

import sqlite3

conn = sqlite3.connect('test.db') #is going to hold the connection to the database

with conn: #while the connection is open to the dB
    cur = conn.cursor() #invoke the cursor object and giving it the name 'cur'
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_file( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )') #passing in a string and the backslash escape key allows continuation
            #of text to the next line
    conn.commit() #to commit any changes that were made
conn.close() #have to be sure and close the 'with' statement


conn = sqlite3.connect('test.db') #connecting to database again


#tuple of files
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#loop through each file in the tuple to find the names that end in y.
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
        #each row will be one name out of the tuple so (x,)
        #will denote a one-element tuple for each file ending in txt
            cur.execute('INSERT INTO tbl_file (col_file) VALUES(?)', (x,))
            conn.commit()
            print(x) #printing the files that end in 'txt' to the console
conn.close()
