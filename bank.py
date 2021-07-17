class money:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def checkbalance(self):
        print("Your balance is 10000")
    def withdrawal(self, amount):
        newamount = 10000 - amount
        print("You have withdrawn:" + str(amount) + " Your remaining balance is:" + str(newamount))
    
def main():
    card_number = input("Enter your card number:")
    pin_number = input("Enter your pin number:")
    new_user = money (card_number, pin_number)
    print ("Choose your activity: 1. Balance Inquiry 2. Withdrawal")
    activity = int(input("Enter the activity number:"))
    if (activity ==1):
        new_user.checkbalance()
    elif (activity ==2):
        amount = int(input("Enter the amount:"))
        new_user.withdrawal(amount)
    else:
        print("Invalid Choice")
if __name__ =="__main__":
    main()