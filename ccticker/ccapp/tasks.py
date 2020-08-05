from celery import shared_task
from .kraken import Kraken
from .binance import Binance
from django.core.cache import cache

BINNANCE_URL = 'https://api.binance.com/api/v3/ticker/bookTicker'
KRAKEN_URL = 'https://api.kraken.com/0/public/Ticker'
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
	cryptocoins = ['ETH', 'BTC']
	kraken_obj = Kraken(KRAKEN_URL)
	binance_obj = Binance(BINNANCE_URL)
	
	btc = {}
	eth = {}
	#btc.append(kraken_obj.get_btc_prices())
	#btc.append(binance_obj.get_btc_prices())
	btc['binnance'] = binance_obj.get_btc_prices()
	btc['kraken']   = kraken_obj.get_btc_prices()
	eth['binnance'] = binance_obj.get_eth_prices()
	eth['kraken']   = kraken_obj.get_eth_prices()
	cache.set('ETH',eth)
	cache.set('BTC',btc)



