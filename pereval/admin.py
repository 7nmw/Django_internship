from django.contrib import admin

# Register your models here.
from .models import Users, Coords, Pereval_areas, Pereval_added, Pereval_images, Spr_activities_types

admin.site.register(Users)
admin.site.register(Coords)
admin.site.register(Pereval_areas)
admin.site.register(Pereval_added)
admin.site.register(Pereval_images)
admin.site.register(Spr_activities_types)