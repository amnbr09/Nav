from django.contrib import admin

from .models import Doc
from django.contrib import admin
from presence_service.models import Viewers
# Register your models here.
admin.site.register(Viewers)
#admin.site.register(Doc)