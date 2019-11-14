"""Docstring"""
from django.urls import path
from . import views

app_name = 'aliments_off'
urlpatterns = [
    path('search/', views.SearchView.as_view(), name='search'),
    path('<int:product_id>/result/', views.ResultView.as_view(), name='result'),
    path('<int:pk>/detail/', views.DetailProductView.as_view(), name='detail'),
    path('save/', views.SaveView, name='save'),
    path('myproducts/', views.MyProductsView.as_view(), name='myproducts'),
]
