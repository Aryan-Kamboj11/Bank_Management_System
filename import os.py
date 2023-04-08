import os
import pathlib
import json

file_name =[ file for file in os.listdir() if file.endswith('.json')]

with open('{}'.format(max(file_name)),'r') as json_file:
    obj=json.load(json_file)
print(type(obj['User_id']))