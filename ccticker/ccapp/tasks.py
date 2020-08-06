from celery import shared_task
from .prices import Prices
from django.core.cache import cache


'''
@shared_task
def example_task():
    import logging
    k = Kraken(KRAKEN_URL)
    b = Binnance(BINNANCE_URL)
    logging.info(k.get_btc_prices())
    logging.info(b.get_btc_prices())
'''
@shared_task
def update_cc_prices():
	prices_obj 	= Prices()
	cryptocoins = ['ETH', 'BTC']
	sources		= ['BIN','KRA']
	response 	= prices_obj.get_current_prices(cryptocoins, sources)

	for cryptocoin in cryptocoins:
		for source in sources:
			ticker_code = cryptocoin + source
			cache.set(ticker_code, response[cryptocoin][source])




