from django.urls import path
import views

urlpatterns = [
    path('', views.index),
    path('all/', views.all),
    path('chart/', views.chart),
]

