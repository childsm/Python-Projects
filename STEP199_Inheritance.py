"""
STEP 199 - Inheritance Assignment

Python:  3.9.0

Author:  Michelle Childs

Purpose: The Tech Academy - Python Course
         Create two classes that inherit from another class
         Each child should have at least two attributes of their own
"""


class Pet: #the parent class
    #defining the parent attributes
    pet_name = 'No Name Provided'
    petType = ' '
    food = 'type of food'
    age = ' '

class reptile(Pet): #the child class
    #attributes just for the child class
    number_legs = 0
    habitat = ' '

class bird(Pet): #the child class
    #attributes just for the child class
    talks = 'No'
    feathers = 'Yes'
    wing_spann = 'inches'
