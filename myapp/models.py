from django.db import models

# Create your models here.
class Customer(models.Model):
    first_Name = models.CharField(max_length=120)
    last_Name = models.CharField(max_length=120)
    phone_Number = models.CharField(unique=True,max_length=40)
    email_Address = models.EmailField(unique=True)
    message = models.CharField(max_length=200)


    def __str__(self):
        return self.first_Name
