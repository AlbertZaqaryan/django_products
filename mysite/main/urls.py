from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('products/<int:id>/', views.products, name='products'),
    path('one_product/<int:id>/', views.products_detail, name='products_detail'),
]