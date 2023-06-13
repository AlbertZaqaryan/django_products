from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_prod')
    name = models.CharField('Product name', max_length=50)
    price = models.PositiveIntegerField('Product price')
    img = models.ImageField('Product image', upload_to='prod_images')
    about = models.TextField('Product about')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']