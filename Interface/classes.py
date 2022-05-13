from numpy import arctanh
from SQLconnection import cursor, connection
import datetime


def getCurrencies():
    currencies = []
    cursor.execute(
        '''SELECT * FROM currency''')
    rows = cursor.fetchall()
    for row in rows:
        currencies.append(row.curr_code)
    return currencies


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


def req_open(currency, cus_id):
    cursor.execute(
        '''INSERT INTO account2 
        VALUES( ?, 0)
        ''', currency)
    cursor.execute(
        '''INSERT INTO accountStatus2
        VALUES('R-OPEN')
        ''')
    connection.commit()
    cursor.execute(
        '''SELECT MAX(acc_id) AS LastID FROM account2''')
    acc_row = cursor.fetchone()
    cursor.execute(
        '''INSERT INTO userAccounts2
        VALUES(?,?)
        ''', acc_row.LastID, cus_id)
    connection.commit()


def get_salary():
    cursor.execute("SELECT val FROM Salary")
    salary = cursor.fetchone()
    return salary.val


def set_salary(new_salary):
    if(new_salary > 0):
        cursor.execute(
            '''UPDATE Salary SET val = ?''', new_salary)
        connection.commit()


def add_customer(fn, ln, e, p, tc, ad):
    cursor.execute(
        '''INSERT INTO customer2 
        VALUES(?, ?, ?, ?, ?, ?)''', fn, ln, e, p, tc, ad)

    connection.commit()
    cursor.execute(
        '''INSERT INTO customerStatus2
        VALUES('ACTIVE')''')

    cursor.execute(
        '''SELECT MAX(id) AS LastID FROM customer2''')
    cus_row = cursor.fetchone()
    # print(cus_row.LastID)
    cursor.execute(
        '''SELECT clerk_id, COUNT(clerk_id) AS r_cus
        FROM customerClerks2
        GROUP BY clerk_id
        ORDER BY r_cus''')
    first_row = cursor.fetchone()
    # print(first_row.clerk_id)
    cursor.execute(
        '''INSERT INTO customerClerks2
        VALUES(?, ?)''', cus_row.LastID, first_row.clerk_id)
    connection.commit()


def add_currency(cur, rate):
    cursor.execute(
        '''INSERT INTO currency 
        VALUES(?, ?)''', cur, rate)
    connection.commit()


def add_currency(cur, rate):
    cursor.execute(
        '''UPDATE currency 
        SET exch_rate = ?
        WHERE curr_code = ?''', rate, cur)
    connection.commit()


class Account:
    def __init__(self, account):
        self.account_id = account.acc_id
        self.currency = account.currency
        self.balance = account.balance

    def save(self):
        cursor.execute(
            '''UPDATE accountStatus2 
            SET accountStatus2.acc_status = 'ACTIVE'
            WHERE accountStatus2.acc_id = ?
            ''', self.account_id)
        connection.commit()

    def delete(self):
        cursor.execute(
            '''UPDATE accountStatus2 
            SET accountStatus2.acc_status = 'DELETED'
            WHERE accountStatus2.acc_id = ?
            ''', self.account_id)
        connection.commit()

    def req_delete(self):
        cursor.execute(
            '''UPDATE accountStatus2 
            SET accountStatus2.acc_status = 'R-DELETED'
            WHERE accountStatus2.acc_id = ?
            ''', self.account_id)
        connection.commit()

    def get_balence(self):
        return self.balance

    def get_currency(self):
        return self.currency

    def withdraw(self, value):
        self.balance = int(self.balance) - int(value)
        if(self.balance >= 0):
            cursor.execute(
                '''UPDATE account2
                SET account2.balance = ?
                WHERE account2.acc_id = ?''', self.balance, self.account_id)
            t = datetime.datetime.now()
            cursor.execute(
                '''INSERT INTO transactions2 
                VALUES( ? ,?,NULL,'withdraw',?, ?, NULL)
                ''', t, self.account_id, value, self.balance)
            connection.commit()

    def deposit(self, value):
        self.balance = int(self.balance) + int(value)
        cursor.execute(
            '''UPDATE account2
            SET account2.balance = ?
            WHERE account2.acc_id = ?''', self.balance, self.account_id)
        t = datetime.datetime.now()
        cursor.execute(
            '''INSERT INTO transactions2 
            VALUES( ? ,NULL,?,'deposit',?, NULL, ?)
            ''', t, self.account_id, value, self.balance)
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
                VALUES( ? ,?,?,'money transfer',?, ?, ?)
                ''', t, self.account_id, receiver.account_id, amount, new_balance1, new_balance2)
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
            '''SELECT customer2.* FROM customer2, customerStatus2 
            WHERE customerStatus2.cus_id = customer2.id and
            customer2.id = ? and
            customerStatus2.cus_status = 'ACTIVE' ''', customer_id)
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
            WHERE u.acc_id = a.acc_id AND u.cus_id = ? ''', self.customer_id)
        rows = cursor.fetchall()
        for row in rows:
            self.accounts.append(Account(row))
        return self.accounts

    def list_transactions(self):
        cursor.execute(
            '''SELECT DISTINCT t.trans_no, t.trans_date, t.src_id, t.rsv_id, t.trans_type, t.total
            FROM customer2 c, transactions2 t, account2 a, userAccounts2 ua
            WHERE c.id = ua.cus_id and
            ua.acc_id = a.acc_id and
            (t.src_id = a.acc_id or t.rsv_id = a.acc_id)  and
            c.id = ?
            ORDER BY(t.trans_date) DESC
            ''', self.customer_id)
        rows = cursor.fetchall()
        # print(rows)
        for row in rows:
            self.transactions.append(Transaction(row, self.customer_id))
        return self.transactions

    def to_array(self):
        arr = []
        arr.append(self.customer_id)
        arr.append(self.first_name)
        arr.append(self.last_name)
        arr.append(self.email)
        arr.append(self.phone)
        arr.append(self.TC)
        arr.append(self.address)
        return arr

    def update(self, first_name, last_name, email, phone, tc, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.TC = tc
        self.address = address
        cursor.execute(
            '''UPDATE customer2
            SET customer2.firstN = ? ,
            customer2.lastN = ?,
            customer2.email = ?,
            customer2.phone = ?,
            customer2.TC = ?,
            customer2.Adress = ?
            WHERE customer2.id = ?
            ''', self.first_name, self.last_name, self.email, self.phone, self.TC, self.address, self.customer_id)
        connection.commit()

    # The next function should be edited in clerk (update)

    def __str__(self):
        return f"----\n({self.customer_id}, {self.first_name},{self.last_name}, {self.email}, {self.phone}, {self.TC}, {self.address})\n---"


class Transaction:
    def __init__(self, ob, cus_id):
        self.trans_no = ob.trans_no
        self.trans_date = ob.trans_date
        self.src_id = ob.src_id
        self.rsv_id = ob.rsv_id
        self.trans_type = ob.trans_type
        self.total = ob.total
        self.cus_id = cus_id
        self.arr = []

    def toArray(self):
        self.arr.append(self.trans_no)
        self.arr.append(str(self.trans_date))

        if(self.trans_type == "deposit"):
            src = f"customer {self.cus_id}"
            self.arr.append(src)
            self.arr.append(self.rsv_id)
        elif(self.trans_type == "withdraw"):
            rsv = f"customer {self.cus_id}"
            self.arr.append(self.src_id)
            self.arr.append(rsv)
        elif(self.trans_type == "money transfer"):
            self.arr.append(self.src_id)
            self.arr.append(self.rsv_id)
        # last one is the bank loan

        self.arr.append(self.trans_type)
        self.arr.append(self.total)
        return self.arr

    def __str__(self):
        return f"----\n({self.trans_no}, {self.trans_date},{ self.src_id}, {self.rsv_id}, {self.trans_type}, {self.total})\n---"


class Clerk:
    def __init__(self, clerk_id):
        self.customers = []
        self.transactions = []
        self.clerk_id = clerk_id

        cursor.execute(
            '''SELECT c.*
            FROM customer2 c, customerStatus2 cs , customerClerks2 cc
            WHERE cs.cus_id = cc.cus_id and
            cc.clerk_id = ? and
            c.id = cs.cus_id and 
            cus_status = 'ACTIVE' ''', self.clerk_id)
        rows = cursor.fetchall()
        if(not rows):
            print("Clerk not Found Class Related")
        else:
            for row in rows:
                self.customers.append(str(row.id))

    def list_transactions(self, cus_id):
        cursor.execute(
            '''
            SELECT DISTINCT tr.*,  ua1.cus_id src_cus, ua2.cus_id rsv_cus
            FROM transactions2 tr
            LEFT JOIN account2 a1
            ON tr.src_id = a1.acc_id
            LEFT JOIN account2 a2
            ON tr.rsv_id = a2.acc_id
            LEFT JOIN userAccounts2 ua1
            ON ua1.acc_id = src_id
            LEFT JOIN userAccounts2 ua2
            ON ua2.acc_id = rsv_id
            WHERE ua1.cus_id = ? or ua2.cus_id =?
            ''', cus_id, cus_id)
        rows = cursor.fetchall()
        for row in rows:
            self.transactions.append(self.to_array(row))
        return self.transactions

    def list_customer(self):
        ar = []
        for c in self.customers:
            ar.append(Customer(c))
        return ar

    # def list_expenses(self):
    #     cursor.execute(
    #         '''

    #         ''', cus_id, cus_id)
    #     rows = cursor.fetchall()
    #     for row in rows:
    #         self.transactions.append(self.to_array(row))

    def to_array(self, row):
        arr = []
        arr.append(str(row.trans_date))
        # source customer
        if(row.trans_type == "deposit"):
            src = f"customer"
            arr.append(src)
            arr.append(row.rsv_cus)
            arr.append(src)
            arr.append(row.rsv_id)
        elif(row.trans_type == "withdraw"):
            rsv = f"customer"
            arr.append(row.src_cus)
            arr.append(rsv)
            arr.append(row.src_id)
            arr.append(rsv)
        elif(row.trans_type == "money transfer"):
            arr.append(row.src_cus)
            arr.append(row.rsv_cus)
            arr.append(row.src_id)
            arr.append(row.rsv_id)

        arr.append(row.trans_type)
        arr.append(row.total)
        arr.append(row.src_balance)
        arr.append(row.rsv_balance)
        return arr


c = Clerk(2)
print(c.customers)
print(c.list_customer()[0].first_name)
# print(c.list_transactions(301))
