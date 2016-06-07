from django.contrib import admin
from .models import *

class siva(admin.ModelAdmin):
	search_fields=('first_name','last_name',)


# Register your models here.
admin.site.register(student,siva)