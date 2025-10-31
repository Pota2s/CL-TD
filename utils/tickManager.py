from types import MethodType
from .tickers import Ticker

class TickManager():
    
    _tickers : list[Ticker] = []
    
    @staticmethod
    def tick():
        for ticker in TickManager._tickers:
            ticker.tick()