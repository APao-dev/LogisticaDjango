from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.
# Buscar en la carpeta blog el archivo blog.html
def blog(request):
    posts=Post.objects.all()
    return render(request,"blog/blog.html", {"posts": posts})


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id) 
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria': categoria, "posts": posts})   