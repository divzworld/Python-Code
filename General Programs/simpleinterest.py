# Write a program to calculate the simple interest: 
class SimpleInterest :
    def ___init___( self ) :
        self.principal = None
        self.rate = None
        self.timee = None
        self.SI = None

    def principalAmt(self) :
        try :
            self.principal = float(input(" Enter principal amount : "))
            if self.principal <= 0 :
                self.principalAmt()
        except :
            print(" Please Enter Numeric Value ! ")
            self.principalAmt()

    def rateAmt(self) :
        try :
            self.rate = float(input(" Enter rate amount : "))
            if self.rate <= 0 :
                self.rateAmt()
        except :
            print(" Please Enter Numeric Value ! ")
            self.rateAmt()

    def time(self) :
        try :
            self.timee = float(input(" Enter time : "))
            if self.timee <= 0 :
                self.time()
        except :
            print(" Please Enter Numeric Value ! ")
            self.time()

    def calculation(self) :
        self.principalAmt()
        self.rateAmt()
        self.time()
        self.SI = ( self.principal * self.rate * self.timee ) / 100
        return self.SI

si = SimpleInterest()
si.calculation()
print(si.SI)
print(f"Principal Amount : {si.principal} , Rate : {si.rate}% , Time : {si.timee} So Simple Interest : {si.SI:.2f}")






