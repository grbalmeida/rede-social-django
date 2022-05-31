from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .forms import ImageCreateForm
from .models import Image

@login_required
def image_create(request):
    if request.method == 'POST':
        # formulário foi enviado
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # os dados do formulário são válidos
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # atribui o usuário atual ao item
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')

            # redireciona para a view de detalhes do novo item criado
            return redirect(new_item.get_absolute_url())
    else:
        # cria o formulário com os dados fornecidos pelo bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})

def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)

    return render(request, 'images/image/detail.html', {'section': 'images', 'image': image})

# O decorador require_POST devolve um objeto HttpResponseNotAllowed (código de status 405)
# se a requisição HTTP não for feita com POST.
@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')

    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                # Chamar add() passando um objeto que já está presente no conjunto
                # de objetos relacionados não terá nenhum efeito.
                image.users_like.add(request.user)
            else:
                # Chamar remove() e passar um objeto que não está no conjunto de
                # objetos relacionados não terá nenhum efeito.
                image.users_like.remove(request.user)
            
            return JsonResponse({'status': 'ok'})
        except:
            pass

        return JsonResponse({'status': 'error'})