from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('product/', views.product_list),
    path('product/<int:pk>/',views.product_detail)
]
