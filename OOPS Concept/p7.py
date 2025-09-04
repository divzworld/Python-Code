# Create a class `BankAccount` that uses **Encapsulation** to secure account balance and allow deposit/withdraw operations.
class BankAccount :
    def __init__(self, accBal) :
        self.__accBal = accBal

    @property  # Getter
    def deposit(self) :
        return self.__accBal
    
    # setter
    @deposit.setter
    def deposit(self, depAmt : float) -> None :
        
        if depAmt > 0 :
            self.__accBal += depAmt
            print(f"{depAmt} Deposited")
        else :
            print("Deposit Amount should be positive !")
        self.display()
    
    @property # Getter
    def withdraw(self) -> int:
        return self.__accBal
    
    # setter
    @withdraw.setter
    def withdraw(self, withAmt : float) -> None :
        
        if withAmt <= self.__accBal :
            self.__accBal -= withAmt
            print(f"{withAmt} Withdrawal")
        else :
            print(" Insufficient Account Balance ! So it is not possible to withdraw  money !")
        self.display()

    def display(self) -> None :
        print(f"Account Balance = {self.__accBal}")


obj = BankAccount(7000)

obj.deposit = 5000
obj.withdraw = 9000

obj.deposit = 50
obj.withdraw = 2000000