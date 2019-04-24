from django.db import models
from django.urls import reverse
from django.db.models import F
import os

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
    picture = models.ImageField(upload_to ='media/')



class Category(models.Model):
    name = models.CharField(max_length=30, unique = True)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category', kwargs = {'category_slug':self.slug})


class Brand(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

def image_folder(instance,filename):
    return '{0}/{1}'.format(instance.slug,filename)

class Product(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=300)
    picture = models.ImageField(upload_to=image_folder)
    category = models.ForeignKey(Category, to_field='name', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=9, decimal_places=2,default = 0.00)
    available = models.BooleanField(default = True)
    slug = models.SlugField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs = {'product_slug':self.slug})


            
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    cost = models.DecimalField(max_digits=9, decimal_places=2,default = 0.00)
    total = models.DecimalField(max_digits=9, decimal_places=2,default = 0.00)

    def save(self, *args, **kwargs):
        self.cost = self.product.cost
        self.total = self.quantity * self.cost
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.product)

class PromoCode(models.Model):
    code = models.CharField(max_length=30,)
    title = models.CharField(max_length=30,)
    total = models.DecimalField(max_digits=9, decimal_places=2,default = 0.00)
    
class Cart(models.Model):
    products = models.ManyToManyField(CartItem)
    promocodes = models.ManyToManyField(PromoCode)
    total = models.DecimalField(max_digits=9, decimal_places=2,default = 0.00)

    def get_products(self):
        return "\n".join([str(p.product) for p in self.products.all()])

    def __unicode__(self):
        return str(self.id)
