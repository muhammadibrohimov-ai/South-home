from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password = None, **extra_fields):
        if not phone:
            raise ValueError("Foydalanuvhci teledon raqamini kiritshi muajburiy")
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, phone, password = None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not password:
            raise ValueError("Superuser uchun parol majburiy")

        return self.create_user(phone, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    profession = models.CharField(max_length=50, blank=True)
    image = models.FileField(upload_to='users', blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)



    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

