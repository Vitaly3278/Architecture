from homework2.ItemFabric import ItemFabric
from homework2.GemReward import GemReward


class GemGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (др. камень)")
        return GemReward()