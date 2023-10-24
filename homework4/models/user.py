import itertools

class User:
    id_iter = itertools.count()

    def __init__(self, userName: str, cardNumber: int):
        self.id = next(self.id_iter)
        self.userName = userName
        self.cardNumber = cardNumber

    def getId(self):
        return self.id

    def getUserName(self):
        return self.userName

    def getCardNumber(self):
        return self.cardNumber

    def __str__(self):
        return f"Client {self.id} userName= {self.userName} cardNumber= {self.cardNumber}"

