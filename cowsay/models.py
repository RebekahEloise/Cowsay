from django.db import models

# Create your models here.
class Cowsay(models.Model):
    cowsay_str = models.CharField(max_length=100)

    def __str__(self):
        return self.cowsay_str 