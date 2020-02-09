from django.urls import path


urlpatterns = [
    # path('example/', include('{{ project_name_admin }}.example.urls', namespace='example')),
]

if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
