from django.db import models

from django.contrib.auth.models import User

from city.models import City
from category.models import Category

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField( blank=True,null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True,blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    

    def __str__(self):
        return self.name


# place images model
class PlaceImage(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='places/') # '/media/place/' (save)

    def __str__(self):
        return f'Image for {self.place.name}'
