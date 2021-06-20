class SavingsAccount:
    def __init__(self, annual_inter_rate, saving_balance):
        self.annual_inter_rate=annual_inter_rate
        self.saving_balance=saving_balance
        
    def MonthlyInterest(self):
        self.monthly_interest=(self.annual_inter_rate*self.saving_balance*0.01)/(12)
        self.saving_balance+=self.monthly_interest
        print("Monthly interest: ", self.monthly_interest)
        print("Saving balance: ",self.saving_balance)

    def modifyInterestRate(self,rate):
        self.annual_inter_rate=rate
    


r=int(input("Enter the rate: "))
p1=int(input("Enter the principal amount of saver 1: "))
p2=int(input("Enter the principal amount of saver 2: "))

saver1=SavingsAccount(r,p1)
saver2=SavingsAccount(r,p2)

saver1.MonthlyInterest()
saver2.MonthlyInterest()

saver1.modifyInterestRate(7)
saver2.modifyInterestRate(7)

saver1.MonthlyInterest()
saver2.MonthlyInterest()




