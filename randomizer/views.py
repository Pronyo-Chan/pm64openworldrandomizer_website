from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import SettingSerializer


class RandomizerViewSet(viewsets.ViewSet):
    def get(self, request):
        return Response({}, status=status.HTTP_200_OK)

    def create(self, request):
        if "seed" not in request.data:
            return Response({
                "seed": "Seed must be included"
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = SettingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        setting = serializer.create()

        data = SettingSerializer(setting).data

        return Response(data, status=status.HTTP_200_OK)
