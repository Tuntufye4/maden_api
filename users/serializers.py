from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):   
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User   
        fields = ('username','first_name', 'surname','email','last_name','password','phone_number')

    def create(self, validated_data):
        user = User(    
            username=validated_data['username', ''],   
            first_name=validated_data.get('first_name', ''),
            surname=validated_data.get('surname'),
            email=validated_data.get('email', ''),                                             
            last_name=validated_data.get('last_name', ''),    
            phone_number=validated_data.get('phone_number', ''),              
        )  
        user.set_password(validated_data['password'])                             
        user.save()        
        return user
    
class UserSerializer(serializers.ModelSerializer):        

    class Meta:         
        model = User                 
        fields = ('username','first_name', 'surname','email','last_name','phone_number' )
                               