from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user found with this email address.")
        return value

    def save(self):
        email = self.validated_data['email']
        users = User.objects.filter(email=email)

        if not users.exists():
            raise serializers.ValidationError("No user found with this email address.")

        for user in users:
            profile = user.profile
            otp = get_random_string(length=6, allowed_chars='0123456789')
            profile.reset_otp = otp
            profile.save()

            send_mail(
                'Password Reset OTP',
                f'Your OTP for password reset is: {otp}',
                'from@example.com',  # Replace with your sender email
                [email],
                fail_silently=False,
            )

class PasswordResetConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        otp = attrs.get('otp')
        if not User.objects.filter(email=email, profile__reset_otp=otp).exists():
            raise serializers.ValidationError("Invalid OTP or email address.")
        return attrs

    def save(self):
        email = self.validated_data['email']
        new_password = self.validated_data['new_password']
        users = User.objects.filter(email=email)

        if not users.exists():
            raise serializers.ValidationError("No user found with this email address.")

        for user in users:
            if user.profile.reset_otp == self.validated_data['otp']:
                user.set_password(new_password)
                user.profile.reset_otp = ''
                user.profile.save()
                user.save()
                break
        else:
            raise serializers.ValidationError("Invalid OTP.")
