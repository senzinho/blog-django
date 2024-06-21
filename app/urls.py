from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import noticia_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', noticia_view, name='noticia_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
