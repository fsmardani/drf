from django.contrib.auth import login
from django.contrib.auth.models import update_last_login
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import generics

from .models import Account
from .serializers import RegisterSerializer,LoginSerializer,AccountSerializer


class Plot(APIView):
    permission_classes = (IsAuthenticated,)
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


class SetPermission(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'set_permission.html'

    def get(self, request, pk):
        profile = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})


        # queryset = Account.objects.all()
        # serializer_class = AccountSerializer
        # permission_classes = (IsAdminUser,)
        #
        # def update(self, request,pk, *args, **kwargs):
        #     instance = self.get_object()
        #     instance.has_permission_to = request.data.get("has_permission_to")
        #     instance.save()
        #
        #     serializer = self.get_serializer(instance)
        #     serializer.is_valid(raise_exception=True)
        #     self.perform_update(serializer)
        #
        #     return Response(serializer.data)
    # queryset = Account.objects.all()
    # permission_classes = (IsAdminUser,)
    # serializer_class = AccountSerializer
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'set_permission.html'
    # def get_object(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     # make sure to catch 404's below
    #     obj = queryset.get(pk=self.request.data['user'])
    #     self.check_object_permissions(self.request, obj)
    #     return obj
    # def get(self, request):
    #     users = Account.objects.all()
    #     print(users)
    #     return Response({'users':users})

    # def update(self, request, *args, **kwargs):
    #     print(request.data)
    #     serializer = AccountSerializer(data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     # user = serializer.validated_data['user']
    #     return redirect('main')

    # def post(self, request, *args, **kwargs):
    #     print(request.data)
    #     username = request.data.get('user')
    #     has_permission_to = request.data.get('perm')
    #     serializer = AccountSerializer(data={'username':username,'has_permission_to':has_permission_to})
    #     serializer.is_valid(raise_exception=True)
    #
    #     serializer.save()
    #     # token, created = Token.objects.get_or_create(user=user)
    #     return redirect('main')
    #


class AccountsList(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer