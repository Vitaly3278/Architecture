class BancRepo:

    def __init__(self):
        self.banc_data={}
        self.banc_data={1234567898765432: 10000}
    def request(self, bill, cardNumber):
        if bill < self.banc_data[cardNumber]:
            self.banc_data[cardNumber] = self.banc_data[cardNumber]-bill
            return True
        else:
            return False