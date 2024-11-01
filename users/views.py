from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import LoginSerializer,ChangePasswordSerializer,UserSerializer
from rest_framework import status
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from django.http import Http404

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer= LoginSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        user= authenticate(request,**serializer.data)
        if user is None:
            return Response({'detail': 'Invalid Credentials'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        elif not user.is_active:
            return Response({'detail':'Account is Disabled'}, status=status.HTTP_401_UNAUTHORIZED)
        login(request,user)
        return Response(status=status.HTTP_200_OK)

class ChangePasswordView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer= ChangePasswordSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        user= self.request.user
        if user.check_password(serializer.validated_data.get('current_password')):
            if serializer.validated_data.get('new_password') == serializer.validated_data.get('confirm_new_password'):
                user.set_password(serializer.validated_data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'message':'Password and Confirm Password didnt match'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Incorrect  password.'}, status=status.HTTP_400_BAD_REQUEST)
    

class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        logout(request)    
        return Response(status=status.HTTP_200_OK)
    



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    #permission_classes = (UserViewSetPermissions,)
    queryset = User.objects.all().select_related("profile")

    def list(self, request, *args, **kwargs):
        # dont list all users
        raise Http404
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial",False)
        instance= self.get_object()
        serializer = UserSerializer(
            instance=instance,data=request.data,partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)


    @action(methods=("GET",), detail=False, url_path="me")
    def get_current_user_data(self, request):
        user = request.user
        user_data = self.get_serializer(user).data
        return Response(user_data)
    
