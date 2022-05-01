from SQLconnection import cursor


class Customer:
    accounts = []
    transactions = []

    def __init__(self, object):
        self.customer_id = object.id
        self.first_name = object.firstN
        self.last_name = object.lastN
        self.email = object.email
        self.phone = object.phone
        self.TC = object.TC
        self.address = object.Adress

    def list_accounts(self):
        cursor.execute(
            'SELECT a.acc_id, a.currency, a.balance FROM account As a, userAccounts As u WHERE u.acc_id = a.acc_id AND u.cus_id = ?', self.customer_id)
        rows = cursor.fetchall()
        for row in rows:
            self.accounts.append(Account(row))

        return self.accounts

    def list_transactions(self):
        cursor.execute(
            '''SELECT DISTINCT t.trans_no, t.trans_date, t.src_id, t.rsv_id, t.trans_type, t.total, t.cus_id
            FROM customer c, transactions t, account a, userAccounts ua
            WHERE c.id = ua.cus_id and
            ua.acc_id = a.acc_id and
            (t.src_id = a.acc_id OR t.cus_id = c.id) and
            c.id = ?
            ORDER BY(t.trans_date)''', self.customer_id)
        rows = cursor.fetchall()
        print(rows)
        for row in rows:
            self.transactions.append(row)

        return self.transactions

    def __str__(self):
        return f"----\n({self.customer_id}, {self.first_name},{self.last_name}, {self.email}, {self.phone}, {self.TC}, {self.address})\n---"


class Account:
    def __init__(self, account):
        self.account_id = account.acc_id
        self.currency = account.currency
        self.balance = account.balance

    def save(self):
        cursor.execute(
            'INSERT INTO account VALUES(?, ?, ?)', self.account_id, self.currency, self.balance)

    def __str__(self):
        return f"----\n({self.account_id}, {self.currency},{self.balance})\n----"
