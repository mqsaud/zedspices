from django.db import models


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
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    credit = models.URLField(max_length=1024)

    def __str__(self):
        return self.name
        
