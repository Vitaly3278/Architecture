from homework4.models.ticket import Ticket
from homework4.services.ticketRepo import TicketRepo


class TicketProvider:
    def __init__(self):
        self.ticketRepo = TicketRepo()
        self.ticketRepo.repo_generation()

    def getTickets(self, routeNumber):
        return self.ticketRepo.readAll(routeNumber)

    def updateTicketStatus(self, ticket: Ticket):
        self.ticketRepo.update(ticket)