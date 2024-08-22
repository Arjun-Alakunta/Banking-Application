import random

details=[]

class BankDetails:
    def accountDetails(name):
        for data in details:
            if data['name']==name:
                print("Name :",data['name'])
                print("Account Number :",data['AccountNumber'])
                print("Balance :",data['balance'])
                print("Mobile No:",data['mb_no'])
                print("Account Type:",data['accountType'])
                return
        print("Invalid Name")
        return

    def balanceEnquiery(AccountNumber):
        for data in details:
            if data['AccountNumber']==AccountNumber:
                currBalance=data['balance']
                print("Your Balance is ",currBalance)
                return
            print("Not a Valid Account Number")
        return

    def deposit(AccountNumber,amount):
        for data in details:
            if data['AccountNumber']==AccountNumber:
                data['balance']+=amount
                print("Your Balance after Depositing",amount,"is ",data['balance'])
                return
            print("Invalid Account")
        return


    def withdraw(AccountNumber,amount):
        for data in details:
            if data['AccountNumber']==AccountNumber:
                if amount>data['balance']:
                    print("Not Suffiecient Funds in Your Account")
                    return
                data['balance']-=amount
                print("Your Balance after Withdrawing ",amount,"is ",data['balance'])
        return

    def newAccount():
        name=input("Enter The Account Holder Name :")
        AccountNumber=random.randint(100000,999999)
        balance=random.randrange(10,99999)
        mb_no=int(input("Enter 10 digit Mobile number :"))
        accountType=input("Savings or Current :")

        details.append({'name':name,'AccountNumber':AccountNumber,'balance':balance,'mb_no':mb_no,'accountType':accountType})
        return

if __name__=='__main__':
    
    while True:
        print()
        print()
        print("Enter 1 for Account Details")
        print("Enter 2 for Balance Enquiery")
        print("Enter 3 for Deposit")
        print("Enter 4 for Withdraw")
        print("Enter 5 for Opening New Account")
        print("Enter 6 for Exiting")

        choice=int(input("Enter Your Choice : "))
        if (choice>=1 and choice<=6):
            if choice==1:
                name=input("Enter your Name: ")
                for data in details:
                    if data['name']==name:
                        BankDetails.accountDetails(name)

            elif choice==2:
                AccountNumber=int(input("Enter your Account Number: "))
                for data in details:
                    if data['AccountNumber']==AccountNumber:
                        BankDetails.balanceEnquiery(AccountNumber)


            elif choice==3:
                AccountNumber=int(input("Enter your Account Number: "))
                for data in details:
                    if data['AccountNumber']==AccountNumber:
                        amount=float(input("Enter The Amount to Deposit :"))
                        BankDetails.deposit(AccountNumber,amount)
    

            elif choice==4:
                AccountNumber=int(input("Enter your Account Number: "))
                for data in details:
                    if data['AccountNumber']==AccountNumber:
                        amount=float(input("Enter The Amount to WithDraw :"))
                        BankDetails.withdraw(AccountNumber,amount)
                    
            elif choice==5:
                BankDetails.newAccount()
                print(details)

            elif choice==6:
                print("\t\t\tThank You")
                break
        else:
            print("\t\t\tEnter Valid Input ")
