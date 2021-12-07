from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ Define Category Model """

    class Meta:
        verbose_name ='Category'
        verbose_name_plural = 'Categroies'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ Return Category Names """
        return self.name

    def get_friendly_name(self):
        """ Return Friendly Names """
        return self.friendly_name


class Product(models.Model):
    """ Define Product Model """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    size = models.CharField(max_length=25, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    credit = models.URLField(max_length=1024)

    def __str__(self):
        return self.name


class RateAndReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    rating = models.FloatField()
    review = models.TextField()
    status = models.BooleanField()
    created_on_date = models.DateTimeField(auto_now_add=True)
    updated_on_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
