from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)

    # model configuration (database + admin display)
    class Meta:
        db_table = 'categories_table'  # custom table name in database
        verbose_name = 'Category'  # singular name in admin panel
        verbose_name_plural = 'Categories'  # plural name in admin panel
    
    
    def __str__(self):
        return self.title
    
