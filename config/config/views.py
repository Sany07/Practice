from django.shortcuts import render
from django.http import JsonResponse

def Home(request):
    return render(request, 'index.html')

def Data(request):

    pn=[
        {
        't':'1',
        't2':'2',
        't3':'3',
        },
        {
        't':'2',
        't2':'3',
        't3':'3',
        }
    ]
    data={
        'name':pn
    }
    
    print(data)
    return JsonResponse(data)