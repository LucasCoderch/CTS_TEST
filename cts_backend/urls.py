from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

# importa las vistas de API
from raffle.api import ParticipantListView, RaffleDrawView
from users.api import RegisterView, VerifyEmailView

def root(request):
    # endpoint de salud en /
    return JsonResponse({"status": "ok", "app": "CTS API", "version": 1})

urlpatterns = [
    path("", root, name="root"),

    # Admin
    path("admin/", admin.site.urls),

    # API pública (registro y verificación por correo)
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/verify/<str:token>/", VerifyEmailView.as_view(), name="verify-email"),

    # API para admin (listar y sortear)
    path("api/participants/", ParticipantListView.as_view(), name="participants-list"),
    path("api/raffle/draw/", RaffleDrawView.as_view(), name="raffle-draw"),
]
