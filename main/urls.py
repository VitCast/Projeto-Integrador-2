from django.urls import path
from main.views import index, doacao_animais, despesas, orcamento, conclusao

urlpatterns = [
    path('', index, name='index'),
    path('doacao_animais/', doacao_animais, name='doacao_animais'),
    path('despesas/', despesas, name='despesas'),
    path('orcamento/', orcamento, name='orcamento'),
    path('coclusao/', conclusao, name='conclusao'),
]