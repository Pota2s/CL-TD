class Ticker():
    _cooldown : int
    _current : int

    @property
    def cooldown(self) -> int: 
        return self._cooldown
    @cooldown.setter
    def cooldown(self,cooldown : int) -> None:
        self._cooldown = cooldown

    @property
    def current(self) -> int:
        return self._current
    @current.setter
    def current(self, current : int) -> None:
        self._current = current 
    
    @property
    def ready(self) -> bool:
        return self._current == self._cooldown
    
    def tick(self) -> None:
        self._current = min(self._current + 1,self._cooldown)

    def reset(self) -> None:
        self._current = 0