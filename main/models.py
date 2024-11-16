from django.db import models

class Animais(models.Model):
    nome = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    sexo = models.CharField(max_length=255)
    idade = models.CharField(max_length=255)
    cor = models.CharField(max_length=255)
    castrado = models.CharField(max_length=255)

    class Meta:
        db_table = 'main_animais'
    

class Despesa(models.Model):
    procedimentos_aquisicoes = models.CharField(max_length=255)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor_medio = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'main_despesas'


class Orcamento(models.Model):
    categoria = models.CharField(max_length=255)
    previsao = models.DecimalField(max_digits=10, decimal_places=2)
    despesas = models.DecimalField(max_digits=10, decimal_places=2)
    porct_utilizado = models.DecimalField(max_digits=5, decimal_places=2)
    anotacoes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'main_orcamento'