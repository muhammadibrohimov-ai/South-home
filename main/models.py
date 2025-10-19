from django.db import models
from django.core.exceptions import ValidationError

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
        
        
class Contact(models.Model):
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    
    def save(self, *args, **kwargs):
        
        if not self.pk and Contact.objects.exists():
            raise ValidationError("Faqatgina 1 ta contact yartish mumkin")

        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.phone
    
    
        
        
class Client(models.Model):
    name = models.CharField(max_length=150)
    preofession = models.CharField(max_length=200)
    text = models.TextField()
    title = models.CharField(max_length=150)
    image = models.FileField(upload_to='clients/')
    
    
    def __str__(self):
        return self.name
    
            
