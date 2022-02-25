from django.urls import path

import views

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path('', views.index),
    path('all/', views.all),
    path('chart/', views.chart),
]

