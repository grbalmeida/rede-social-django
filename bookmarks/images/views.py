from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from common.decorators import ajax_required
from actions.utils import create_action
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

            create_action(request.user, 'bookmarked image', new_item)

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

                create_action(request.user, 'likes', image)
            else:
                # Chamar remove() e passar um objeto que não está no conjunto de
                # objetos relacionados não terá nenhum efeito.
                image.users_like.remove(request.user)
            
            return JsonResponse({'status': 'ok'})
        except:
            pass

        return JsonResponse({'status': 'error'})

@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')

    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um inteiro, exibe a primeira página
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # Se a requisição for AJAX e a página estiver fora,
            # do intervalo, devolve uma página vazia
            return HttpResponse('')
        
        # Se a página estiver fora do intervalo,
        # exibe a última página de resultados
        images = paginator.page(paginator.num_pages)

    if request.is_ajax():
        # Para requisições AJAX, renderizamos o template list_ajax.html. Esse template
        # conterá somente as imagens da página requisitada.
        return render(request, 'images/image/list_ajax.html', {'section': 'images', 'images': images})
    
    # Para requisições padrões, renderizamos o template list.html. Esse template
    # estenderá o template base.html para exibir a página completa e incluirá o
    # template list_ajax.html para incluir a lista de imagens.
    return render(request, 'images/image/list.html', {'section': 'images', 'images': images})