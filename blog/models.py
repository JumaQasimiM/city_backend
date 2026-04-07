from django.db import models
from django.conf import settings
from category.models import Category

class Blog(models.Model):
    title = models.CharField(max_length=300)
    slug  = models.SlugField(unique=True)
    description = models.TextField()
    image  = models.ImageField(upload_to='blog/')
    tags = models.CharField(max_length=50)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,blank=True,related_name='blogs')
    views = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # one time
    updated_at = models.DateTimeField(auto_now=True) # after evry save

    class Meta:
        db_table = 'blogs'


    def __str__(self):
        return self.title
     

# blog comment  
class BlogComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,blank=True,related_name='blog_comments')
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField(null=False,blank=False)

    class Meta:
        db_table = 'blog_comments'

    def __str__(self):
        # maybe the user be null (on_delete = set_null)
        username = self.user.username if self.user else 'Anonymous'
        return f"{username} comment - [ {self.comment} ] to {self.blog.title} "