from django.db import models

from django.contrib.auth.models import User

from city.models import City
from category.models import Category


# Create your models here.
# services 
class Service(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Place(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField( blank=True,null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True,related_name='places')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True,blank=True,related_name='places')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True,related_name='places')
    services = models.ManyToManyField(Service,related_name='places')
    register_date = models.DateField(auto_now=True)
    
 # model configuration (database + admin display)
    class Meta:
        db_table = 'places_table'  # custom table name in database
        verbose_name = 'Place'  # singular name in admin panel
        verbose_name_plural = 'places' # plural name in admin panel
        ordering = ['city','-register_date']
        indexes = [
            models.Index(fields=['name','category'])
        ]
  
    def __str__(self):
        return self.name


# place images model
class PlaceImage(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='places/') # '/media/place/' (save)

    def __str__(self):
        return f'Image for {self.place.name}'
