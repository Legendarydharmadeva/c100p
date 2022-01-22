class Atm(object):
    def __init__(self,name,cardnumber,pinnumber,balance):
        self.name=name
        self.cardnumber =  cardnumber
        self.pinnumber = pinnumber
        self.balance = balance

    def balanceInquiry(self):
        print('Your account balance is :' , self.balance)
    
    def withdraw(self,ammount):
        self.balance = self.balance - ammount
        print("Your remaining balance is :",self.balance)

    def deposition(self,amount2):
        self.balance = self.balance + amount2
        print("Your balance is :",self.balance)



tejasv = Atm(name='tejasv',cardnumber=5757557,pinnumber=122001,balance=1000000000000)

tejasv.balanceInquiry()
tejasv.withdraw(10000)
tejasv.deposition(100000)



