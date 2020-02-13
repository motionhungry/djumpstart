from config.settings.base import (
    ROOT_DIR, INSTALLED_APPS, STATICFILES_DIRS, TEMPLATES,
)

APPS_DIR = ROOT_DIR.path('{{ project_name }}_admin')
TEMPLATES[0]['DIRS'] = [str(APPS_DIR.path('templates'))]

STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]

ROOT_URLCONF = '{{ project_name }}_admin.urls'

INSTALLED_APPS += []
