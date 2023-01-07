from django.urls import path
from . import views

# /products
# /products/1/detail
# /products/new

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name="product-new"),
    path('details/', views.details, name="product-details"),
]