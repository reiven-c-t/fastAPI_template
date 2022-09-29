from time import sleep

from celery import Celery

from core.config import settings

celery = Celery(__name__)
celery.conf.broker_url = settings.CELERY_BROKER_URL
celery.conf.result_backend = settings.CELERY_BACKEND_URL


@celery.task(name="tasks.demo_function")
def demo_function(weight: float, height: float) -> float:
    sleep(30)
    bmi = weight / height**2
    return bmi
