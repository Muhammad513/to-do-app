from django.shortcuts import render
from django.http import HttpResponse
import json

def add(request):
    src1=request.GET.get('name')
    src2=request.GET.get('capital')
    src3={src1:src2}
    file_name='db.json'
    with open(file_name,"r") as file:
        data=json.load(file)
        data["davlatlar"].append(src3)
    
    with open(file_name,'w') as file:
        json.dump(data,file,indent=4)

    return HttpResponse(f'{data}')




def remove(request):
    DELETE=request.GET.get("key")
    file_name="db.json"
    with open(file_name,"r") as file:
        data=json.load(file)
        KEY=DELETE
        data1=data['davlatlar']
        for i in data1:
            if i.get(KEY)!=None:
                del i[KEY]
        
    with open(file_name,'w') as file:
        json.dump(data,file,indent=4)

    return HttpResponse(f'delete {KEY}')
    

def index(request):
    file_name="db.json"
    with open(file_name,"r") as file:
        data=json.load(file)
    return HttpResponse(f'<h1>Davlat Poytaxtlari</h1><br> {data}')        