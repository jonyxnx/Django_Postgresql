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

    paises = Pais.objects.filter(is_active=True)
    nombre = request.GET.get('nombre')
    capital = request.GET.get('capital')
    poblacion = request.GET.get('poblacion')
    
    if nombre:
        paises = paises.filter(nombre__icontains=nombre)
    if capital:
        paises = paises.filter(capital__icontains=capital)
    if poblacion:
        paises = paises.filter(poblacion__icontains=poblacion)
    
    paises = paises.order_by('nombre')
    
    return render(request, 'home.html', {'paises': paises})