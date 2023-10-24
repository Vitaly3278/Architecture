import itertools
from typing import List
from datetime import date
from homework4.interfaces.iCustomer import ICustomer
from homework4.models.ticket import Ticket
from homework4.models.user import User
from homework4.core.ticketProvider import TicketProvider
from homework4.core.cashProvider import CashProvider


class Customer(ICustomer):
    id_iter = itertools.count()
    def __init__(self, user: User):
        self.id = next(self.id_iter)

        self.ticketProvider = TicketProvider()
        self.cashProvider = CashProvider()
        self.client = user
        self.selectedTickets = []

    def getSelectedTickets(self) -> List[Ticket]:
        return self.selectedTickets

    def setSelectedTickets(self, selectedTickets: List[Ticket]) -> None:
        self.selectedTickets = selectedTickets

    def buyTicket(self, ticket: Ticket) -> bool:
        flag: bool

        self.cashProvider.authorization(self.client)
        flag = self.cashProvider.buy(ticket)
        if flag:
            flag = self.ticketProvider.updateTicketStatus(ticket)
        return flag

    def searchTicket(self, date: date, route: int) -> List[Ticket]:
        result = []
        list = self.ticketProvider.getTickets(route)
        print('log: found tickets for rooute')
        for ticket in list:
            print(ticket)
            if ticket.getDate() == date:
                result.append(ticket)
        if not result:
            raise RuntimeError("There are no tickets for this date")
        return result