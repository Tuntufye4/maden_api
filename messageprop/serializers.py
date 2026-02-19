# serializers.py
from rest_framework import serializers
from .models import MessageProp

class MessagePropSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageProp
        fields = '__all__'
          