from django.contrib import admin
from cal.models import Reader


# Register your models here.


class ReadersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reader._meta.fields]
    list_filter = ['email', 'phone', 'start_time']
    search_fields = ['name', 'surname', 'email', 'phone', 'start_time']
    #list_display = ['name', 'surname', 'email',  'phone', 'start_time']







admin.site.register(Reader,ReadersAdmin )