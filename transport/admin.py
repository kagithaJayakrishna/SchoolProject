from django.contrib import admin

# Register your models here.
from .models import TransportDetail, RouteDetail
# Register your models here.
class TransportDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'stu_name', 'route', 'fees')
admin.site.register(TransportDetail, TransportDetailAdmin)

class RouteDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'route_name', 'distance', 'fees')
admin.site.register(RouteDetail, RouteDetailAdmin)