from homework2.IGameItem import IGameItem

class SilverReward(IGameItem):
    def open(self):
        print("Открыли сундук с серебром")