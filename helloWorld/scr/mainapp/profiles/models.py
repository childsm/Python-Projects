from django.db import models

# Create your models here.


PREFIX_OPTION = (
    ('Mr','Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
)

class Profiles(models.Model):
    Prefix = models.CharField(max_length=60, default="", choices=PREFIX_OPTION)
    First_Name = models.CharField(max_length=30, default="", blank=False, null=False)
    Last_Name = models.CharField(max_length=30, default="", blank=False, null=False)
    Email = models.EmailField(max_length=254) #Email = models.CharField(max_length=254, EmailVarify)
    Username = models.CharField(max_length=60, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.First_Name #invoking Python's built in module string
        #the above takes "Product object(1)" and turns it to a string. So name is returned instead of object

