import json


with open('db.json',"r") as file:
    data=json.load(file)
    KEY="Germaniya"
    data=data['davlatlar']
    


    for i in data:
        if i.get(KEY)!=None:
            del i[KEY]
            
print(data)            
