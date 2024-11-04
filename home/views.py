from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import mseResult, mseMarks
from .serializers import mseResultCreateSerializer, mseResultSerializer, mseMarksCreateSerializer, mseMarksSerializer

# Create your views here.

class MseResultViewSet(viewsets.ModelViewSet):
    queryset = mseResult.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return mseResultCreateSerializer
        return mseResultSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return super().get_serializer(*args, **kwargs)

class MseMarksViewSet(viewsets.ModelViewSet):
    queryset = mseMarks.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return mseMarksCreateSerializer
        return mseMarksSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return super().get_serializer(*args, **kwargs)
