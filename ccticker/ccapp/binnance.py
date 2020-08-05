class Binnance():

	def __init__(self, endpoint):
		self.url = endpoint

	def get_buy_price(self, resp):
		return resp['bidPrice']

	def get_sell_price(self, resp):
		return resp['askPrice']

	def get_data(self, symbol):
		resp = requests.get( self._url() + symbol)
		#print(resp.json())
		if resp.status_code != 200:
	    # self means something went wrong.
	 		#raise ApiError('GET /tasks/ {}'.format(resp.status_code))
	 		print("ApiError")

		return resp.json()

	def _url(self):
		return self.url +'?symbol='

	def get_btc_prices(self):
		res = {}
		res['source'] = 'binnance'
		resp_obj = self.get_data('BTCUSDT')
		res['buy'] = self.get_buy_price(resp_obj)
		res['sell'] = self.get_sell_price(resp_obj)
		return res

	def get_eth_prices(self):
		res = {}
		resp_obj = self.get_data('ETHUSDT')
		res['source'] = 'binnance'
		res['buy'] = self.get_buy_price(resp_obj)
		res['sell'] = self.get_sell_price(resp_obj)
		return res