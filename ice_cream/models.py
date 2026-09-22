from django.db import models

class Wrapper(models.Model):
    title = models.CharField(max_length=256)
    is_published = models.BooleanField(True)

class Topping(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    is_published = models.BooleanField(True)

class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)
    is_published = models.BooleanField(True)

class IceCream(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_on_main = models.BooleanField(False)
    is_published = models.BooleanField(True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    toppings = models.ManyToManyField(Topping)
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL
    )

