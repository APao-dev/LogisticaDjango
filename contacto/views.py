from django.shortcuts import render, redirect
from .forms import FormContacto
# Create your views here.

def contacto(request):
    form_contacto = FormContacto()

    if request.method == "POST":
        form_contacto = FormContacto(data= request.POST)
        if form_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            consulta=request.POST.get("consulta")

            return redirect("/contacto/?valido")



    return render(request,"contacto/contacto.html", {'miFormulario':form_contacto})
