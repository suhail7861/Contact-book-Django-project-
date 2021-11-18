from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20,default='Name',blank=False)
    number=models.CharField(max_length=10,blank=False,default='number')
  

    def __str__(self):
        return self.name
        