
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=140,blank=False,null=False)
    model_no = models.CharField(max_length=140,blank=False,null=False)

    brands = [
        ("1", "Samsung"),
        ("2", "Apple"),
        ("3", "Nokia")
    ]

    brand = models.CharField(max_length=9,
                  choices=brands,
                  default="1")
    price = models.IntegerField(default=0)
    rating = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(0)])
    thumbnail = models.ImageField()
    quantity = models.IntegerField(default=0)
    description = models.TextField(max_length=1000,blank=False,null=False)
 
 
    def __str__(self):
        return self.name

class Product_Variant(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # color of mobile
    colors = (
        ("1", "Red"),
        ("2", "Blue"),
        ("3", "Green"),
    )

    color = models.CharField(max_length=9,
                  choices=colors,
                  default="1")

    size = (
        ("1", "4gb 64gb"),
        ("2", "6gb 64gb"),
        ("3", "8gb 128gb"),
    )

    variant = models.CharField(max_length=9,
                  choices=size,
                  default="1")

    quantity  = models.IntegerField(default=0)
    def __str__(self):
        return self.product.name+'_'+self.color+'_'+self.variant




class Cart(models.Model):
    user = models.OneToOneField(
            User,
            primary_key=True,
            on_delete=models.CASCADE,
            related_name="profile"
        )

    def __str__(self):
        return self.user.username

class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(Product_Variant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(Product_Variant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=1000,blank=False,null=False)

    def __str__(self):
        return self.product.name+self.user.username
