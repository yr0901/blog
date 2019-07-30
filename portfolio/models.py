from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'image/')
    description = models.CharField(max_length= 500)

    def __str__(self):
        return self.title