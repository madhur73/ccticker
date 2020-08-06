from django.urls import path
from .views import TickerView
from .consumers import TickerConsumer

urlpatterns = [
    path('', TickerView.as_view()),
]

websocket_urlpatterns = [
    path('ws/<str:cryptocoin>/<str:source>', TickerConsumer),
]