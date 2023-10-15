from abc import ABCMeta, abstractmethod

class ItemFabric():
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_item(self):
        pass