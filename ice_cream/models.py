from django.db import models

class Wrapper(models.Model):
    title = models.CharField(max_length=256)
    is_published = models.BooleanField(True)

class Topping(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    is_published = models.BooleanField(True)

class IceCream(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_on_main = models.BooleanField(False)
    is_published = models.BooleanField(True)

class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.IntegerField(default=100, validators = [MaxValueValidator(32767), MinValueValidator(0)] )
    is_published = models.BooleanField(True)

