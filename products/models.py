from django.db import models

class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=5000)
    amazon_id = models.CharField(max_length=50)
    current_price = models.CharField(max_length=20)
    amazon_affiliate_link = models.CharField(max_length=200)
    primary_photo_link = models.CharField(max_length=500)
    department = models.ForeignKey(Department, default=None, null=True, blank=True, on_delete=models.SET_NULL)
    is_best_seller = models.BooleanField(default=False)
    is_hot_deal = models.BooleanField(default=False)

    def __str__(self):
        return self.name
