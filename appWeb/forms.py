
from django import forms

class Contacta(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Introduce tu nombre"}),label="Nombre")
    apellido=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Introduce tu apellido"}),label="Apellido")
    telefono=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Introduce tu telefono"}),label="Telefono")
    email=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Introduce tu email"}),label="Email")
    mensaje=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Introduce tu mensaje"}),label="Mensaje")
