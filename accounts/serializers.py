from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name',
            'username', 'email', 'bio',
            'password', 'avatar', 'role'
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True},
            'avatar': {'required': False}
        }

    # 🔹 username validation
    def validate_username(self, username):
        if 'admin' in username:
            raise serializers.ValidationError('username is not allowed!')

        if len(username) < 3:
            raise serializers.ValidationError(
                'Username must be at least 3 characters'
            )
        return username

    # 🔹 email validation
    def validate_email(self, value):
        qs = User.objects.filter(email=value)

        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError('Email already exists!')

        return value

    # 🔹 password validation
    def validate_password(self, password):
        if len(password) < 6:
            raise serializers.ValidationError(
                'Password must be at least 6 characters'
            )

        first_name = self.initial_data.get('first_name')
        last_name = self.initial_data.get('last_name')
        email = self.initial_data.get('email')

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

    # 🔐 hash password
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    # update pass
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance