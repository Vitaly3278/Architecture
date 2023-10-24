from abc import ABC, abstractmethod
from typing import List
from datetime import date
from homework4.models.ticket import Ticket


class ICustomer(ABC):
    @abstractmethod
    def getSelectedTickets(self) -> List[Ticket]:
        pass

    @abstractmethod
    def setSelectedTickets(self, selectedTickets: List[Ticket]) -> None:
        pass

    @abstractmethod
    def buyTicket(self, ticket: Ticket) -> bool:
        pass

    @abstractmethod
    def searchTicket(self, date: date, route: int) -> List[Ticket]:
        pass