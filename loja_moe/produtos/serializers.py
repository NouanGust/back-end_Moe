from rest_framework import serializers
from .models import Produto, ProdutoImagem


class ProdutoImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoImagem
        fields = ["imagem", "tipo"]
        
class ProdutoSerializer(serializers.ModelSerializer):
    imagens = ProdutoImagemSerializer(many=True, ready_only=True)
    class Meta:
        model = Produto
        fields = "__all__"
