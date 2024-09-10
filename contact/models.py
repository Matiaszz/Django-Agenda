from django.db import models
import django.utils.timezone as tz


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

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
