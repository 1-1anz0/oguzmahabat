from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


    

class Category(MPTTModel):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    parent = TreeForeignKey('self', related_name='child', on_delete=models.PROTECT, null=True, blank=True)
    

    class MPTTMETA:
        order_insertion_by = ['title']


    def __str__(self):
        return self.title
    

class Products(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    img = models.ImageField(upload_to='media', null=True)
    description = models.TextField()
    category = models.ForeignKey(to=Category, related_name='products', on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField(default=0, verbose_name='Price')

    class Meta:
        verbose_name = 'Önüm'
        verbose_name_plural = 'Önümler'

    def __str__(self) -> str:
        return self.title
    