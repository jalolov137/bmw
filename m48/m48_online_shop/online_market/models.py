
from django.db import models

from online_market.forms import OrderForm


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Product(BaseModel):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="products")
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)
    rating = models.PositiveIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value)
    discount = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products", null=True, blank=True)

@property
def image_url(self):
    if self.image:
        return self.image.url
    return None


@property
def discounted_price(self):
    if self.discount > 0:
        return self.price * (1 - self.discount / 100)
    return self.price


def __str__(self):
    return self.name


class Comment(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    is_provide = models.BooleanField(default=False)



    def __str__(self):
        return f'{self.name} - {self.created_at}'


class Order(models.Model):
  product = models.CharField(max_length=100)
  quantity = models.IntegerField()
  customer = models.CharField(max_length=100)
  status = models.CharField(max_length=100)


  def __str__(self):
      return f'{self.product}, ordered by {self.customer}'