from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Loja, Funcionario, Cliente, Banco, Promotora, Prazo, Produto, Orgao, Contrato
# Register your models here.


admin.site.site_header = 'Melhor Idade'

class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome_loja', 'author', 'created_date')
    list_filter = ('nome_loja', 'author', 'created_date')

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('cpf','nome_funcionario','telefone', 'author', 'created_date')
    list_filter = ('nome_funcionario', 'author', 'created_date')
    
    search_fields = ['cpf','nome_funcionario']

admin.site.register(Loja, LojaAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Cliente)
admin.site.register(Banco)
admin.site.register(Promotora)
admin.site.register(Prazo)
admin.site.register(Produto)
admin.site.register(Orgao)
admin.site.register(Contrato)
