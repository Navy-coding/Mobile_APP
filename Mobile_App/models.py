from django.db import models
#from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Order(models.Model):
    customer = models.ForeignKey('User', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date = models.DateTimeField(auto_now_add=True)



    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def generate_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

