from django import forms

class FormContacto(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True)

    email=forms.CharField(label="Email", required=True)

    contenido=forms.CharField(label="Consulta", widget=forms.Textarea)