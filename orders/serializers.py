from email.policy import default
from rest_framework import serializers
from .models import order

class orderCreationSerializer(serializers.ModelSerializer):

    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()
    
    class Meta:
        model = order
        fields = ['id', 'size', 'order_status', 'quantity']

class orderDetailSerializer(serializers.ModelSerializer):

    size = serializers.CharField(max_length=20)
    order_status = serializers.CharField(default='PENDING')
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    
    class Meta:
        model = order
        fields = ['id','size', 'order_status', 'quantity', 'created_at', 'updated_at']

class orderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(default='PENDING')
    
    class Meta:
        model = order
        fields= ['order_status']