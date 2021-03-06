from xml.etree.ElementInclude import include
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # view de login anterior
    # path('login/', views.user_login, name='login'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # # urls para alteração de senha
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # # urls para reiniciar a senha
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('users/', views.user_list, name='user_list'),
    # Certifique-se de que o padrão users/follow será colocado antes do padrão de URL
    # user_detail. Caso contrário, qualquer requisição para /users/follow/ corresponderá
    # à expressão regular do padrão user_detail, e essa view será executada em seu lugar.
    # Lembre-se de que, para qualquer requisição HTTP, Django verifica o URL requisitado
    # em relação a cada padrão na ordem em que aparecem, e interromperá a busca quando
    # houver a primeira correspondência.
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/<username>/', views.user_detail, name='user_detail'),
]

# A view PasswordChangeView cuidará do formulário de alteração de senha,
# enquanto a view PasswordChangeDoneView exibirá uma mensagem de sucesso
# depois que o usuário tiver alterado sua senha de forma bem-sucedida.