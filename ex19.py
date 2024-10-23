class BankAccount:
    def __init__(self, accountNumber,  balance, password):
        self.accountNumber = accountNumber
        self._balance = balance
        self.__password = password

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance can not be negative!")
        self.balance = new_balance

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, new_password):
        if len(new_password) < 3:
            raise ValueError("must be more than 3 charecters")
        self.__password = new_password
    
class SavingsAccount(BankAccount):
    def __init__(self, accountNumber, balance, password):
        super().__init__(accountNumber, balance, password)

    def show_info(self):

        try:
            print(self._balance) #protected, accessible within subclass 
            print(self.__password) # Private, not accessible
        
        except Exception as e:
            print(f"access error {e}")
        
        #using setter and getter to show balace or password
        print(self.balance)
        print(self.password)

a1 = BankAccount("1234", 2000, "mahshad21")
print(a1.balance)
print(a1.password)
a1.password = "mehdi20"
print(a1.password)

"""_balance is protected, meaning it can be accessed directly
within the subclass but should generally be accessed via getter/setter methods"""

"""__password is private and cannot be accessed directly from SavingsAccount.
 Attempting to do so will raise an AttributeError"""


