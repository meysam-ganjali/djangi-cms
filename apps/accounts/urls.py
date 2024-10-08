from django.urls import path

from apps.accounts import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
]