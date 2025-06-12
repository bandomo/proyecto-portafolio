from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def portfolio(request):
    return HttpResponse("<h1>Portafolio personal</h1><h3>Mi portafolio</h3><p>Mi listado de trabajos realizados</p>")