from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def base(request):
    return render(request, 'core/layouts/base.html')

def galeria(request):
    return render(request, 'core/galeria.html', {})

def procedimiento(request):
    return render(request, 'core/procedimiento.html', {})

def somos(request):
    return render(request, 'core/somos.html', {})

def ubicacion(request):
    return render(request, 'core/ubicacion.html', {})

def portfolio(request):
    return HttpResponse("<h1>Portafolio personal</h1><h3>Mi portafolio</h3><p>Mi listado de trabajos realizados</p>")