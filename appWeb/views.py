
from django.shortcuts import redirect, render
from appWeb.forms import Contacta
from django.core.validators import validate_email

from appWeb.models import Consulta
# Create your views here.

def home(request):
    return render(request,'index.html')



def pienso(request):
    return render(request,'piensos.html')


def planesSalud(request,animal):
    titulo=''
    if animal == 'perro':
        titulo = 'Seguros para perros'
    elif animal == 'gato':
        titulo = 'Seguros para gatos'
    else:
        return redirect(home)
    return render(request,'planesSalud.html', locals())

def blog(request):
    return render(request, 'blog.html')

def formulario(request):
    request.session['mensaje']=""
    if request.method=="POST":
        miFormulario=Contacta(request.POST)
        if miFormulario.is_valid():
            dicc=miFormulario.cleaned_data
            val=enviarPeticion(dicc)
            if(val==-1):
                mensaje=request.session['mensaje'] = "El telefono introducido no es válido"
                return render(request,'formulario.html',{'form':miFormulario,"mensaje":mensaje})
            elif val==-2:
                mensaje=request.session['mensaje'] = "El correo introducido no es válido"
                return render(request,'formulario.html',{'form':miFormulario,"mensaje":mensaje})
            elif val==-3:
                mensaje=request.session['mensaje'] = "El nombre o apellido introducido no es válido"
                return render(request,'formulario.html',{'form':miFormulario,"mensaje":mensaje})
            else:
                mensaje=request.session['mensaje'] = "Peticiçon guardada"
                nom=dicc["nombre"]+" "+dicc["apellido"]
                consulta=Consulta(nombre=nom,telefono=dicc["telefono"],email=dicc["email"],mensaje=dicc["mensaje"])
                consulta.save()
                return redirect(formulario)
    else:
        micontacta=Contacta()
        return render(request,'formulario.html', {'form':micontacta})


def enviarPeticion(dicc):
    telf=dicc['telefono']
    val=validarTelf(telf)
    if(val==-1):
        return -1
    else:
        email=dicc["email"]
        val=validarEmail(email)
        if(val==-2):
            return -2
        else:
            val=validarnombre(dicc["nombre"],dicc["apellido"])
            if(val==-3):
                return -3
            return 1

def validarTelf(telf):
    if(len(telf)!=9):
            return -1
    try:
        int(telf)
    except ValueError:
        return -1


def validarEmail(email):
    try:
        validate_email(email)
        return 1
    except:
        return -2

def validarnombre(nombre, apell):
    n=list(nombre)
    for x in n:
        if(not x.isalpha()):
            return -3
    a=list(apell)
    for x in a:
        if(not x.isalpha()):
            return -3
    return 1