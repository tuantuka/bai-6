class Bank:
    Account_type = "Savings"
    location = "Guntur"
    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = Bank.Account_type
        self.location = Bank.location

    def __repr__(self):
        print("Wellcome to the SBI ATM Machine")
        account_pin = int(input("Nhập mật khẩu của bạn: "))
        if account_pin == 123:
            Account(self)
        else:
            print("Mật khẩu không đúng! Mời nhập lại")
            Error(self)
        return ' '.join([self.name, self.Account_Number])

def Error(self):
    account_pin = int(input("Nhập mật khẩu của bạn: "))
    if account_pin == 123:
        Account(self)
    else:
        print("Mật khẩu không đúng! Mời nhập lại")
        Error(self)

def Account(self):
    print("Số thẻ của bạn là: XXXX XXXX XXXX 1337")
    print("Bạn có thể chọn các chức năng sau đây: Balance/ Withdraw/ Disposit/ Quit?")
    print("""
        1)  Balance
        2)  Withdraw
        3)  Deposit
        4)  Quit
        """)
    option = int(input("Sự lựa chọn của bạn là: "))
    if option == 1:
        Balance(self)
    elif option == 2:
        Withdraw(self)
    elif option == 3:
        Deposit(self)
    elif option == 4:
        exit()

def Balance(self):
    print("Balance: ", self.balance)
    Account(self)

def Withdraw(self):
    w = int(input("Nhập số tiền mong muốn: "))
    if self.balance > 0 and self.balance >= w:
        self.balance -= w
        print("Giao dịch thành công")
        print("Số dư hiện của bạn là: ", self.balance)
    else:
        print("Giao dịch bị hủy")
        print("Số tiền trong tài khoản của bạn không đủ")
    Account(self)

def Deposit(self):
    d = int(input("Nhập mong muốn của bạn: "))
    self.balance += d
    print("Giao dịch thành công")
    print("Số dư hiện tại của bạn là: ", self.balance)
    Account(self)

def Exit(self):
    print("Thoát")

t1 = Bank('Nam', 1453210145, 5000)
print(t1)