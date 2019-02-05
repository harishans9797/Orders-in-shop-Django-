from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Order, Product
from .serializer import ProductSerializer, ProductSerializerUpdate, CustomerSerializer, CustomerSerializerUpdate, OrderSerializer, OrderSerializerUpdate, UserSerializer
from rest_framework import generics
from rest_framework.generics import (DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView)
from django.contrib.auth import authenticate



class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def filter_queryset(self, queryset):
        queryset = super(CustomerList, self).filter_queryset(queryset)
        return queryset




class CustomerListUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializerUpdate



class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def filter_queryset(self, queryset):
        queryset = super(ProductList, self).filter_queryset(queryset)
        return queryset


class ProductListUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerUpdate







class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def filter_queryset(self, queryset):
        queryset = super(OrderList, self).filter_queryset(queryset)
        return queryset


class OrderListUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerUpdate


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer




class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)