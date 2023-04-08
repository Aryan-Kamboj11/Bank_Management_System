import os
import pathlib
import json



ch = input("Enter your account number : ")

file_name=[file for file in os.listdir() if file.endswith('.json') and file.startswith(ch)]

with open('{}'.format(file_name[0]),'r') as read_json:
    obj = json.load(read_json)
    password = input("Enter yout password:")
    if password == obj['Password']:
        print('<---------------------------{}---------------------->'.format(obj['Name']))
        print("User ID : ",obj['User_id'])
        print("Account Number : ",obj['Account_Number'])
        print("Email : ",obj["Email"])
        print("Deposit Money : ",obj["Savings"])
