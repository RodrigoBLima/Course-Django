from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.
def inicio(request):
    titulo = "Hola"
    if request.user.is_authenticated():
        titulo = "Bem vindo %s" %(request.user)
    form = RegModelForm(request.POST or None)

    context = {  
                "titulo": titulo,
                "el_form" : form,
            }

    if form.is_valid(): 
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        if not instance.nombre:
            instance.nombre = "Pessoa"
        instance.save() 

        context = {
            "titulo" : "Obrigado %s!" %(nombre)
        }

        if not nombre:
           context = {
            "titulo" : "Obrigado pessoa sem nome %s!" %(email) 
            } 

        #form_data = form.cleaned_data
        #abc = form_data.get("email")
        #abc2 = form_data.get("nombre")
        #obj = Registrado.objects.create(email=abc, nombre=abc2)


   
    return render(request, "inicio.html", context)
    

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        mensaje = form.cleaned_data.get("mensaje")
        nombre = form.cleaned_data.get("nombre")
        #print email,mensaje, nombre

        context = {
            "form" : form,
        }
    return render(request, "forms.html", context)