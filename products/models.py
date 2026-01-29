from django.db import models

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

class Tag(models.Model):
    tag_name = models.CharField(max_length=1000)
    tag_value = models.CharField(max_length=1000)

    def __str__(self):
        return self.tag_name


# Create your models here.
class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=5000)
    amazon_id = models.CharField(max_length=50)
    current_price = models.CharField(max_length=20)
    amazon_affiliate_link = models.CharField(max_length=200)
    primary_photo_link = models.CharField(max_length=500)
    discount_percentage = models.IntegerField(default=0)
    department = models.ForeignKey(Department, default=None, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(
        Tag,
        related_name="products",
        blank=True
    )

    def __str__(self):
        return self.name
