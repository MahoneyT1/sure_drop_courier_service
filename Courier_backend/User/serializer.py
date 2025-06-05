"""
    User serializer class
"""
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from User.models import User


class UserSerializer(ModelSerializer):
    """serializes user objec to python types
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'full_name', 'is_active', 
                    'is_staff', 'phone_number', 'address', 'role']

        extra_kwargs = {
            'password': { "write_only": True }
        }

    def create(self, validated_data):
        """Methods that creates user object with serialer class"""
        validated_data.pop('confirm_password', None)
        email = validated_data.get('email')

        if not email:
            raise serializers.ValidationError("email must be provided")
        
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """Updates existing user with validated data
        """

        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.username = validated_data.get('username', instance.username)

        instance.save()
        return instance


