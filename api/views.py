from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer
from django.core.cache import cache

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        cached_categories = cache.get('categories')
        if cached_categories:
            return Response(cached_categories)

        response = super().list(request, *args, **kwargs)
        cache.set('categories', response.data, timeout=3600)
        return response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        cached_products = cache.get('products')
        if cached_products:
            return Response(cached_products)

        response = super().list(request, *args, **kwargs)
        cache.set('products', response.data, timeout=3600)
        return response

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
