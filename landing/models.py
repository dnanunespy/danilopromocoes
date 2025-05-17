from django.db import models

class RegistroAcesso(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    def __str__(self):
        return f"Acesso em {self.data_hora}"

class CliqueGrupoWhatsApp(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    def __str__(self):
        return f"Clique em {self.data_hora}"
    
class RegistroGeolocalizado(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return f"{self.data_hora} - ({self.latitude}, {self.longitude})"    