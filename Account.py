# Banking management system 
import pickle
import os
import json
import pathlib


class Account:

    file_name =[ file for file in os.listdir() if file.endswith('.json')]

    with open('{}'.format(max(file_name)),'rb') as json_file:
        obj=json.load(json_file)

    Account_No=obj['Account_Number']
    User_ID=obj['User_id']

    def __init__(self):
        self.email_id=''
        self.name=''
        self.password=''
        self.money=0
        Account.Account_No+=1
        self.acnt_no=Account.Account_No
        Account.User_ID+=100
        self.User_ID=Account.User_ID
        self.menu()

    @staticmethod
    def get_Account_no():
        return Account.Account_No
    
    @staticmethod
    def get_user_id():
        return Account.User_ID
    
    def menu(self):
        print("\t\t\t\t <--------------------MENU------------------->\t\t\t\t\n1. Create Account \n2. See Balance \n3. Withdraw Money \n4.Deposit \n5.Exit")
        self.action()

    def action(self):
        ch = int(input("Enter your choice (1/2/3/4/5) : "))
        if ch == 1:
            #create Account
            self.create_account()
        elif ch == 2:
            #See Balance 
            self.peek_balance()
        elif ch == 3:
            # Withdraw Money
            self.withdraw()
        elif ch == 4:
            # Deposit Money
            self.deposit()
        else:
            exit

    def create_account(self):
        self.name = input("Enter your name : ")
        self.email_id  = input("Enter email : ")
        self.password =input("Set Password : ") 
        self.money=float(input('HI! {} as you are a new user you need to deposit some money greater than 999 to create an account.').format(self.name))
        while self.money <= 999:
            print("\nPlease enter a valid amount")
            self.money=float(input('HI! {} as you are a new user you need to deposit some money greater than 999 to create an account.').format(self.name))
        action = 1 
        self.deposit(action)

            

            
    def deposit(self,action=2):
        if action == 1:
            print("Your current Account balance is {} ".format(self.money))
            self.menu()
        else :
            print("\t\t\t\t<---------------------- Deposit --------------------------->")
            deposit_money=float(input("Enter the amount you want to deposit: "))
            self.money+=deposit_money
            print("Your current Account balance is {} ".format(self.money))
            self.menu()


    def peek_balance(self):

        ch =input("Enter your user_name: ")

        if ch == self.name:
            print('Your account balance {}'.format(self.money))
            self.menu()
        else:
            print('NIKAL LAUDE PEHLI FURSAT MEIN NIKAL')
            self.menu()

    def withdraw(self):

        ch = input('Enter your username: ')
        if ch == self.name:
            honey_my_money = float(input("Enter money to withdraw: "))
            if honey_my_money > self.money :
                print("TERI MAA KI CHUT TERI GANDU MASTI KARTA HAI")
                self.menu()
            else :
                self.money-=honey_my_money
                print('Your account balance {}'.format(self.money))
                self.menu()
        else: 
            print('NIKAL LAUDE PEHLI FURSAT MEIN NIKAL')
            self.menu()



        


        


