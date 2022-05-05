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

    def __str__(self):
        return f"----\n({self.account_id}, {self.currency},{self.balance})\n----"


class Customer:
    accounts = []
    transactions = []

    def __init__(self, customer_id):
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

    def update_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        cursor.execute(
            '''UPDATE customer
            SET customer.firstN = ?, , customer.lastN = ?
            WHERE customer.id = ?''', self.first_name, self.last_name, self.customer_id)

    def update_firstname(self, first_name):
        self.first_name = first_name
        cursor.execute(
            '''UPDATE customer
            SET customer.firstN = ?
            WHERE customer.id = ?''', self.first_name, self.customer_id)

    def update_lastname(self, last_name):
        self.last_name = last_name
        cursor.execute(
            '''UPDATE customer
            SET customer.lastN = ?
            WHERE customer.id = ?''', self.last_name, self.customer_id)

    def update_email(self, email):
        self.email = email
        cursor.execute(
            '''UPDATE customer
            SET customer.email = ?
            WHERE customer.id = ?''', self.email, self.customer_id)

    def update_phone(self, phone):
        self.phone = phone
        cursor.execute(
            '''UPDATE customer
            SET customer.phone = ?
            WHERE customer.id = ?''', self.phone, self.customer_id)

    def update_tc(self, tc):
        self.TC = tc
        cursor.execute(
            '''UPDATE customer
            SET customer.TC = ?
            WHERE customer.id = ?''', self.TC, self.customer_id)

    def update_address(self, address):
        self.address = address
        cursor.execute(
            '''UPDATE customer
            SET customer.Adress = ?
            WHERE customer.id = ?''', self.address, self.customer_id)

    def update_information(self, first_name, last_name, email, phone, tc, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.TC = tc
        self.address = address

    def update(self):
        cursor.execute(
            '''UPDATE customer
            SET customer.firstN = ? ,
            customer.lastN = ?,
            customer.email = ?,
            customer.phone = ?,
            customer.TC = ?,
            customer.Adress = ?
            WHERE customer.id = ?''', self.first_name, self.last_name, self.email, self.phone, self.TC, self.address, self.customer_id)
        connection.commit()

    def __str__(self):
        return f"----\n({self.customer_id}, {self.first_name},{self.last_name}, {self.email}, {self.phone}, {self.TC}, {self.address})\n---"
