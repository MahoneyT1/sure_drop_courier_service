"""
    User serializer class
"""
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from User.models import User


class UserSerializer(ModelSerializer):
    """serializes user object to python types
    """
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'confirm_password', 'full_name', 'is_active', 
                    'is_staff', 'phone_number', 'address', 'role']

        extra_kwargs = {
            'email': {'required': True }, 
            'password': { "write_only": True, 'min_length': 6, 'required': True },
            'full_name': {'required': True },
            'confirm_password': {'required': True },
        }

    def validate_email(self, value):
        """validates email field
        """
        if value is None:
            raise serializers.ValidationError("email must be provided")

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("email already exists")
        return value

    def validate(self, data):
        """validates password and confirm password
        """
        password = data['password']
        confirm_password = data.pop('confirm_password', None)

        if password != confirm_password:
            raise serializers.ValidationError("passwords do not match")

        return data

    def create(self, validated_data):
        """Methods that creates user object with serialer class"""
        
        email = validated_data.get('email')
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        """Updates existing user with validated data
        """

        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.username = validated_data.get('username', instance.username)

        instance.save()
        return instance
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """ Overiding the default token serializer to 
    validate with email as the username
    """

    username_field = 'email'

    def validate(self, attrs):
        """validates the token with email and password
        """
        credentials = {
            'email': attrs.get('email'),
            'password': attrs.get('password')
        }

        user = User.objects.filter(email=credentials['email']).first()

        if user is None:
            raise serializers.ValidationError('No user with this email exists')
        
        else:
            if not user.check_password(credentials['password']):
                raise serializers.ValidationError('Incorrect password')

        if credentials['email'] and credentials['password']:
            from django.contrib.auth import authenticate

            user = authenticate(**credentials)
            if not user:
                raise serializers.ValidationError('Invalid email or password.')

            refresh = self.get_token(user)
            access = refresh.access_token

            # Add tokens to response data
            data = {
                'refresh': str(refresh),
                'access': str(access),
                'user': {
                    'id': str(user.id),
                    'email': user.email,
                    'username': user.username,
                }
            }

        return data 


