class Customer:
    def __init__(self, id, firstName, lastName, email, TC, address, phone):
        self.id = id
        self.fistName = firstName
        self.lastName = lastName
        self.email = email
        self.TC = TC
        self.address = address
        self.phone = phone


class Account:
    def __init__(self, acc_id, currency, balance):
        self.acc_id = acc_id
        self.currency = currency
        self.balance = balance
