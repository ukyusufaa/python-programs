class BankAccount:

    def __init__(self, customer_name,account_number,balance,acc_type):

        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = balance
        self.acc_type = acc_type
    
    def display_details(self):
        print(self.customer_name)
        print(self.account_number)
        print(self.balance)
        print(self.acc_type)
    
    def deposit(self,amount):
        self.balance = self.balance + amount
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        else:
            self.balance = self.balance - amount

def search_account(accounts):
    found = False
    user_input = int(input("Enter account number:"))
    for account in accounts:
        if user_input != account.account_number:
            continue  
        else:
            found = True
            account.display_details()
            print("Account found")
            break
    if found == False:
        print("Nothing found")

accounts = []

account1 = BankAccount(
    "Ahmad",1005,250,"Current Account"
)
accounts.append(account1)

account2 = BankAccount(
    "Shazia",1006,340,"Savings Account"
)
accounts.append(account2)

account1.withdraw(25)
account2.deposit(50)

search_account(accounts)






