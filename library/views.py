from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


def man_room(request):
    return render(request, 'man_room.html')

