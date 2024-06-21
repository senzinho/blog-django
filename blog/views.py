from django.shortcuts import render
from blog.models import Noticias

def noticia_view(request):
    noticias = Noticias.objects.all().order_by('-pub_date')
    search = request.GET.get('search')

    if search:
        noticias = Noticias.objects.filter(title__icontains=search)

    return render(
        request,
        'noticias.html',
        {'noticias': noticias},
                 )

def noticia(request):
    if request.method == 'GET':
        id = request.GET.get('id')  # 'id' é o nome do campo que você está tentando recuperar
        print(id)

        # Faça algo com o ID, se necessário

    return render(
        request,
        'noticias_geradas.html',
        {'id': id},  # Passa o valor de 'id' para o contexto do template
    )
