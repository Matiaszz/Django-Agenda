from django.db import models
import django.utils.timezone as tz
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    # models.CharField(max_length=50) -> string
    # models.EmailField(max_length=254) -> type: email

    # blank = True -> void fields are enabled
    # 60 because the longest name has 58 letters
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=tz.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)

    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    # creating a folder named pictures, inside, a folder with year, and inside
    # of folder year, a folder with the months
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
