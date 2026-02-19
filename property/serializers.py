# property/serializers.py
from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    # Write-only image field for uploads
    image = serializers.ImageField(write_only=True, required=False)
    # Read-only absolute URL for frontend
    image_url = serializers.SerializerMethodField(read_only=True)
      
    class Meta:
        model = Property     
        fields = "__all__"

    def get_image_url(self, obj):
        if obj.image_url:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image_url.url)
            return obj.image_url.url
        return None
   
    def create(self, validated_data):
        image = validated_data.pop("image", None)
        if image:
            validated_data["image_url"] = image
        return super().create(validated_data)

    def update(self, instance, validated_data):
        image = validated_data.pop("image", None)
        if image:
            validated_data["image_url"] = image
        return super().update(instance, validated_data)
         