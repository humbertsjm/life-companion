from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from main_app.views import IndexPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    # Static files
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]
