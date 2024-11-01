from django.urls import path 
from . import views
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path("change-password/",views.ChangePasswordView.as_view()
         ,name='change-password'),
    path('logout/', views.LogoutView.as_view(), name='logout')

]