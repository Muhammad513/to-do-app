from django.shortcuts import render
from django.http import HttpResponse
import json

def add(request):
    file_name='db.json'
    capital={"davlatlar":[]}
    davlat=request.GET.get('dav')
    poytaxt=request.GET.get('poy')
    new={davlat:poytaxt}
    capital['davlatlar'].append(new)
    with open(file_name,'a') as file:
        capital=capital['davlatlar']
        json.dump(capital,file)
    return HttpResponse(f'{capital}')
def remove(request):
    return HttpResponse('3')    


def index(request):
    
    return HttpResponse('4')        