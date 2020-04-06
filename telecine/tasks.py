from celery import shared_task
from celery.exceptions import SoftTimeLimitExceeded


@shared_task(time_limit=60)
def celery_email_send():
    print(f"TODO Sending email ... ")
    return None


@shared_task
def debug_task():
    try:
        print('Request: OK')
    except SoftTimeLimitExceeded:
        print(f"cleanup_in_a_hurry")
