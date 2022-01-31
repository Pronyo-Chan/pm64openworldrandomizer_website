from ast import operator
import io
import os
from pathlib import Path
import sys
import json
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'PM64OpenWorldRandomizer' / 'tools')) #local
sys.path.insert(0, str(Path(__file__).parent.parent / 'PM64OpenWorldRandomizer' / 'tools')) # PROD
from randomizer import web_randomizer

from django.shortcuts import render
from django.http import FileResponse, HttpResponse

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

        rando_settings = json.dumps(data)
        operations = web_randomizer(rando_settings)
        
        inmemoryfile = io.BytesIO(operations)
        response = FileResponse(inmemoryfile)
        return HttpResponse(response, content_type='application/octet-stream', status=status.HTTP_200_OK)
