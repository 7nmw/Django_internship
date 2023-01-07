from rest_framework import serializers
from .models import Pereval_added, Users, Coords, Pereval_areas, Pereval_images, Spr_activities_types

#создание сериализатора


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval_added
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class Pereval_areasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval_areas
        fields = '__all__'


class Pereval_imagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval_images
        fields = '__all__'


class Spr_activities_typesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spr_activities_types
        fields = '__all__'
