from rest_framework import serializers
from .models import ViewingRequest

class ViewingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewingRequest
        fields = '__all__'
        read_only_fields = ['user', 'viewingrequest_id', 'created_at', 'updated_at']
               

                     