from abc import ABC,abstractmethod

class TowerBase(ABC):
    """
    An abstract class for all towers to inherit.
    
    Args:
        _cost (int) : The turret's cost to deploy.
        _health (int) : The turret's health.
    """
    _cost : int
    _health : int 

    def __init__(self,cost : int ,health : int ) -> None:
        super().__init__()
        self._cost = cost
        self._health = health

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