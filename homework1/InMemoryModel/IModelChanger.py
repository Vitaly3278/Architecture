from abc import ABCMeta, abstractmethod
class IModelChanger:
    __metaclass__ = ABCMeta

    @abstractmethod
    def notify_change(self, sender):
        pass