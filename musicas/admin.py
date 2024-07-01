from django.contrib import admin
from .models import *

# Register your models here.
class NomeAlternativoAdmin(admin.TabularInline):
    model = NomeAlternativo

@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    list_display=('id','filme','posicao','jogo',)
    inlines=[NomeAlternativoAdmin,]
