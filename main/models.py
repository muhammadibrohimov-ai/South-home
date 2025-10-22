from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
import string
import random

# Create your models here.


# Model SoftDelete

class SoftDeleteModel(models.Model):
    is_delete = models.BooleanField(default=False, editable=False)
    
    
    class Meta:
        abstract = True
        
        
    def delete(self, *args, **kwargs):
        self.is_delete = True
        self.save(*args, **kwargs)


# Model category

class Category(SoftDeleteModel):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        
            
    
# Model Home

class Home(SoftDeleteModel):

    class StatusChoice(models.TextChoices):
        SALE = ('sale', 'Sale')
        RENT = ('rent', 'Rent')

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200)
    city = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    num_of_bathrooms = models.PositiveIntegerField()
    num_of_garages = models.PositiveIntegerField()
    main_image = models.FileField(upload_to='media/main_images')
    size = models.DecimalField(max_digits=8, decimal_places=2)
    is_new = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=StatusChoice.choices, default=StatusChoice.SALE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            chars = string.ascii_lowercase + string.digits

            while Home.objects.filter(slug=slug).exists():
                random_part = ''.join(random.choices(chars, k=random.randint(5, 10)))
                slug = f"{base_slug}-{random_part}"

            self.slug = slug 

        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'
        
        
# Model Images

class Images(SoftDeleteModel):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='media/images')
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Images"
        verbose_name_plural = 'Images'
        
        
# Model contact

class Contact(SoftDeleteModel):
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    
    def save(self, *args, **kwargs):
        
        if not self.pk and Contact.objects.exists():
            raise ValidationError("Faqatgina 1 ta contact yartish mumkin")

        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
    
    
        
# Model client

class Client(SoftDeleteModel):
    name = models.CharField(max_length=150)
    profession = models.CharField(max_length=200)
    text = models.TextField()
    title = models.CharField(max_length=150)
    image = models.FileField(upload_to='clients/')
    
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Client'
            
