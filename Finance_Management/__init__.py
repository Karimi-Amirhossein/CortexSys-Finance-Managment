"""
Initialize Celery app when Django starts.
Ensures @shared_task decorators use this app instance.
"""

from .celery import app as celery_app

__all__ = ("celery_app",)