from django.db import models
from django.db.models.functions import Lower

class Category(models.Model):
    title = models.CharField(max_length=50)

    # model configuration (database + admin display)
    class Meta:
        db_table = 'categories_table'  # custom table name in database
        verbose_name = 'Category'  # singular name in admin panel
        verbose_name_plural = 'Categories'  # plural name in admin panel

        constraints = [ # title must be unique 
            models.UniqueConstraint(
                Lower('title'),
                name='unique_lower_title'
            )
        ]
    
    
    def __str__(self):
        return self.title
    

