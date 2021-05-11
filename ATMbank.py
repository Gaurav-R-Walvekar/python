class Bankacconut():
    def __init__(self,name,balance,accno,bankname,pin):
        self.name=name
        self.balance=balance
        self.accno=accno
        self.bankname=bankname
        self.pin=pin
    def deposite(self):
        print("Enter the amount to deposite")
        deposite=int(input())
        self.balance+=deposite
        print("After deposite balance is:",self.balance)
    
    def withdraw(self):
        print("Enter amount to withdraw:")
        withdraw=int(input())
        print("Enter your pin:")                #accecpt the atm pin 
        no=int(input())
        if (no==self.pin):                      #check the pin
            self.balance-=withdraw
            print("{} was withdraw".format(withdraw))
            print("After withdraw balance is:",self.balance)
        else:
            print("Invalied Pin please try again")
        
    def details(self):
        print("Account name:",self.name)
        print("Account number:",self.accno)
        print("Bank name:",self.bankname)
        print("Balance:",self.balance)
    
def main():

    obj=Bankacconut(name='gaurav',balance=5000,accno=1009785,bankname='HDFC',pin=1234)
    no=1
    while no!=0:
        print("\nEnter your choice")
        print("1:Deposite")
        print("2:Credit")
        print("3:Details")
        print("0:exit")
        no=int(input())
        if no==1:
            obj.deposite()
        elif no==2:
            obj.withdraw()
        elif no==3:
            obj.details()
        else:
            no=0
            print("Thank you for using ATM")
            
if __name__=="__main__":
    main()