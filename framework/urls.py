from django.urls import path, re_path

from framework import views

urlpatterns = [
    path('create/', views.AddingData.as_view()),
    path('frameworks/', views.DataListView.as_view()),
    re_path('^frameworks/(?P<language>.+)/$', views.DataView.as_view()),
]