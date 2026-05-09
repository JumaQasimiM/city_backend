from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'bio',
            'password',
            'avatar',
            'role',
        ]

        read_only_fields = ['id']

        extra_kwargs = {
            'password': {'write_only': True},
            'avatar': {'required': False},
        }

    # username validation
    def validate_username(self, username):

        if 'admin' in username.lower():
            raise serializers.ValidationError(
                'Username is not allowed!'
            )

        if len(username) < 3:
            raise serializers.ValidationError(
                'Username must be at least 3 characters'
            )

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'Username already exists!'
            )

        return username

    # email validation
    def validate_email(self, value):

        qs = User.objects.filter(email=value)

        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError(
                'Email already exists!'
            )

        return value

    # password validation
    def validate_password(self, password):

        if len(password) < 6:
            raise serializers.ValidationError(
                'Password must be at least 6 characters'
            )

        first_name = self.initial_data.get('first_name', '')
        last_name = self.initial_data.get('last_name', '')
        email = self.initial_data.get('email', '')

        if first_name and first_name.lower() in password.lower():
            raise serializers.ValidationError(
                'Password must not contain first name'
            )

        if last_name and last_name.lower() in password.lower():
            raise serializers.ValidationError(
                'Password must not contain last name'
            )

        if email and email.lower() in password.lower():
            raise serializers.ValidationError(
                'Password must not contain email'
            )

        return password

    # create user
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    # update user
    def update(self, instance, validated_data):

        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()

        return instance