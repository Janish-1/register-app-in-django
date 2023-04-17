from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    dob = models.DateField()
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    secques = models.CharField(max_length=100)
    #Creating a sql database for model
    class Meta:
        db_table="account_user"