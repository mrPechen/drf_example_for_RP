from RP_app.api.celery_dir.celery import app
from RP_app.api.services.currency_service import CurrencyService


@app.task()
def run_task():
    CurrencyService().daily_add_currencies()
