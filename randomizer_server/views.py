from ast import operator
from rest_framework.decorators import api_view
from pathlib import Path
import sys
import json

from randomizer_server.services.cloud_storage_service import get_file_from_cloud, save_file_to_cloud
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


@api_view(['GET'])
def get_randomizer_settings(request, pk):

    if pk is None:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        try:
            setting = Setting.objects.get(pk=pk)
        except Setting.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    serializer = SettingSerializer(setting)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_randomizer_settings(request):

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


@api_view(['GET'])
def get_spoiler_log(request, pk):
    if pk is None:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        try:
            setting = Setting.objects.get(pk=pk)
        except Setting.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    spoiler_file = get_file_from_cloud(f'spoiler/{pk}.txt')
    if spoiler_file is None:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    response = FileResponse(spoiler_file)
    return HttpResponse(response, content_type='application/octet-stream', status=status.HTTP_200_OK)

@api_view(['GET'])
def get_patch(request, pk):
    if pk is None:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        try:
            setting = Setting.objects.get(pk=pk)
        except Setting.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    patch_file = get_file_from_cloud(f"patch/{pk}.pmp")
    if patch_file is None:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    response = FileResponse(patch_file)
    return HttpResponse(response, content_type='application/octet-stream', status=status.HTTP_200_OK)
        
