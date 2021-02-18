"""
The Tech Academy - Python Course STEP 236 - Encapsulation

Python:  3.9.0

Author:  Michelle Childs
"""

class User: #1 & 2 a class that uses a private and protected attribute or function

    def __init__(self):
        self.__age = 39 

    def numYears(self): 
        print(self.__age)

    def agePrivate(self, private):
        self.__age = private

    def __init__(self):  #2 a protected attribute or function
        self._phone = '555-555-5555'

Susan = User() #3 an object that uses private and protected
Susan.agePrivate(29)
Susan.numYears()
Susan._phone = 'XXX-XXXX-XXXX'
print(Susan._phone)

