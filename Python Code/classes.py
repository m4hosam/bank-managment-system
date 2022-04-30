class Customer:
    def __init__(self, object):
        self.customer_id = object.id
        self.first_name = object.firstN
        self.last_name = object.lastN
        self.email = object.email
        self.phone = object.phone
        self.TC = object.TC
        self.address = object.Adress

    def __str__(self):
        return f"----\n({self.customer_id}, {self.first_name},{self.last_name}, {self.email}, {self.phone}, {self.TC}, {self.address})\n---"


class Account:
    def __init__(self, account):
        self.account_id = account.acc_id
        self.currency = account.currency
        self.balance = account.balance

    def __str__(self):
        return f"----\n({self.account_id}, {self.currency},{self.balance})\n----"
