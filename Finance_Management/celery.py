"""
Celery configuration for the Finance_Management project.
Integrates Celery with Django settings and autodiscovers tasks.
"""

import os
import sys
from pathlib import Path
from celery import Celery
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

# Set default Django settings module for Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Finance_Management.settings")

# Create Celery app
app = Celery("Finance_Management")

# Load settings with CELERY_ prefix from Django settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Autodiscover tasks.py files in all installed apps
app.autodiscover_tasks()