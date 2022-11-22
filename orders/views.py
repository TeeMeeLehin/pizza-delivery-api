from django.shortcuts import render, get_object_or_404
from requests import delete
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from . import serializers
from .models import order, User
from drf_yasg.utils import swagger_auto_schema

class HelloOrders(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(data={'message':'Orders!'}, status = status.HTTP_200_OK )
    

class orderCreateListView(generics.GenericAPIView):
    serializer_class = serializers.orderCreationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = order.objects.all()
    
    @swagger_auto_schema(operation_summary="List All Orders")
    def get(self, request):
        orders = order.objects.all()
        serializer = self.serializer_class(instance=orders, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_summary="Create an Order")
    def post(self, request):
        data=request.data
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save(customer=request.user)
            
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class orderDetailView(generics.GenericAPIView):
    serializer_class = serializers.orderDetailSerializer
    permission_classes=[IsAdminUser]
    
    @swagger_auto_schema(operation_summary="Get Order Details")
    def get(self, request, order_id):
        orderX = get_object_or_404(order, pk=order_id)
        serializer = self.serializer_class(instance=orderX)
        return Response(data=serializer.data, status=status.HTTP_200_OK)     
    
    @swagger_auto_schema(operation_summary="Update Order Details")
    def put(self, request, order_id):
        data = request.data
        orderX = get_object_or_404(order, pk=order_id)
        serializer = self.serializer_class(data=data, instance=orderX)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_summary="Delete an Order")
    def delete(self, request, order_id):
        orderX = get_object_or_404(order, pk=order_id)
        orderX.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class orderUpdateStatusView(generics.GenericAPIView):
    serializer_class=serializers.orderStatusUpdateSerializer
    permission_classes=[IsAdminUser]
    
    @swagger_auto_schema(operation_summary="Update Order Status")
    def put(self, request, order_id):
        orderX=get_object_or_404(order, pk=order_id)
        data = request.data
        serializer=self.serializer_class(data=data, instance=orderX)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserOrderView(generics.GenericAPIView):
    serializer_class = serializers.orderDetailSerializer
    
    @swagger_auto_schema(operation_summary="List User\'s Orders")
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        orderX = order.objects.all().filter(customer=user)
        serializer = self.serializer_class(instance=orderX, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UserOrderDetailView(generics.GenericAPIView):
    serializer_class=serializers.orderDetailSerializer
    
    @swagger_auto_schema(operation_summary="Get User\'s Order Details")
    def get(self,request, user_id, order_id):
        user = User.objects.get(pk=user_id)
        orderX=order.objects.all().filter(customer=user).get(pk=order_id)
        serializer=self.serializer_class(instance=orderX)
        return Response(data=serializer.data, status=status.HTTP_200_OK)