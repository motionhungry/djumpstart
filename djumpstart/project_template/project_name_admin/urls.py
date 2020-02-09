from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.views.generic import TemplateView as DjangoTemplateView


urlpatterns = [
    # path('example/', include('{{ project_name_admin }}.example.urls', namespace='example')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
