from homework2.IGameItem import IGameItem

class GemReward(IGameItem):
    def open(self):
        print("Открыли сундук с драгоценными камнями")