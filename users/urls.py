from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'semesters', views.SemesterViewSet, basename='semester')
router.register(r'courses', views.CourseViewSet, basename='course')
router.register(r'personal-profiles', views.PersonalProfileViewSet, basename='personal-profile')
router.register(r'admission-profiles', views.AdmissionProfileViewSet, basename='admission-profile')
router.register(r'contact-information-profiles', views.ContactInformationProfileViewSet, basename='contact-information-profile')
router.register(r'education-qualification-profiles', views.EducationQualificationProfileViewSet, basename='education-qualification-profile')
router.register(r'parent-profiles', views.ParentProfileViewSet, basename='parent-profile')

urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
    # Add URL for SubjectAPI
    path('subjects/', views.SubjectAPI.as_view(), name='subject-api'),
    # Existing paths for login, change-password, and logout
    path('login/', views.LoginView.as_view(), name='login'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
urlpatterns += router.urls