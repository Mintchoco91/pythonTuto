from django.conf.urls import url, include
from . import views
from django.urls import path

app_name = 'python_lotto_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('insert', views.insertData, name="insert"),
    path('ajax', views.ajax, name="ajax"),
    path('analyze', views.analyze, name="analyze"),
    path('home/', views.home, name="home"),
]
