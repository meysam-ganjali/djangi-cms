from django.urls import include, path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index')
]
