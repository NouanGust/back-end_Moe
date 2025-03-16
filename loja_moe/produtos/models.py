from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    colecao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    estoque = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.nome


class ProdutoImagem(models.Model):
    TIPOS_IMAGEM = [
        ("maior", "Imagem Maior"),
        ("menor", "Imagem Menor"),
        ("png", "Imagem PNG"),
        ("cor", "Variação de Cor"),
    ]
    
    produto = models.ForeignKey(Produto, related_name="imagens", on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="produtos/estampas/")
    tipo = models.CharField(max_length=10, choices=TIPOS_IMAGEM)
    
    def __str__(self):
        return f"{self.produto.nome} - {self.get_tipo_display()}"