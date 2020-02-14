from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('manufacturer/<slug:manufacturer_slug>/', views.product_list_manufacturer,
         name='product_list_by_manufacturer'),
    path('collection/<slug:collection_slug>/', views.product_list_collection,
         name='product_list_by_collection'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]