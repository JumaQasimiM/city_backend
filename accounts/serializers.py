from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, username):
        if len(username) < 3:
            raise serializers.ValidationError(
                'Username must be at least 3 characters'
            )
        return username

    def validate_password(self, password):
        if len(password) < 6:
            raise serializers.ValidationError(
                'Password must be at least 6 characters'
            )

# initial_data ---> send data from user or data befor validation
        first_name = self.initial_data.get('first_name')
        last_name = self.initial_data.get('last_name')
        email = self.initial_data.get('email')

# validated_data ---> clear data and ready to save in database

        if first_name and first_name in password:
            raise serializers.ValidationError(
                'Password must not contain first name'
            )

        if last_name and last_name in password:
            raise serializers.ValidationError(
                'Password must not contain last name'
            )

        if email and email in password:
            raise serializers.ValidationError(
                'Password must not contain email'
            )

        return password

# data = validated data
    def validate(self, data):
        email = data.get('email')

        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists!')
        return data
    
    # to hash password
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)