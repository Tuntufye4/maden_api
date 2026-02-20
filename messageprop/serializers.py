from rest_framework import serializers
from .models import MessageProp

class MessagePropSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageProp
        fields = ["id", "user", "property", "text_message", "created_at"]
        read_only_fields = ["id", "user", "created_at"]         