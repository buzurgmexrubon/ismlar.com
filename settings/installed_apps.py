import os
import sys

from settings.base import BASE_DIR

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "apps.common.apps.CommonConfig",
    "apps.names.apps.NamesConfig",
    "apps.origins.apps.OriginsConfig",
    "apps.continents.apps.ContinentsConfig",
]

THIRD_APPS = []

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_APPS

APP_DIR = os.path.join(BASE_DIR, "apps")
if os.path.isdir(APP_DIR):
    sys.path.append(APP_DIR)
