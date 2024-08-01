
# Register your models here.
from django.contrib import admin
from online_market.models import Comment, Order, Product, Category

admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Category)