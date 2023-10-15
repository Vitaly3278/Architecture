from homework2.ItemFabric import ItemFabric
from homework2.CupperReward import CupperReward


class CupperGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (медь)")
        return CupperReward()