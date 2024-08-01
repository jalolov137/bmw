
from django.contrib import admin

from online_market import views
f
from django.urls import path



urlpatterns = [
    path('product-list/', views.product_list, name='product_list'),
    path('categories/<int:category_id>/', views.product_list, name='category/detail.id'),
    path('product-detail//<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_order/', views.add_order, name='add_order'),
    path('order_success/', views.order_success, name='order_success'),
]
