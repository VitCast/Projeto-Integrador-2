from django.shortcuts import render
from main.models import Animais, Despesa, Orcamento

def index(request):
    return render(request, 'main/index.html')



def doacao_animais(request):
    animais = Animais.objects.all()
    return render(request, 'main/doacao_animais.html', {"animals": animais})



def despesas(request):
    despesas = Despesa.objects.all()
    return render(request, 'main/despesas.html', {"despesas": despesas})



def orcamento(request):
    orcamentos = Orcamento.objects.all()
    return render(request, 'main/orcamento.html', {"orcamentos": orcamentos})



def conclusao(request):
    return render(request, 'main/conclusao.html')