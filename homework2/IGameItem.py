from abc import ABCMeta, abstractmethod

class IGameItem():
    __metaclass__ = ABCMeta

    @abstractmethod
    def open(self):
        pass