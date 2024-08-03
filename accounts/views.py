from rest_framework import generics, status
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, MyTokenObtainPairSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
from rest_framework.permissions import AllowAny

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "detail": "User created successfully.",
            "user": UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/password_reset.html')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return render(request, 'accounts/password_reset_done.html', {
            'message': 'OTP has been sent to your email.'
        })

class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/password_reset_confirm.html')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return render(request, 'accounts/password_reset_complete.html', {
            'message': 'Password has been reset successfully.'
        })