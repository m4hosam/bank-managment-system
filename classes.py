from SQLconnection import cursor, connection
import datetime


def getCurrencyRate(currency):
    cursor.execute(
        '''SELECT exch_rate FROM currency 
        WHERE currency.curr_code = ?''', currency)
    row = cursor.fetchone()
    if(row):
        return float(row.exch_rate)
    else:
        print("ERROR in get Currency Rate")
        return -1


def searchAccountIDs(r_id):
    cursor.execute(
        '''SELECT a.acc_id, a.currency, a.balance 
            FROM account2 As a''')
    rows = cursor.fetchall()
    for row in rows:
        if(r_id == row.acc_id):
            return Account(row)
    return 1


class Account:
    def __init__(self, account):
        self.account_id = account.acc_id
        self.currency = account.currency
        self.balance = account.balance

    def save(self):
        cursor.execute(
            '''INSERT INTO account2 
            VALUES(?, ?, ?)''', self.account_id, self.currency, self.balance)
        connection.commit()

    def delete(self):
        cursor.execute(
            '''DELETE account2 
            WHERE id = ?''', self.account_id)
        connection.commit()

    def get_balence(self):
        return self.balance

    def get_currency(self):
        return self.currency

    def withdraw(self, value):
        print("before self.balance: " + str(self.balance))
        self.balance = int(self.balance) - int(value)
        print("withdraw self.balance: " + str(self.balance)+"\n\n")
        if(self.balance >= 0):
            cursor.execute(
                '''UPDATE account2
                SET account2.balance = ?
                WHERE account2.acc_id = ?''', self.balance, self.account_id)
            t = datetime.datetime.now()
            cursor.execute(
                '''INSERT INTO transactions2 
                VALUES( ? ,?,NULL,'withdraw',?)
                ''', t, self.account_id, value)
            connection.commit()

    def deposit(self, value):
        print("before self.balance: " + str(self.balance))
        self.balance = int(self.balance) + int(value)
        print("deposit self.balance: " + str(self.balance)+"\n\n")
        cursor.execute(
            '''UPDATE account2
            SET account2.balance = ?
            WHERE account2.acc_id = ?''', self.balance, self.account_id)
        t = datetime.datetime.now()
        cursor.execute(
            '''INSERT INTO transactions2 
            VALUES( ? ,NULL,?,'deposit',?)
            ''', t, self.account_id, value)
        connection.commit()

    def money_transfer(self, receiver, amount):
        # Exchange rate logic should be here
        t = datetime.datetime.now()
        c1 = self.currency
        c2 = receiver.currency
        new_balance1 = int(self.balance) - int(amount)
        if (c1 == c2):
            new_balance2 = int(receiver.balance) + int(amount)
        else:
            amount_in_TL = float(amount) * getCurrencyRate(c1)
            amount_in_c = amount_in_TL / getCurrencyRate(c2)
            new_balance2 = int(receiver.balance) + amount_in_c

        if(new_balance1 >= 0):
            # Source balance Change
            cursor.execute(
                '''UPDATE account2
                 SET account2.balance = ?
                 WHERE account2.acc_id = ?''', new_balance1, self.account_id)
            # Receiver balance Change
            cursor.execute(
                '''UPDATE account2
                 SET account2.balance = ?
                 WHERE account2.acc_id = ?''', new_balance2, receiver.account_id)
            cursor.execute(
                '''INSERT INTO transactions2 
                VALUES( ? ,?,?,'money transfer',?)
                ''', t, self.account_id, receiver.account_id, amount)
            connection.commit()
        else:
            print("Transfer Denied Classes Related")

    def __str__(self):
        return f"----\n({self.account_id}  |  {self.currency}  | {self.balance})\n----"


class Customer:
    def __init__(self, customer_id):
        self.accounts = []
        self.transactions = []
        self.customer_id = customer_id
        cursor.execute(
            'SELECT * FROM customer2 WHERE customer2.id = ?', customer_id)
        row = cursor.fetchone()
        if(not row):
            print("Customer not Found Class Related")
        else:
            self.first_name = row.firstN
            self.last_name = row.lastN
            self.email = row.email
            self.phone = row.phone
            self.TC = row.TC
            self.address = row.adress

    def list_accounts(self):
        cursor.execute(
            '''SELECT a.acc_id, a.currency, a.balance 
            FROM account2 As a, userAccounts2 As u 
            WHERE u.acc_id = a.acc_id AND u.cus_id = ?''', self.customer_id)
        rows = cursor.fetchall()
        for row in rows:
            self.accounts.append(Account(row))
        return self.accounts

    def list_transactions(self):
        cursor.execute(
            '''SELECT DISTINCT t.trans_no, t.trans_date, t.src_id, t.rsv_id, t.trans_type, t.total, t.cus_id
            FROM customer2 c, transactions2 t, account2 a, userAccounts2 ua
            WHERE c.id = ua.cus_id and
            ua.acc_id = a.acc_id and
            (t.src_id = a.acc_id OR t.cus_id = c.id) and
            c.id = ?
            ORDER BY(t.trans_date)''', self.customer_id)
        rows = cursor.fetchall()
        # print(rows)
        for row in rows:
            self.transactions.append(row)
        return self.transactions

    def request_update(self, first_name, last_name, email, phone, tc, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.TC = tc
        self.address = address
        cursor.execute(
            '''
            INSERT INTO update_customer
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', self.customer_id, self.first_name, self.last_name, self.email, self.phone, self.TC, self.address)
        connection.commit()

    # The next function should be edited in clerk (update)

    def __str__(self):
        return f"----\n({self.customer_id}, {self.first_name},{self.last_name}, {self.email}, {self.phone}, {self.TC}, {self.address})\n---"


# k = getCurrencyRate("USD")
# print(k)

# class Transactions:
#     def __init__(self, ob):
#         self.first_nametra = ob.trans_no
#         self.last_name = ob.trans_date
#         self.email = ob.src_id
#         self.phone = ob.rsv_id
#         self.TC = ob.trans_type
#         self.address = ob.Adress
