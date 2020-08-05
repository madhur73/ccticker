import requests

class Kraken():

	def __init__(self, endpoint):
		self.url = endpoint

	def get_buy_price(self, resp):
		return resp['a'][0]

	def get_sell_price(self, resp):
		return resp['b'][0]

	def get_data(self, symbol):
		resp = requests.get( self._url() + symbol)
		#print(resp.json())
		if resp.status_code != 200 or (resp.json()['error'] is None):
	    # self means something went wrong.
	 		#raise ApiError('GET /tasks/ {}'.format(resp.status_code))
	 		print("ApiError")

		return resp.json()['result'][symbol]

	def _url(self):
		return self.url +'?pair='

	def get_btc_prices(self):
		res = {}
		resp_obj = self.get_data('XXBTZUSD')
		res['buy'] = self.get_buy_price(resp_obj)
		res['sell'] = self.get_sell_price(resp_obj)
		return res

	def get_eth_prices(self):
		res = {}
		resp_obj = self.get_data('XETHZUSD')
		res['buy'] = self.get_buy_price(resp_obj)
		res['sell'] = self.get_sell_price(resp_obj)
		return res
