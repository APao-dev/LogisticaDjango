from django.shortcuts import render
from blog.models import Post

# Create your views here.
# Buscar en la carpeta blog el archivo blog.html
def blog(request):
    posts=Post.objects.all()
    return render(request,"blog/blog.html", {"posts": posts})