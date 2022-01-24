from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Setting

from .serializers import SettingSerializer


class RandomizerViewSet(viewsets.ViewSet):
    def get(self, request, pk=None):
        if pk is None:
            try:
                setting = Setting.objects.get(IsDefault=True)
            except Setting.DoesNotExist:
                return Response({}, status=status.HTTP_404_NOT_FOUND)
            except Setting.MultipleObjectsReturned:
                return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                setting = Setting.objects.get(pk=pk)
            except Setting.DoesNotExist:
                return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = SettingSerializer(setting)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = SettingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        setting = serializer.create()

        data = SettingSerializer(setting).data

        return Response(data, status=status.HTTP_200_OK)
