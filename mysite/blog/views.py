from django.shortcuts import render, get_object_or_404, redirect  # importamos este get_object_or_404 para erores 404
# agramos el metodo Post del archivo models
# significa que podemos utilizar . y el nombre del archivo (sin .py)
from .models import Post

# importamos esta libreria de fechas de django
from django.utils import timezone
# importamos para el post de
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # publicamos los posto por fechas
    return render(request, 'blog/post_list.html', {'posts': posts}) # 'nombre de la varialve posts'


# aca creamos nuestra vista para los detalles del post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)   #aca por si la variable pk no existe
    return render(request, 'blog/post_detail.html', {'post': post})


# la clase para mandar el nuevo post
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# clase para editar los posts
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})