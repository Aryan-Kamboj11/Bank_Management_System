import Account as Account
import json
import pickle


def open_file():
    with open('Pickle_file.dat','rb') as unpickle_file:
        while True: 
            try:
                obj=pickle.load(unpickle_file)
                dict1={
                    'Account_Number':obj.acnt_no,
                    'User_id':obj.User_ID,
                    'Name':obj.name,
                    'Email':obj.email_id,
                    'Password':obj.password,
                    'Savings':obj.money
                }
                print(Account.Account.get_Account_no())
                print(Account.Account.get_user_id())
                with open('{}.json'.format(obj.acnt_no),'a') as json_file:
                    json.dump(dict1,json_file,indent=4) 
            except EOFError:
                print("Done!")
                break




