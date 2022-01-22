from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import SettingSerializer


class RandomizerViewSet(viewsets.ViewSet):
    def get(self, request):
        return Response({}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = SettingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        setting = serializer.create()

        data = SettingSerializer(setting).data

        return Response(data, status=status.HTTP_200_OK)
