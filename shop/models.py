from django.db import models
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

# Create your models here.
class UserIpStore(models.Model):
    userip=models.CharField(max_length=200)
    countryname=models.CharField(max_length=200)
    regionname=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    latitude=models.CharField(max_length=200)
    longitude=models.CharField(max_length=200)
    def __str__(self):
        return "{} {} {} {}".format(self.userip , self.city , self.regionname, self.countryname)
    
class Category(models.Model):
    name=models.CharField(max_length=200,
                            db_index=True)
    slug=models.SlugField(max_length=200,
                            unique=True) 

    class Meta:
        ordering=('name',)
        verbose_name ='category'
        verbose_name_plural='categories'                                              

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,unique=True)
    image=models.ImageField(upload_to='prodcuts/%Y/%m/%d',blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id, self.slug])

