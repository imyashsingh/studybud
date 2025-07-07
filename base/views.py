from django.shortcuts import render


from .models import Room
from .forms import RoomForm 
# Create your views here.

#Home view to display all rooms
def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request, 'base/home.html',context)

#room views to dispaly selected room
def room(request,pk):
    room=Room.objects.get(id=pk)
    context={'room':room}
    return render(request, 'base/room.html',context)


#Create room view to create a new room
def createRoom(request):
    form=RoomForm()
    context={'form':form}
    return render(request,'base/room_form.html',context=context)
