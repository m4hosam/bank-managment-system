from classes import Customer


def ATM_operations(type):
    # list all accounts that belong to the user ---(Query)
    amount = input("Amount: ")
    account_no = input("Account Number: ")
    # Currency Selection list interface
    # Select that account from database and get the balance ---(Query)
    # Type is either Withdraw or Deposit
    # if balance - amount is negative (Can't Withdraw)
    # Else: Change the database balance into the new value
    # Message Withdraw completed


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






print("1-Withdraw\n"
      "2-Deposit\n"
      "3-Open account\n"
      "4-Delete account\n"
      "5-Update My Information\n"
      "6-Money Transfer\n"
      "7-Pay loan\n"
      "8-request loan\n"
      "9-Monthly Summery\n"
      "10-Excange Rate Panel\n"
      "11-My Accounts\n")
