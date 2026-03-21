from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)
    
 # model configuration (database + admin display)
    class Meta:
        db_table = 'countries_table'  # custom table name in database
       
    def __str__(self):
        return self.name

