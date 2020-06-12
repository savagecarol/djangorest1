from . import views
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.PersonView.as_view()),
    path('add/', views.Weather.as_view()),
]
