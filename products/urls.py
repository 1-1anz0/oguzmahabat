from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    
    path('search/', category, name='search' ),
    path('<slug:category_slug>/', category, name='index' ),
    path('product/<slug:product_slug>/', product_show, name='product' ),

   
]
    # path('<slug:category_slug>/', catalog, name='index'),