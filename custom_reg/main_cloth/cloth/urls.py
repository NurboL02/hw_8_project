from django.urls import path
from . import views

app_name = 'cloth'

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('tags/', views.tag_list, name='tag_list'),
    path('products/', views.product_list, name='product_list'),
    path('create_order/', views.create_order, name='create_order'),
]
