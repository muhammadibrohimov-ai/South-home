from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    
class Images(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='media/images')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Images"
        verbose_name_plural = 'Images'
        
    

class Home(models.Model):

    class StatusChoice(models.TextChoices):
        SALE = ['sale', 'Sale']
        RENT = ['rent', 'Rent']

    name = models.CharField(max_length=150)
    city = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    num_of_bathrooms = models.PositiveIntegerField()
    num_of_garages = models.PositiveIntegerField()
    main_image = models.FileField(upload_to='media/main_images')
    size = models.DecimalField(max_length=10, max_digits=8, decimal_places=2)
    is_new = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=StatusChoice.choices, default=StatusChoice.SALE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'
        
    
    
            
