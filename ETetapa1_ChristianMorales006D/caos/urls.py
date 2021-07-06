from django.urls import path
from .views import index, creaar, ver, eliminar, modificar
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name="index"),
    path('creaar', creaar, name="creaar"),
    path('ver', ver, name="ver"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)