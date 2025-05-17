from django.contrib import admin
from .models import RegistroAcesso, CliqueGrupoWhatsApp, RegistroGeolocalizado

admin.site.register(RegistroAcesso)
admin.site.register(CliqueGrupoWhatsApp)
admin.site.register(RegistroGeolocalizado)

# Register your models here.
