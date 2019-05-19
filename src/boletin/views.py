from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.
def inicio(request):
    titulo = "Bem vindo"
    if request.user.is_authenticated():
        titulo = "Bem vindo"
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
    titulo = "Contato"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        assunto = 'Form  de contato'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "otroemail@gmail.com"]
        email_mensaje = "%s: %s enviado por %s" %(form_nombre,form_mensaje,form_email)

        send_mail(assunto,
                email_mensaje,
                email_from,
                email_to,
                fail_silently = False
                )
    context = {
        "form" : form,
        "titulo": titulo
    }
    return render(request, "forms.html", context)