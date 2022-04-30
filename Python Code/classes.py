class Customer:
    def __init__(self, object):
        self.customer_id = object.id
        self.first_name = object.firstN
        self.last_name = object.lastN
        self.email = object.email
        self.phone = object.phone
        self.TC = object.TC
        self.address = object.Adress


class Account:
    def __init__(self, acc_id, currency, balance):
        self.acc_id = acc_id
        self.currency = currency
        self.balance = balance
