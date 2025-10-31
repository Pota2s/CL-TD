from types import MethodType
from utils.tickers import Ticker

class TickManager():
    
    _tickers : list[Ticker] = []
    
    @staticmethod
    def tick():
        for ticker in TickManager._tickers:
            ticker.tick()

    @staticmethod
    def add_ticker(ticker : Ticker):
        TickManager._tickers.append(ticker)
    @staticmethod
    def remove_ticker(ticker : Ticker):
        TickManager._tickers.remove(ticker)