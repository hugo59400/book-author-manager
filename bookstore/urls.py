from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),  # quand tu créeras le fichier urls.py de l'app
]

# Gestion des fichiers médias (images uploadées)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
