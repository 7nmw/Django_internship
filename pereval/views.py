from django.http import HttpResponse
from rest_framework import viewsets
import json

from .models import Pereval_added, Users, Coords, Pereval_areas, Pereval_images, Spr_activities_types
from .serializers import PerevalSerializer, UsersSerializer, CoordsSerializer, Pereval_areasSerializer, \
    Pereval_imagesSerializer, Spr_activities_typesSerializer

#создание представлений


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer


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


def submitData(request):
    if request.method == 'POST':
        json_params = json.loads(request.body)

        pereval_added = Pereval_added.objects.create(
            beautyTitle=json_params['beautyTitle'],
            title_added=json_params['title_added'],
            other_titles=json_params['other_titles'],
            connect=json_params['connect'],
            add_time=json_params['add_time'],
            area=Pereval_areas.objects.create(
                title_area=json_params['title_area']
            ),
            coord_id=Coords.objects.create(
                coord_id=json_params['coord_id']
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
            "add_time": pereval_added.add_time,
            "area": pereval_added.area,
            "coord_id": pereval_added.coord_id,
            "author": pereval_added.author,
        }))

