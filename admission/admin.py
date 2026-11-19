from django.contrib import admin

# Register your models here.
from .models import Admission
# Register your models here.
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('id','stu_name', 'stu_fname', 'stu_age', 'stu_class', 'stu_fphone', 'stu_fee')
admin.site.register(Admission, AdmissionAdmin)