from django.contrib.auth import authenticate
from rest_framework import serializers
from api.models import User
from api.models import Task



class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ['id', 'email', 'date_joined', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128,
                                     min_length=8,
                                     write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in'
            )

        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'User not found'

            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )
        return {
            'token': user.token
        }

class TaskSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    accomplished = serializers.ReadOnlyField()
    class Meta:
        model = Task
        fields = ['id','title','deadline','accomplished']