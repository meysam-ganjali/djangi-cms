from django.urls import path

from apps.accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('activation/', views.ActiveAcoountView.as_view(), name='activation'),
    path('logout/', views.custom_logout_view, name='logout'),
]
