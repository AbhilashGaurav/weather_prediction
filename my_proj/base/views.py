from django.shortcuts import render, redirect
from django.contrib import messages 
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RoomForm
# Create your views here.
from .models import Room, Topic
# rooms = [
#     {'id': 1, 'name': '1 oop data'},
#     {'id': 2, 'name': '2 data'},
#     {'id': 3, 'name': '3 data'},
#     {'id': 4, 'name': '4 data'}
# ]


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid username or password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password does not exist')
    context = {'page': page}
    return render(request,"base/login_page.html",context)

def  logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    return render(request,"base/login_page.html",)
def home(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains= q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
        )
    topics = Topic.objects.all()
    rooms_count = rooms.count()
    context = {'rooms': rooms, 'topics': topics, 'room_count': rooms_count} 
    return render(request, 'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    # room =None
    # for i in rooms:
    #     if i['id'] ==int(pk):
    #         room =i
    context = {'room':room}
    return render(request, 'base/room.html',context)
# create a new room 
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request,"base/room_form.html",context)

# update the authorized room
@login_required(login_url='login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user !=room.host:
        return HttpResponse('You are not allowed here!!!')
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request,"base/room_form.html",context)


# delete an authorized room
@login_required(login_url='login')
def delete_room(request,pk):
    room = Room.objects.get(id=pk)
    if request.user !=room.host:
        return HttpResponse('You are not allowed here!!!')
    if request.method =='POST':
        room.delete()
        return redirect('home')
    return render(request,"base/delete.html",{'obj':room})