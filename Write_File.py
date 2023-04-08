import Account as Account
import json
import pickle
import Unpickle 
from Unpickle import open_file 

def make_obj():
    with open('Pickle_file.dat','wb') as pickle_file:
        obj = Account.Account()
        pickle.dump(obj,pickle_file)

