from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # view de login anterior
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # urls para alteração de senha
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]

# A view PasswordChangeView cuidará do formulário de alteração de senha,
# enquanto a view PasswordChangeDoneView exibirá uma mensagem de sucesso
# depois que o usuário tiver alterado sua senha de forma bem-sucedida.