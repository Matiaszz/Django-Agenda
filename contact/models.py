from django.db import models
import django.utils.timezone as tz


class Category(models.Model):
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

    # cria uma pasta chamada pictures, dentro dela tem uma pasta com o ano
    # e dentro do ano, tem os meses daquele ano
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
