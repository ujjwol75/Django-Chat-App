from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import Message, Room
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {'username':username, 'room':room, 'room_details':room_details})

def checkView(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    message = Message.objects.create(value=message, username=username, room=room_id)
    message.save()
    return HttpResponse('Message sent successfully!')
