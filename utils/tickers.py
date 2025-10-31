from types import MethodType,FunctionType

class Ticker():
    _cooldown : int
    _current : int

    _connected_functions : list[MethodType|FunctionType]

    def __init__(self,cooldown : int,current : int = 200000) -> None:
        self._cooldown = cooldown
        self._current = min(current,cooldown)

        self._connected_functions = []

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
    
    def connect(self,function : MethodType|FunctionType):
        self._connected_functions.append(function)
    def disconnect(self,function : MethodType|FunctionType):
        self._connected_functions.remove(function)

    def on_ready(self) -> None:
        if self.ready:
            for function in self._connected_functions:
                function()

    def tick(self) -> None:
        self._current = min(self._current + 1,self._cooldown)
        self.on_ready()

    def reset(self) -> None:
        self._current = 0