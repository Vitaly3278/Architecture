import datetime
import itertools


class Ticket:
    id_iter = itertools.count()
    def __init__(self, routeNumber, place, price, date):
        self.id = next(self.id_iter)
        self.routeNumber = routeNumber
        self.place = place
        self.price = price
        self.date = date
        self.isValid = True

    def getRouteNumber(self):
        return self.routeNumber

    def getValid(self):
        return self.isValid

    def getDate(self):
        return self.date

    def getPrice(self):
        return self.price

    def setValid(self, status: bool):
        self.isValid = status

    def getId(self):
        return self.id

    def __str__(self):
        return f"ticket {self.id}, routeNumber:{self.routeNumber}, date:{self.date}, price:{self.price}, place: {self.place}, isValid:{self.isValid}"





