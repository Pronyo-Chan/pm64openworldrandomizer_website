from ast import operator
import io
import os
from pathlib import Path
import sys
import json

from randomizer_server.services.cloud_storage_service import save_file_to_cloud
from randomizer_server.services.database_service import insert_seed_with_unique_ID
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

        settings = serializer.create()

        data = SettingSerializer(settings).data
        seedID = insert_seed_with_unique_ID(settings)

        rando_settings = json.dumps(data)
        rando_result = web_randomizer(seedID, rando_settings)
        
        response = FileResponse(rando_result.patchBytes)

        save_file_to_cloud(str(f'patch/{settings.SeedID}.pmp'), rando_result.patchBytes)
        save_file_to_cloud(str(f'spoiler/{settings.SeedID}.txt'), rando_result.spoilerLogBytes)

        return HttpResponse(response, content_type='application/octet-stream', status=status.HTTP_200_OK)
