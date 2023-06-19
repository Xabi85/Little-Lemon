from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index, name='Index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()), 
]

