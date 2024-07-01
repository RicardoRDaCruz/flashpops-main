from django.shortcuts import render
from .models import *
#from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def flashpops_um(request):
    musicas = Musica.objects.filter(jogo=1).order_by('posicao')
    lista_musicas = []
    for i in musicas:
        dicionario_musica = {}
        dicionario_musica.update({'filme':i.filme})
        dicionario_musica.update({'posicao':i.posicao})
        dicionario_musica.update({'file':i.file})        
        nomes_alternativos_especificos=NomeAlternativo.objects.filter(musica__id=i.id)
        lista_nomes_alternativos=[]
        for j in nomes_alternativos_especificos:
            lista_nomes_alternativos.append(j.nome)
        dicionario_musica.update({'nomes_alternativos':lista_nomes_alternativos})
        lista_musicas.append(dicionario_musica)
    
    quantidade = musicas.count()
    context = {
        'musicas':lista_musicas,
        'quantidade':quantidade,
    }
    return render(request, 'flashpops_um.html', context)

def flashpops_dois(request):
    musicas = Musica.objects.filter(jogo=2).order_by('posicao')
    lista_musicas = []
    for i in musicas:
        dicionario_musica = {}
        dicionario_musica.update({'filme':i.filme})
        dicionario_musica.update({'posicao':i.posicao})
        dicionario_musica.update({'file':i.file})        
        nomes_alternativos_especificos=NomeAlternativo.objects.filter(musica__id=i.id)
        lista_nomes_alternativos=[]
        for j in nomes_alternativos_especificos:
            lista_nomes_alternativos.append(j.nome)
        dicionario_musica.update({'nomes_alternativos':lista_nomes_alternativos})
        lista_musicas.append(dicionario_musica)
    
    quantidade = musicas.count()
    context = {
        'musicas':lista_musicas,
        'quantidade':quantidade,
    }
    return render(request, 'flashpops_dois.html', context)


def flashpops_tres(request):
    musicas = Musica.objects.filter(jogo=3).order_by('posicao')
    lista_musicas = []
    for i in musicas:
        dicionario_musica = {}
        dicionario_musica.update({'filme':i.filme})
        dicionario_musica.update({'posicao':i.posicao})
        dicionario_musica.update({'file':i.file})        
        nomes_alternativos_especificos=NomeAlternativo.objects.filter(musica__id=i.id)
        lista_nomes_alternativos=[]
        for j in nomes_alternativos_especificos:
            lista_nomes_alternativos.append(j.nome)
        dicionario_musica.update({'nomes_alternativos':lista_nomes_alternativos})
        lista_musicas.append(dicionario_musica)
    
    quantidade = musicas.count()
    context = {
        'musicas':lista_musicas,
        'quantidade':quantidade,
    }
    return render(request, 'flashpops_tres.html', context)

def flashpops_quatro(request):
    musicas = Musica.objects.filter(jogo=4).order_by('posicao')
    lista_musicas = []
    for i in musicas:
        dicionario_musica = {}
        dicionario_musica.update({'filme':i.filme})
        dicionario_musica.update({'posicao':i.posicao})
        dicionario_musica.update({'file':i.file})        
        nomes_alternativos_especificos=NomeAlternativo.objects.filter(musica__id=i.id)
        lista_nomes_alternativos=[]
        for j in nomes_alternativos_especificos:
            lista_nomes_alternativos.append(j.nome)
        dicionario_musica.update({'nomes_alternativos':lista_nomes_alternativos})
        lista_musicas.append(dicionario_musica)
    
    quantidade = musicas.count()
    context = {
        'musicas':lista_musicas,
        'quantidade':quantidade,
    }
    return render(request, 'flashpops_quatro.html', context)

# Create your views here.
