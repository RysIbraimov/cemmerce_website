from django.shortcuts import render
from rest_framework import generics, authentication,viewsets
from rest_framework import permissions
from rest_framework.response import Response

from account.models import Profile
from .models import Category,Item,Order
from .serializers import CategorySerializer,ItemSerializer, OrderSerializer
from .permissions import IsSenderOrReadOnly, IsAuthorOrReadOnly,IsBuyerOrReadOnly

class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication, ]
    permission_classes = [IsSenderOrReadOnly,]

class CategoryRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication, ]
    permission_classes = [IsSenderOrReadOnly, ]

class ItemCreateListApiView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication, ]
    permission_classes = [IsSenderOrReadOnly, ]

    def get_queryset(self):
        category = self.kwargs['pk']
        return Item.objects.filter(category=category)

    def perform_create(self, serializer):
        category = Category.objects.filter(pk=self.kwargs['pk']).first()
        serializer.save(category=category,profile=self.request.user.profile)

class ItemRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication, ]
    permission_classes = [IsAuthorOrReadOnly, ]

class OrderCreateApiView(generics.ListCreateAPIView):
    #queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication, ]
    permission_classes = [IsBuyerOrReadOnly]

    def get_queryset(self):
        item = self.kwargs['id']
        return Order.objects.filter(item=item)

    def perform_create(self, serializer):
        item = Item.objects.filter(pk=self.kwargs['id']).first()
        profile = Profile.objects.filter(user=self.request.user).first()
        serializer.save(item=item,profile=profile)


class OrderRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication, ]
    permission_classes = [IsBuyerOrReadOnly, ]

    def get_object(self):
        item = self.kwargs['id']
        value = self.kwargs['order_id']
        order_obj = Order.objects.filter(pk=value,item=item).first()
        return order_obj





