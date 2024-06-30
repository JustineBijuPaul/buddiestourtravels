from django.contrib import admin
from home.models import Detail, Package, Location, Gallery
# Register your models here.

myModels = [Detail, Package, Location, Gallery]
admin.site.register(myModels)
admin.site.site_header  =  "Buddies Tourlines"  
admin.site.site_title  =  "BT Admin"
admin.site.index_title  =  "Admin"