import random

from homework2.GemGenerator import GemGenerator
from homework2.GoldGenerator import GoldGenerator
from homework2.SilverGenerator import SilverGenerator
from homework2.CupperGenerator import CupperGenerator

if __name__ == '__main__':
    fabricList = [GemGenerator(), GoldGenerator(), SilverGenerator(), CupperGenerator()]
    for i in range(5):
        rnd = random.choice(fabricList).create_item().open()