# -*- coding: utf-8 -*-
from datetime import timedelta
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView
from library.models import Room, Status, Seat, Reservation, DURATION


def get_room_status():
    man_room = Room.objects.get(name='Man')
    woman_room = Room.objects.get(name='Woman')

    len_all_man_rooms = Seat.objects.filter(room=man_room).count()
    len_all_woman_rooms = Seat.objects.filter(room=woman_room).count()

    status_pass = Status.objects.get(status='Pass')
    status_using = Status.objects.get(status='Using')

    len_man_pass_seats = Seat.objects.filter(
        room=man_room).filter(
        status=status_pass).count()
    len_woman_pass_seats = Seat.objects.filter(
        room=woman_room).filter(
        status=status_pass).count()

    using_seats = Seat.objects.filter(status=status_using)
    len_used_man_seats = using_seats.filter(room=man_room).count()
    len_used_woman_seats = using_seats.filter(room=woman_room).count()

    len_available_man_rooms = len_all_man_rooms - len_man_pass_seats - len_used_man_seats
    len_available_woman_rooms = len_all_woman_rooms - len_woman_pass_seats - len_used_woman_seats

    context = {'len_all_man_rooms': len_all_man_rooms,
               'len_all_woman_rooms': len_all_woman_rooms,
               'len_available_man_rooms': len_available_man_rooms,
               'len_available_woman_rooms': len_available_woman_rooms}
    return context

def index(request):
    '''
    총 사용자수, 현재 사용자수,
    각 방의 총 좌석수, 각 방의 예약가능 좌석수(총 좌석수 - 사용 좌석수)
    '''


    # CBV면 Queryset으로?? 일단은 FBV로 하자!

    # SQL로 할 수 있는 방법이 있을것 같다.
    # 일단 먼저 코드로 구현하고 시간이 되면 SQL로 짜보자

    context = get_room_status()
    # print(context)
    return render(request, 'library/index.html', context)


def man(request, room_name):
    man_room = Room.objects.get(name=room_name.capitalize())
    seats = Seat.objects.filter(room=man_room)

    return render(request,
                  'library/seat_list.html',
                  {'object_list': seats,})


class ManListView(ListView):
    model = Seat
    # template_name = 'library/seat_list.html'

    def get_context_data(self, **kwargs):
        # print(kwargs)
        context = super(ManListView, self).get_context_data(**kwargs)
        man_room = Room.objects.get(name='Man')
        context['object_list'] = context['object_list'].filter(room=man_room)
        context['room_name'] = '3층 남자'
        # print(context)
        return context


class WomanListView(ListView):
    model = Seat
    # template_name = 'library/seat_list.html'

    def get_context_data(self, **kwargs):
        # print(kwargs)
        context = super(WomanListView, self).get_context_data(**kwargs)
        woman_room = Room.objects.get(name='Woman')
        context['object_list'] = context['object_list'].filter(room=woman_room)
        context['room_name'] = '4층 여자'
        # print(context)
        return context


