# -*- coding: utf-8 -*-
from datetime import timedelta
from django.shortcuts import render
from django.utils import timezone
from library.models import Room, Status, Seat, Reservation, DURATION


def get_room_status():
    man_room = Room.objects.get(name='Man')
    woman_room = Room.objects.get(name='Woman')

    len_all_man_rooms = Seat.objects.filter(room=man_room).count()
    len_all_woman_rooms = Seat.objects.filter(room=woman_room).count()

    status_pass = Status.objects.get(status='Pass')

    len_man_pass_seats = Seat.objects.filter(
        room=man_room).filter(
        status=status_pass).count()
    len_woman_pass_seats = Seat.objects.filter(
        room=woman_room).filter(
        status=status_pass).count()

    time_now = timezone.now()
    time_now_plus_duration = time_now + timedelta(hours=DURATION)

    used_rooms_at_now = Reservation.objects.filter(
        end_time__gte=time_now).filter(
        start_time__lt=time_now_plus_duration)

    len_used_man_rooms = len([room for room in used_rooms_at_now
                              if room.seat.room == man_room])
    len_used_woman_rooms = len([room for room in used_rooms_at_now
                                if room.seat.room == woman_room])

    len_available_man_rooms = len_all_man_rooms - len_man_pass_seats - len_used_man_rooms
    len_available_woman_rooms = len_all_woman_rooms - len_woman_pass_seats - len_used_woman_rooms

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


    # man_total_room = man_room.seat_set.count()
    # woman_total_room = woman_room.seat_set.count()

    # status_available = Status.objects.get(status='Available')
    status_pass = Status.objects.get(status='Pass')
    # 예약 가능 좌석수 = 총 갯수 - 사용불가 좌석수 - 현재 사용중 좌석수
    # available_room = total_room - '현재 사용 갯수'

    # Seat.objects.filter(room=1)
    # Seat.objects.filter(room=man_room)
    # Seat.objects.filter(room=man_room).filter(status=status_available)
    # len_man_pass_seats = Seat.objects.filter(room=man_room).filter(status=status_pass).count()
    # len_man_pass_seats = Seat.objects.filter(room=woman_room).filter(status=status_pass).count()

    # now = timezone.now()
    # Reservation.objects.filter(end_time__gte=now)


    # Seat.objects.filter(room=man_room).count()
    # available_seat = Seat.objects.filter(room=man_room).count() - \
    #                  Seat.objects.filter(room=man_room).filter(
    #                      status=status_pass).count() # -
    #
    # time_now = timezone.now()
    # time_now_plus = time_now + timedelta(hours=DURATION)
    #
    # used_rooms_at_now = Reservation.objects.filter(
    #     end_time__gte=time_now).filter(
    #     start_time__lt=time_now_plus)

    # Reservation.objects.last().seat.room


    # SQL로 할 수 있는 방법이 있을것 같다.
    # 일단 먼저 코드로 구현하고 시간이 되면 SQL로 짜보자
    # len_woman_rooms = len([room for room in used_rooms_at_now if room.seat.room == woman_room])
    # len_man_rooms = len([room for room in used_rooms_at_now if room.seat.room == man_room])
    #
    # man_seats = Seat.objects.filter(room=man_room)

    context = get_room_status()
    return render(request, 'library/index.html', context)


def man(request):
    context = get_room_status()
    man_room = Room.objects.get(name='Man')
    seats = Seat.objects.filter(room=man_room)

    time_now = timezone.now()
    time_now_plus_duration = time_now + timedelta(hours=DURATION)
    used_seats_at_now = Reservation.objects.filter(
        end_time__gte=time_now).filter(
        start_time__lt=time_now_plus_duration)
    print(used_seats_at_now)

    return render(request,
                  'library/man.html',
                  {'context': context,
                   'seats': seats,
                   'used_seats_at_now': used_seats_at_now,
                   })