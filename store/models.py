from django.db import models

# Create your models here.

class Category_group(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(blank=True, null=True)
    category_group = models.ForeignKey(Category_group,related_name='category_group', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' | ' + str(self.code)

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    quantity = models.FloatField()
    quantity_category = models.CharField(max_length=20)
    date_entered = models.DateTimeField(auto_now_add=True)

class Sale_Products(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity_category = models.CharField(max_length=100)
    date_entered = models.DateTimeField(auto_now_add=True)

class Inventories(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.FloatField()
    quantity_category = models.CharField(max_length=100)
    date_entered = models.DateTimeField(auto_now_add=True)