from django.db import models

# Create your models here.
class House(models.Model):
    logo = models.ImageField(upload_to="images/")
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    price = models.IntegerField()
    garage = models.IntegerField()
    bedroom = models.IntegerField()
    size = models.IntegerField(max_length=50)