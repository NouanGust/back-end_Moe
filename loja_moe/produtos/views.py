from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all
    serializer_class = ProdutoSerializer
