from datetime import date
from random import randint, uniform
from typing import List

from homework4.models.ticket import Ticket
from homework4.interfaces.iTicketRepo import ITicketRepo

class TicketRepo(ITicketRepo):

    def __init__(self):
       self.tickets: List[Ticket] = []

    def repo_generation(self):
        """ создание базы данных билетов"""
        for i in range(20):
            year = randint(2023, 2023)
            month = randint(2, 2)
            day = randint(23, 26)
            ticket_date = date(year, month, day)
            self.tickets.append(Ticket(randint(1, 8), randint(1, 100), round(uniform(10, 100), 2), ticket_date))

            print(self.tickets[i])
    def readAll(self, routeNumber: int) -> List[Ticket]:
        routeTickets = []
        for ticket in self.tickets:
            if ticket.getRouteNumber() == routeNumber and ticket.getValid() == True:
                routeTickets.append(ticket)
        if len(routeTickets) == 0:
            raise RuntimeError("There are no tickets for this route.")
        return routeTickets

    def update(self, ticket: Ticket):
        for tick in self.tickets:
            if tick.getId() == ticket.getId():
                tick.setValid(False)

            print(tick)
