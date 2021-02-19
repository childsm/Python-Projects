"""
Python Course STEP 238 - Abstraction assignment

Python:  3.9.0

Author:  Michelle Childs
"""

from abc import ABC, abstractmethod

class cart(ABC):

    def checkOut(self, amount):
        print('Your purchasing total is',amount)
#this function is telling us to pass in an argument, but we won't tell you how
#or what kind of data it will be
    @abstractmethod
    def payment(self, amount):
        pass

#2 child class that defines implementation of parent abstract method
class CreditCardPayment(cart): 
    
    def payment(self,amount):
        limit = '$250'
        print('We\'re sorry, but your new purchase of {} \
                \nhas exceeded your {} limit. \nAGAIN!'.format(amount,limit))

amount = '$251'
order = CreditCardPayment()
order.checkOut(amount)
print()
order.payment(amount)

