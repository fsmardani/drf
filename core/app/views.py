from django.contrib.auth import login
from django.contrib.auth.models import update_last_login
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import generics

from .models import Account
from .serializers import RegisterSerializer,LoginSerializer


class Plot(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main.html'

    def get(self, request):
        # serializer = LoginSerializer()
        return Response()


class LoginView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        serializer = LoginSerializer()
        return Response({'serializer': serializer})

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user)
        # token, created = Token.objects.get_or_create(user=user)
        return redirect('main')


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class SetPermission(APIView):
    permission_classes = (IsAdminUser,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'set_permission.html'

    def get(self, request):
        users = Account.objects.all()
        print(users)
        return Response({'users':users})

