from django.shortcuts import render

# Create your views here.

rooms=[
    {'id':1,'name':'Learn Python'},
    {'id':2,'name':'Learn Django'},
]


def home(request):
    context={'rooms':rooms}
    return render(request, 'base/home.html',context)


def room(request,pk):
    room=rooms[int(pk)-1]
    context={'room':room}
    return render(request, 'base/room.html',context)
