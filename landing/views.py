from django.shortcuts import render
from .models import RegistroAcesso, CliqueGrupoWhatsApp, RegistroGeolocalizado

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    RegistroAcesso.objects.create(
        ip=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT', '')
    )
    return render(request, 'index.html')

@csrf_exempt
def registrar_clique(request):
    if request.method == 'POST':
        CliqueGrupoWhatsApp.objects.create(
            ip=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT', '')
        )
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'error': 'invalid request'}, status=400)


@csrf_exempt
def salvar_localizacao(request):
    if request.method == 'POST':
        lat = float(request.POST.get('lat', 0))
        lon = float(request.POST.get('lon', 0))
        RegistroGeolocalizado.objects.create(
            ip=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            latitude=lat,
            longitude=lon
        )
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'error': 'Requisição inválida'}, status=400)