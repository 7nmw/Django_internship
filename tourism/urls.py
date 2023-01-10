"""tourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include

from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_urls

from pereval import views
from pereval.views import PerevalViewSet, UsersViewSet, CoordsViewSet, Pereval_areasViewSet, Pereval_imagesViewSet, \
    Spr_activities_typesViewSet, submitData, submitDataGetPatch

router = routers.DefaultRouter()
router.register(r'Pereval_added', PerevalViewSet)
router.register(r'Users', UsersViewSet)
router.register(r'Coords', CoordsViewSet)
router.register(r'Pereval_areas', Pereval_areasViewSet)
router.register(r'Pereval_images', Pereval_imagesViewSet)
router.register(r'Spr_activities_types', Spr_activities_typesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', include(router.urls)),
    path('api/v1/submitData/', submitData),
    path('api/v1/submitData/<int:Pereval_added_id>', submitDataGetPatch)
]

urlpatterns += doc_urls