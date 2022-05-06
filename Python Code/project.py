# from SQLconnection import cursor
from classes import Account, Customer


customerId = input("Insert Customer Id: ")

currentCustomer = Customer(customerId)

print(currentCustomer)

currentCustomer.update_information(
    "Mohamed", "Hosam", "email@google.com", "556 588 89 56", "99886555478", "Delete My Adress")


print(currentCustomer)
currentCustomer.update()
c1 = Customer(customerId)
print(c1)

# cursor.execute(
#     '''SELECT DISTINCT t.trans_no, t.trans_date, t.src_id, t.rsv_id, t.trans_type, t.total, t.cus_id
# FROM customer c, transactions t, account a, userAccounts ua
# WHERE c.id = ua.cus_id and
# 	ua.acc_id = a.acc_id and
# 	(t.src_id = a.acc_id OR t.cus_id = c.id) and
# 	c.id = ?
# ORDER BY(t.trans_date)''', customerId)
# rowss = cursor.fetchall()
# print(rowss)


# print(currentCustomer)
# print(currentCustomer.list_accounts()[0])
# print(currentCustomer.list_transactions())


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

    # if balance - amount is negative (Can't Withdraw)
    # Else: Change the database balance into the new value
    # Message Withdraw completed
    print("Withdraw Completed")


# ATM_operations("Withdraw")


def open_account():
    # list all accounts that belong to the user ---(Query)
    # Insert A row in the account table with the new account ---(Query)
    # Message Request has been made for your new account
    Currency = input("Currency: ")


def delete_account():
    # list all accounts that belong to the user ---(Query)
    # Get the balance of the selected account    --(Query)
    # If the balance not 0 CAn not be deleted
    # Else: Message Request has been sent for deleting (Clerk)
    account_no = input("Account No: ")


def update_information():
    # list all information that belong to the user ---(Query)
    # Option to Edit all the information ---(Interface)
    # Submit a request to the clerk
    # Message Request has been sent for Updating (Clerk)
    edit = input("All can be edited: ")


def money_transfer():
    # list all accounts that belong to the user ---(Query)
    # account_no = input("Select an account to transfer from: ")
    # recieve_account = input("Select an account to transfer to: ")
    # Select the accounts from database
    # Depending on exchange rate, calculations will be occur
    # Change the balance of the selected account
    # Message Money has been transferred
    account_no = input("Select an account to transfer from: ")


def monthly_summery():
    # Filter all transactions of that user -order by date-  ---(Query)
    # list them on the Screen
    # Consider the loans in a separate section
    total_transaction = 0


def exchange_rate_panel():
    # Select all currencies with their exchange rate  ---(Query) Currency Table
    # list them on the Screen
    # Consider the loans in a separate section
    total_currencies = 0


def list_accounts():
    # Select all corresponding accounts to the selected user ---(Query) account Table
    # list them on the Screen
    total_accounts = 0


def bankGeneralStatus():
    # -income-  select total money that has been deposited into the bank (paying loan included)
    # -expenses- select both withdraw and loan money ----(Sum Query)
    # -Profit-  select total profit out from loans
    # -total balance- Sum of the balance of all accounts
    # Message all info to the Manager Screen
    income = 0


def addNewCurrency():
    currency = input("insert new currency: ")
    # select all currencies out of currency table for comparing
    # if the new currency already exists don't add message User
    # else add to the currency table
    # Message Success or Failure
    currencyValue = input("insert the currency value: ")


def updateCurrency():
    currency = input("insert the currency")
    # select all currencies out of currency table for comparing
    # if the currency exists
    # else ask for redirection to add new currency
    # Message Success or redirection
    currencyValue = input("insert the currency value: ")


def updateEmployeeSalary():
    # Update the clerk table with the new Salary
    # Message Success for Manager screen
    newSalary = input("insert new salary")


def updateInterestRate():
    # Update the Interest Rate with the new Data
    # Message Success for Manager screen
    interest = input("insert new interest Rate: ")


def addNewCustomers():
    # Select the all new customers from ---(Query) new Customer Table
    # For Every Customer move it to the customers table and assign a clerk for him
    # -Assigning clerk- it is assigned to the clerk with the least number of customers.
    # append the customer id to the responsible clerk ----(Clerk Table)
    newCustomers = 0


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
