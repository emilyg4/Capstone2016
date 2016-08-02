from django.contrib import admin
#from django.contrib.gis import admin

# Register your models here.
from .models import Meetup
#, WorldBorder

admin.site.register(Meetup)
#admin.site.register(WorldBorder, admin.GeoModelAdmin)