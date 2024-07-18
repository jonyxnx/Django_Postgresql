from django.shortcuts import render, redirect
from .models import Pais

def home(request):
    if request.method == 'POST' and 'pais_id' in request.POST:
        pais_id = request.POST.get('pais_id')
        pais = Pais.objects.filter(id=pais_id).first()
        if pais:
            pais.is_active = False
            pais.save()
        return redirect('home')

    paises = Pais.objects.filter(is_active=True) # Tomamos solo los registros activos
    nombre = request.GET.get('nombre') # Filtramos por nombre del pais
    capital = request.GET.get('capital') # Filtramos por nombre de la capital
    poblacion = request.GET.get('poblacion') # Filtramos por tamaño de poblacion

    # Realizamos el filtrado: 
    if nombre:
        paises = paises.filter(nombre__icontains=nombre)
    if capital:
        paises = paises.filter(capital__icontains=capital)
    if poblacion:
        paises = paises.filter(poblacion__icontains=poblacion)
    
    paises = paises.order_by('nombre')
    
    return render(request, 'home.html', {'paises': paises})
