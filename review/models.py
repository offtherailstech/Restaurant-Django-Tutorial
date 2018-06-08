from django.db import models
from django.utils.text import slugify
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    state = USStateField(choices=STATE_CHOICES)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Restaurant, self).save()


class Dish(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    slug = models.SlugField(unique=True)
    url_slug = models.SlugField(unique=False)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.restaurant) + "-" + self.name)
        self.url_slug = slugify(self.name)
        super(Dish, self).save()
