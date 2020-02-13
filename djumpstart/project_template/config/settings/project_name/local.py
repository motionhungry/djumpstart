from config.settings.local import *
from .base import *


# Celery
# ------------------------------------------------------------------------------
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# Simple JWT
# ------------------------------------------------------------------------------
SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY
