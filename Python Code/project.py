from SQLconnection import cursor
from classes import Account, Customer


customerId = input("Insert Customer Id: ")
cursor.execute('SELECT * FROM customer WHERE customer.id = ?', customerId)
rows = cursor.fetchall()

if(not rows):
    print("Customer not Found")
else:
    currentCustomer = Customer(rows[0])


cursor.execute(
    '''SELECT DISTINCT t.trans_no, t.trans_date, t.src_id, t.rsv_id, t.trans_type, t.total, t.cus_id
FROM customer c, transactions t, account a, userAccounts ua
WHERE c.id = ua.cus_id and
	ua.acc_id = a.acc_id and
	(t.src_id = a.acc_id OR t.cus_id = c.id) and
	c.id = ?
ORDER BY(t.trans_date)''', customerId)
rowss = cursor.fetchall()
print(rowss)


print(currentCustomer)
print(currentCustomer.list_accounts()[0])
print(currentCustomer.list_transactions())


def ATM_operations(type):
    # list all accounts that belong to the user ---(Query)
    cursor.execute('SELECT account.acc_id, account.currency, account.balance FROM account, userAccounts WHERE userAccounts.acc_id = account.acc_id AND userAccounts.cus_id = ?', customerId)
    rows = cursor.fetchall()
    accounts = []
    accountIds = []

    for row in rows:
        print(row)
        accounts.append(Account(row))
        accountIds.append(row.acc_id)

    account_no = input("Account Number: ")
    # Type is either Withdraw or Deposit
    if(type == "Withdraw"):
        amount = input("Withdraw amount: ")
    elif(type == "Deposit"):
        amount = input("Deposit amount: ")

    # Currency Selection list interface
    # Select that account from database and get the balance ---(Query)
    print(accountIds)
    if int(account_no) in accountIds:
        print("Exists")
    else:
        print("Invaild input")

    if(int(amount) < 0):
        print("Error Can't Withdraw negative")
    # else:
        # cursor.execute('Update', account_no, )

    print("Withdraw Completed")
    # if balance - amount is negative (Can't Withdraw)
    # Else: Change the database balance into the new value
    # Message Withdraw completed


# ATM_operations("Withdraw")


def open_account():
    # list all accounts that belong to the user ---(Query)
    Currency = input("Currency: ")
    # Insert A row in the account table with the new account ---(Query)
    # Message Request has been made for your new account


def delete_account():
    # list all accounts that belong to the user ---(Query)
    account_no = input("Account No: ")
    # Get the balance of the selected account    --(Query)
    # If the balance not 0 CAn not be deleted
    # Else: Message Request has been sent for deleting (Clerk)


def update_information():
    # list all information that belong to the user ---(Query)
    # Option to Edit all the information ---(Interface)
    edit = input("All can be edited: ")
    # Submit a request to the clerk
    # Message Request has been sent for Updating (Clerk)


def money_transfer():
    # list all accounts that belong to the user ---(Query)
    # Option to Edit all the information ---(Interface)
    account_no = input("Select an account to transfer from: ")
    recieve_account = input("Select an account to transfer to: ")
    # Select the accounts from database
    # Depending on exchange rate, calculations will be occur
    # Change the balance of the selected account
    # Message Money has been transferred


def monthly_summery():
    # Filter all transactions of that user -order by date-  ---(Query)
    total_transaction = 0
    # list them on the Screen
    # Consider the loans in a separate section


def exchange_rate_panel():
    # Select all currencies with their exchange rate  ---(Query) Currency Table
    total_currencies = 0
    # list them on the Screen
    # Consider the loans in a separate section


def list_accounts():
    # Select all corresponding accounts to the selected user ---(Query) account Table
    total_accounts = 0
    # list them on the Screen


def bankGeneralStatus():
    income = 0
    # -income-  select total money that has been deposited into the bank (paying loan included)
    # -expenses- select both withdraw and loan money ----(Sum Query)
    # -Profit-  select total profit out from loans
    # -total balance- Sum of the balance of all accounts
    # Message all info to the Manager Screen


def addNewCurrency():
    currency = input("insert new currency: ")
    # select all currencies out of currency table for comparing
    # if the new currency already exists don't add message User
    # else add to the currency table
    currencyValue = input("insert the currency value: ")
    # Message Success or Failure


def updateCurrency():
    currency = input("insert the currency")
    # select all currencies out of currency table for comparing
    # if the currency exists
    currencyValue = input("insert the currency value: ")
    # else ask for redirection to add new currency
    # Message Success or redirection


def updateEmployeeSalary():
    newSalary = input("insert new salary")
    # Update the clerk table with the new Salary
    # Message Success for Manager screen


def updateInterestRate():
    interest = input("insert new interest Rate: ")
    # Update the Interest Rate with the new Data
    # Message Success for Manager screen


def addNewCustomers():
    newCustomers = 0
    # Select the all new customers from ---(Query) new Customer Table
    # For Every Customer move it to the customers table and assign a clerk for him
    # -Assigning clerk- it is assigned to the clerk with the least number of customers.
    # append the customer id to the responsible clerk ----(Clerk Table)


# print("1-Withdraw\n"
#       "2-Deposit\n"
#       "3-Open account\n"
#       "4-Delete account\n"
#       "5-Update My Information\n"
#       "6-Money Transfer\n"
#       "7-Pay loan\n"
#       "8-request loan\n"
#       "9-Monthly Summery\n"
#       "10-Exchange Rate Panel\n"
#       "11-My Accounts\n")

# print("1-income-expense-profit-total balance\n"
#       "2-add new currency\n"
#       "3-update currency\n"
#       "4-Update the salary of the clerks\n"
#       "5-Update interest Rate\n"
#       "6-Add new Customers\n"
#       "7-Advance one Month---As a result of this progress -> salaries should be paid,"
#       " income-expenditure statuses should be updated and customers'"
#       " debts for the next month should be reflected to them.\n"
#       "8-view all transactions (How many??)\n")
