from email import message
from django.db import models

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=400)
    message = models.TextField(max_length=1000,null=True)
    def __str__(self):
        return self.name

class Package(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    image_url = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Location(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    image_url = models.ImageField(upload_to='images/',default='logo.png')
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Gallery(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name