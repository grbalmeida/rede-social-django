from django.urls import path
from . import views

urlpatterns = [
    # view de login
    path('login/', views.user_login, name='login'),
]