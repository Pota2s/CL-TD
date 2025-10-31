from abc import ABC,abstractmethod
from utils.tickers import Ticker

class TowerBase(ABC):
    """
    An abstract class for all towers to inherit.
    
    Args:
        _cost (int) : The turret's cost to deploy.
        _health (int) : The turret's health.
    """
    _cost : int
    _health : int 
    _Ticker : Ticker

    def __init__(self,cost : int ,health : int, cooldown : int = 1, current : int = 1 ) -> None:
        super().__init__()
        self._cost = cost
        self._health = health
        self._Ticker = Ticker(cooldown,current)

    @property
    def health(self) -> int:
        return self._health
    @health.setter
    def health(self,health) -> None : 
        self._health = health

    @property
    def cost(self) -> int:
        return self._cost
    @cost.setter
    def cost(self,cost : int) -> None:
        self._cost = cost

class AutoTowerBase(TowerBase):
    def __init__(self, cost: int, health: int, cooldown: int = 1, current: int = 1) -> None:
        super().__init__(cost, health, cooldown, current)
        self._Ticker.connect(self.on_cooldown)

    @abstractmethod
    def on_cooldown(self):
        pass

    
    