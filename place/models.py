from django.db import models

from django.conf import settings

from city.models import City
from category.models import Category


# services 
class Service(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Place(models.Model):
    CATEGORY_CHOICES =[
        ('tourist','Tourist Attraction'),
        ('market','Market'),
        ('restaurant','Restaurant'),
        ('park','Park'),
        ('museum','Museum'),
        ('hotel','Hotel'),
        ('hospital','Hospital'),
        ('other','Other')
    ]
    name = models.CharField(max_length=40)
    description = models.TextField( blank=True,null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True,related_name='places')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True,blank=True,related_name='places')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,blank=True,related_name='places')
    services = models.ManyToManyField(Service,related_name='places')
    # geo
    latitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)
    longitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)
    # addrerss
    address = models.CharField(max_length=300, blank=True)
    # other descriptions
    opening_hours = models.CharField(max_length=100,blank=True)
    contact_number = models.CharField(max_length=20,blank=True,null=True)
    website = models.URLField(blank=True,null=True)
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
  
    # show in admin panel
    def __str__(self):
        return self.name


# place images model
class PlaceImage(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='places/') # '/media/place/' (save)

    def __str__(self):
        return f'Image for {self.place.name}'

# favorate place
class FavoratePlace(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,blank=True,related_name='favorate_user')
    place = models.ForeignKey(Place,on_delete=models.CASCADE,related_name='favorates')

    def __str__(self):
        return f'{self.user.username} add to favorate [ {self.place.name} ]' 
    
# place commetns 
class PlaceComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,blank=True,related_name='comment_user')
    place = models.ForeignKey(Place,on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField(null=False,blank=False)

    def __str__(self):
        return f"{self.user.username} comment - [ {self.comment} ] to {self.place.name} "
# place like
class PlaceLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,blank=True,related_name='like_uers')
    place = models.ForeignKey(Place,on_delete=models.CASCADE,related_name='likes')

    def __str__(self):
        return f" '{self.user.username}' liked {self.place.name}"