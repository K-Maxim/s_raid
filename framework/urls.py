from django.urls import path

from framework import views

urlpatterns = [
    path('create/', views.AddingData.as_view()),
]