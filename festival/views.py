from django.shortcuts import render
from .models import Palco, Dia, Banda, Concerto

def index_view(request):
    return render(request, 'festival/index.html')

def dias_view(request):
    dias = Dia.objects.all() 
    context = {'dias': dias}
    return render(request, 'festival/dias.html', context)

def palcos_view(request):
    palcos = Palco.objects.all()
    context = {'palcos': palcos}
    return render(request, 'festival/palcos.html', context)

def dia_view(request, dia_id):
    dia = Dia.objects.get(id=dia_id)
    # Filtra os concertos apenas deste dia
    concertos = Concerto.objects.filter(dia=dia)
    context = {'dia': dia, 'concertos': concertos}
    return render(request, 'festival/dia.html', context)

def palco_view(request, palco_id):
    palco = Palco.objects.get(id=palco_id)
    # Filtra os concertos apenas deste palco
    concertos = Concerto.objects.filter(palco=palco)
    context = {'palco': palco, 'concertos': concertos}
    return render(request, 'festival/palco.html', context)

def concerto_view(request, concerto_id):
    # Vai buscar o concerto específico pelo ID
    concerto = Concerto.objects.get(id=concerto_id)
    context = {'concerto': concerto}
    return render(request, 'festival/concerto.html', context)