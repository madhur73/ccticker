from django.shortcuts import render

from django.views.generic import TemplateView

class TickerView(TemplateView):
    template_name = 'ccapp/tickers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticker_codes'] = [
            'ETHBIN',
            'ETHKAR',
            'BTCBIN',
            'BTCKAR',
        ]
        return context
# Create your views here.
