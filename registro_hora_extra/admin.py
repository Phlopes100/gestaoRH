from django.contrib import admin
from .models import RegistroHoraExtra


@admin.register(RegistroHoraExtra)
class RegistroHoraExtraAdmin(admin.ModelAdmin):
    list_display = ['motivo']

