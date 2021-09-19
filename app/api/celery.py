from __future__ import absolute_import
from __future__ import unicode_literals
from celery import Celery, shared_task

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
# app = Celery("api", broker="pyamqp://guest:guest@rabbitmq:15672//")
app = Celery("api")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@shared_task(bind=True)
def producer(self, xnum, ynum):
    zsum = xnum + ynum
    return zsum
