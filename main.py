class BankAccount():
    defaultAccountNumber = 1  # class attribute

    def __init__(self, name, Balance=0):
        self.name = name
        self.Balance = Balance
        self.bank = 'SBI'
        self.branchName = 'Adambakkam'
        self.accountNumber = BankAccount.defaultAccountNumber
        BankAccount.defaultAccountNumber = BankAccount.defaultAccountNumber, 'SBI00', + 1

    def deposit(self, amount):
        self.Balance += amount

    def withdraw(self, amount):
        if self.Balance < amount:
            print("Not Enough Money")
        else:
            self.Balance -= amount
            return f'Dear {self.name}! your withdrawl amount is {amount}\n Your remaining balance is {self.Balance}' \
                   f'\nThank you for using "{self.bank} {self.branchName}" branch.'

    def getBalance(self):
        return f'Dear {self.name}! your balance amount is' + ' ' + str(self.Balance) + ' ' + 'rupees.'


if __name__ == '__main__':
    myObj = BankAccount('George', 1000)
    myObj.deposit(1000)
    print(myObj.getBalance())
    print(myObj.withdraw(500))
