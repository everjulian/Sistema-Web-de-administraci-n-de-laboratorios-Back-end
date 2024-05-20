from django.contrib import admin
from .models import ActivosModel

admin.site.site_header = 'Register data'
admin.site.index_title = 'My records'
admin.site.site_title = 'Web Inventory'

# Register your models here.
admin.site.register(ActivosModel)