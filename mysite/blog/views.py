from django.shortcuts import render, get_object_or_404  # importamos este get_object_or_404 para erores 404
# agramos el metodo Post del archivo models
# significa que podemos utilizar . y el nombre del archivo (sin .py)
from .models import Post

# importamos esta libreria de fechas de django
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # publicamos los posto por fechas
    return render(request, 'blog/post_list.html', {'posts': posts}) # 'nombre de la varialve posts'


# aca creamos nuestra vista para los detalles del post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)   #aca por si la variable pk no existe
    return render(request, 'blog/post_detail.html', {'post': post})