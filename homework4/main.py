from datetime import date

from homework4.core.customer import Customer
from homework4.models.user import User

if __name__ == '__main__':


    user = User("Mark", 1234567898765432)

    customer = Customer(user)

    customer_searching_route = 5
    customer_searching_date = date(2023, 2, 25)
    print("\n")
    customer_tickets_search_result = customer.searchTicket(customer_searching_date, customer_searching_route)
    print("\n")
    print('log: found tickets for date')
    print(*customer_tickets_search_result)
    print('log: buying first ticket')
    print(customer.buyTicket(customer_tickets_search_result[0]))

