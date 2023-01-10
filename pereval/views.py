from django.http import HttpResponse
from rest_framework import viewsets, status
import json
from .models import Pereval_added, Users, Coords, Pereval_areas, Pereval_images, Spr_activities_types
from .serializers import PerevalSerializer, UsersSerializer, CoordsSerializer, Pereval_areasSerializer, \
    Pereval_imagesSerializer, Spr_activities_typesSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
#создание представлений




class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class Pereval_areasViewSet(viewsets.ModelViewSet):
    queryset = Pereval_areas.objects.all()
    serializer_class = Pereval_areasSerializer


class Pereval_imagesViewSet(viewsets.ModelViewSet):
    queryset = Pereval_images.objects.all()
    serializer_class = Pereval_imagesSerializer


class Spr_activities_typesViewSet(viewsets.ModelViewSet):
    queryset = Spr_activities_types.objects.all()
    serializer_class = Spr_activities_typesSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer



@csrf_exempt
def submitData(request):
    if request.method == 'POST':
        json_params = json.loads(request.body)
        pereval_added = Pereval_added.objects.create(
            beautyTitle=json_params['beautyTitle'],
            title_added=json_params['title_added'],
            other_titles=json_params['other_titles'],
            connect=json_params['connect'],
            coord_id=Coords.objects.create(
                latitude=json_params['latitude'],
                longitude=json_params['longitude'],
                height=json_params['height']
            ),
            author=Users.objects.create(
                fam=json_params['fam'],
                name=json_params['name'],
                otc=json_params['otc'],
                emails=json_params['emails'],
                phone=json_params['phone']
            )
        )
        return HttpResponse(json.dumps({
            "beautyTitle": pereval_added.beautyTitle,
            "title_added": pereval_added.title_added,
            "other_titles": pereval_added.other_titles,
            "connect": pereval_added.connect,
            "author": pereval_added.author,
            "coord_id": pereval_added.coord_id
        }))


@csrf_exempt
def submitDataGetPatch(request, Pereval_added_id):
    pereval_added = Pereval_added.objects.get(pk=Pereval_added_id)
    if request.method == 'GET':
        return HttpResponse(json.dumps(
            {
                "id": pereval_added.id,
                "beautyTitle": pereval_added.beautyTitle,
                "title_added": pereval_added.title_added,
                "other_titles": pereval_added.other_titles,
                "connect": pereval_added.connect,
                "status": pereval_added.status
            }
        ))
    json_params = json.loads(request.body)
    if request.method == 'PATCH':
        pereval_added.beautyTitle = json_params.get('beautyTitle', pereval_added.beautyTitle)
        pereval_added.title_added = json_params.get('title_added', pereval_added.title_added)
        pereval_added.other_titles = json_params.get('other_titles', pereval_added.other_titles)
        pereval_added.connect = json_params.get('connect', pereval_added.connect)
        pereval_added.save()
        return HttpResponse(json.dumps({
            "id": pereval_added.id,
            "beautyTitle": pereval_added.beautyTitle,
            "title_added": pereval_added.title_added,
            "other_titles": pereval_added.other_titles,
            "connect": pereval_added.connect
        }))
