from celery import shared_task
from .kraken import Kraken

@shared_task
def example_task():
    import logging
    k = Kraken('https://api.kraken.com/0/public/Ticker')
    logging.info(k.get_btc_prices())