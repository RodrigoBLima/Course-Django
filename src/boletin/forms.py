from django import forms

#model form
from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre","email"]

# validaciones
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveeder = email.split("@")
        dominio, extension = proveeder.split(".")

        if not extension == "edu":
            raise forms.ValidationError("Por favor, digite um e-mail com extensão .edu")
        return email
#nombre
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        return nombre

# inputs 

class RegForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField() 