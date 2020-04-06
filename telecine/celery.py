# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telecine.settings')

app = Celery('telecine')
# STARTED state is not enabled by default so we flip it on
app.conf.update(task_track_started=True)
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load tasks from all registered apps
app.autodiscover_tasks()

# ========================================================
# Celery configuration http://docs.celeryproject.org/en/latest/userguide/configuration.html
# ========================================================

# List of modules to import when the Celery worker starts.
imports = ('telecine.tasks',)

# ------------------------------
# general-settings
# ------------------------------
# A white-list of content-types/serializers to allow.
app.conf.accept_content = ['application/json']
# By default it is the same serializer as accept_content
app.conf.result_accept_content = ['application/json']

# ------------------------------
# time-and-date-settings
# ------------------------------
app.conf.enable_utc = False
# The timezone value can be any time zone supported by the pytz library
app.conf.timezone = 'US/Eastern'

# ------------------------------
# task-settings
# ------------------------------
app.conf.task_serializer = 'json'
# will be retried in the case of connection loss or other connection errors
app.conf.task_publish_retry = True
# The worker stores all task errors in the result
app.conf.task_store_errors_even_if_ignored = True
# Report its status as ‘started’ when the task is executed by a worker
app.conf.task_track_started = True
# Task hard time limit in seconds. (30 min)
app.conf.task_time_limit = 30 * 60
# Task soft time limit in seconds. (20 min)
app.conf.task_soft_time_limit = 20 * 60

# ------------------------------
# task-result-backend-settings
# ------------------------------
# Using the database to store task state and results.
# result_backend = 'db+postgresql://scott:tiger@localhost/mydatabase'
app.conf.result_backend = 'django-db'
# Default: json since 4.0
app.conf.result_serializer = 'json'
# written to backend (name, args, kwargs, worker, retries, queue, delivery_info)
app.conf.result_extended = True

# ------------------------------
# broker & redis settings
# ------------------------------
app.conf.broker_url = 'redis://redis:6379/0'
# Max nb tasks a pool worker process can execute before it’s replaced with a new one.
app.conf.worker_max_tasks_per_child = 100
# Max amount of resident memory, in kilobytes (150000==150 MB)
# It allocates up to some % to Celery
app.conf.worker_max_memory_per_child = 150000
# Max nb connections available in the Redis connection pool used for sending and retrieving results.
app.conf.redis_max_connections = 1

# ------------------------------
# events
# ------------------------------
app.conf.worker_send_task_events = True

# ------------------------------
# beat-settings-celery-beat
# ------------------------------
app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'telecine.tasks.debug_task',
        'schedule': 30.0,
        # 'args': (16, 16)
    },
}
