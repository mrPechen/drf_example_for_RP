import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RP_app.root.settings')

import django

django.setup()

from celery import Celery
from environs import Env

env = Env()
env.read_env()

app = Celery('celery',
             broker=f"amqp://{env.str('RABBITMQ_DEFAULT_USER')}:{env.str('RABBITMQ_DEFAULT_PASS')}@{env.str('RABBITMQ_HOST')}:{env.str('RABBITMQ_PORT')}//")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'repeat everyday 5 minutes': {
        'task': 'RP_app.api.services.tasks.run_task',
        'schedule': 300.0,
    },
}
