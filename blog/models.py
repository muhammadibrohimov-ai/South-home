from django.db import models

# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name



class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='blog/')
    desc = models.TextField()
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comments = models.PositiveIntegerField(default=0)
    
    
    def __str__(self):
        return self.title