#Basic model/schema for our product
#models.py is our database and Objects is the model manager

from django.db import models

TYPE_CHOICES = (
    ('appetizers','appetizers'), #tuples
    ('entrees','entrees'),
    ('treats','treats'),
    ('drinks','drinks'),
)

class Product(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)  #to define a field I have to invoke 'models'
    name = models.CharField(max_length=60, default="", blank=True, null=False)
#line6 -can have max of 60 char, start empty, in site forms can be blank, but in db it must have something
#line6 -could put 'blank=False' then an error would show if user left field blank on form
    description = models.TextField(max_length=300, default="", blank=True)
    price = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    image = models.CharField(max_length=255, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name  # invoking Python's built in module string
        # the above takes "Product object(1)" and turns it to a string. So name is returned instead of object
