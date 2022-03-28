from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Observe a diferença entre authenticate e login: authenticate() verifica as
# credenciais do usuário e devolve um objeto User se estiverem corretas;
# login() define o usuário na sessão atual

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})

# O decorator login_required verifica se o usuário atual está autenticado.
# Se o usuário estiver autenticado, a view decorada será executada;
# se não estiver autenticado, o usuário será redirecionado para o URL de login,
# com o URL originalmente requisitado como um parâmetro de GET chamado next.
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})