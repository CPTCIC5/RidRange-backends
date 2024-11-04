from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MseResultViewSet, MseMarksViewSet

router = DefaultRouter()
router.register(r'mse-results', MseResultViewSet, basename='mse-result')
router.register(r'mse-marks', MseMarksViewSet, basename='mse-mark')

urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns += router.urls