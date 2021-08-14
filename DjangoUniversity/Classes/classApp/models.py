#from django.db import models
#Basic model/schema for our product
#models.py is our database and Objects is the model manager

from django.db import models

class djangoClasses(models.Model):
    Title = models.CharField(max_length=128, default="", blank=True, null=False)  #to define a field I have to invoke 'models' every time
    Course_Number = models.IntegerField() #didn't see any field parameters options for integer at docs.djangoproject.com
    Instructor_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.FloatField() #same thing here as for integer

    objects = models.Manager()

    def __str__(self):
        return self.Title  #this is to display something discriptive and useful for an item in the class
