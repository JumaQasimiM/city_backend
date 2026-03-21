from django.db import models

from country.models import Country
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

 # model configuration (database + admin display)
    class Meta:
        db_table = 'cities_table'  # custom table name in database
        verbose_name = 'City'  # singular name in admin panel
        verbose_name_plural = 'cities' # plural name in admin panel
  
    def __str__(self):
        return self.name



class CityImage(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE,related_name='city_image')
    image = models.ImageField(upload_to='cities')

 # model configuration (database + admin display)
    class Meta:
        db_table = 'cities_image_table'  # custom table name in database
        
    def __str__(self):
        return f"Image for - {self.city.name}"
