from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image_url and request:
            return request.build_absolute_uri(obj.image_url.url)
        return None
          