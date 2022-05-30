from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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