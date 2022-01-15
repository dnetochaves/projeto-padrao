from django.shortcuts import render
from .models import Confirguracoes

def index(request):
    configuracoes = Confirguracoes.listar_configuracoes()
    logo = Confirguracoes.objects.get(pk=1)
    return render(request, 'core/index.html', {'configuracoes': configuracoes, 'logo': logo})
