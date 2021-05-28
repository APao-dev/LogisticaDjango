from django.shortcuts import render, redirect
from .forms import FormContacto

from django.core.mail import  EmailMessage
# Create your views here.

def contacto(request):
    form_contacto = FormContacto()

    if request.method == "POST":
        form_contacto = FormContacto(data= request.POST)
        if form_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            consulta=request.POST.get("consulta")

            email= EmailMessage("Mensaje desde App Django", 
            "El usuario con nombre {} con la dirección {} escribe lo siguiente {} ".format(nombre, email, consulta), "", ["apaofernandez10@gmail.com"], reply_to=[email])

            try:
                email.send() 

                return redirect("/contacto/?valido")

            except:
                return redirect("/contacto/?invalido")



    return render(request,"contacto/contacto.html", {'miFormulario':form_contacto})
