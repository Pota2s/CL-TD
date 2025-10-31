from towers.tower import TowerBase
from utils.tickManager import TickManager

class worldManager:
    lanes : list[list[ TowerBase | None]]

    def __init__(self, width : int = 5, length: int = 9) -> None:
        self.lanes = []
        for i in range(width):
            self.lanes.append([])
            for j in range(length):
                self.lanes[i].append(None)

    
    def add_tower(self,tower : TowerBase,row : int ,column : int):
        TickManager.add_ticker(tower._Ticker)
        self.lanes[row][column] = tower

if __name__ == "__main__":
    wm = worldManager()
    print(*wm.lanes,sep="\n")