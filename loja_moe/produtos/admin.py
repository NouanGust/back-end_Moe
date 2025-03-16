from django.contrib import admin
from .models import Produto, ProdutoImagem

class ProdutoImagemInline(admin.TabularInline):
    model = ProdutoImagem
    extra = 1
    
    
@admin.register(Produto)
class ProdutoAdmin(admin.model):
    list_display = ("nome", "colecao", "preco", "estoque")
    search_fields = ("nome", "colecao")
    list_filter = ("colecao")
    inlines = [ProdutoImagemInline]
    
@admin.register(ProdutoImagem)
class ProdutoImagemAdmin(admin.ModelAdmin):
    list_display = ("produto", "tipo", "imagem")