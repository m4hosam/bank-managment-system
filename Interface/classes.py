from SQLconnection import cursor, connection


class Account:
    def __init__(self, account):
        self.account_id = account.acc_id
        self.currency = account.currency
        self.balance = account.balance

    def save(self):
        cursor.execute(
            '''INSERT INTO account 
            VALUES(?, ?, ?)''', self.account_id, self.currency, self.balance)
        connection.commit()

    def delete(self):
        cursor.execute(
            '''DELETE account 
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
                '''UPDATE account
                SET account.balance = ?
                WHERE account.acc_id = ?''', self.balance, self.account_id)
            connection.commit()

    def deposit(self, value):
        print("before self.balance: " + str(self.balance))
        self.balance = int(self.balance) + int(value)
        print("deposit self.balance: " + str(self.balance)+"\n\n")
        cursor.execute(
            '''UPDATE account
            SET account.balance = ?
            WHERE account.acc_id = ?''', self.balance, self.account_id)
        connection.commit()

    def money_transfer(self, receiver, amount):
        new_balance = int(self.balance) - int(amount)
        # Exchange rate logic should be here
        # if(self.currency != receiver.currency):

        receiver_balance = receiver.balance + amount

        if(new_balance >= 0):
            self.update_balance(new_balance)
            cursor.execute(
                '''UPDATE account
                 SET account.balance = ?
                 WHERE account.acc_id = ?''', receiver_balance, receiver.account_id)
            connection.commit()

    def __str__(self):
        return f"----\n({self.account_id}  |  {self.currency}  | {self.balance})\n----"


class Customer:
    def __init__(self, customer_id):
        self.accounts = []
        self.transactions = []
        self.customer_id = customer_id
        cursor.execute(
            'SELECT * FROM customer WHERE customer.id = ?', customer_id)
        row = cursor.fetchone()
        if(not row):
            print("Customer not Found")
        else:
            self.first_name = row.firstN
            self.last_name = row.lastN
            self.email = row.email
            self.phone = row.phone
            self.TC = row.TC
            self.address = row.Adress

    def list_accounts(self):
        cursor.execute(
            '''SELECT a.acc_id, a.currency, a.balance 
            FROM account As a, userAccounts As u 
            WHERE u.acc_id = a.acc_id AND u.cus_id = ?''', self.customer_id)
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


# class Transactions:
#     def __init__(self, ob):
#         self.first_nametra = ob.trans_no
#         self.last_name = ob.trans_date
#         self.email = ob.src_id
#         self.phone = ob.rsv_id
#         self.TC = ob.trans_type
#         self.address = ob.Adress
