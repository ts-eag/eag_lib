# coding: utf-8
import os
from datetime import datetime, timedelta, date

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'eag_lib.settings')

import django
django.setup()

# Must django.setup() before from rango.models import Category, Page
from library.models import Room, Seat, User, Status, Type, Reservation, ExtensionTime


def populate():
    user_jo = add_user('Jo')
    user_oh = add_user('Oh')

    room_man = add_room('Man')

    status_available = add_status('Available')
    status_noavailable = add_status('Pass')

    type_partition = add_type('Partition')
    type_nopartition = add_type('No Partition')


    seat1 = add_seat(room=room_man,
             seat_num=1,
             status=status_available,
             type=type_partition
    )

    seat2 = add_seat(room=room_man,
         seat_num=2,
         status=status_available,
         type=type_partition
    )

    seat3 = add_seat(room=room_man,
         seat_num=3,
         status=status_available,
         type=type_partition
    )

    seat4 = add_seat(room=room_man,
         seat_num=4,
         status=status_available,
         type=type_partition
    )

    seat5 = add_seat(room=room_man,
         seat_num=15,
         status=status_noavailable,
         type=type_nopartition
    )

    room_woman = add_room('Woman')

    seat6 = add_seat(room=room_woman,
         seat_num=10,
         status=status_available,
         type=type_partition
    )

    seat7 = add_seat(room=room_woman,
         seat_num=13,
         status=status_available,
         type=type_nopartition
    )


    now = datetime.now()
    end = now + timedelta(hours=4)

    add_reservation(
        user=user_jo, seat=seat1, start_time=now, end_time=end
    )

    add_reservation(
        user=user_jo, seat=seat3, start_time=now, end_time=end
    )

    add_reservation(
        user=user_oh, seat=seat4, start_time=now, end_time=end
    )

    add_extension_time(
        user=user_jo, date=date.today(), frequency=0
    )

    add_extension_time(
        user=user_oh, date=date.today(), frequency=0
    )

    # # Print out what we have added to the user.
    # for c in Room.objects.all():
    #     for p in Seat.objects.filter(category=c):
    #         print('- {0} - {1}'.format(str(c), str(p)))


def add_user(name):
    n = User.objects.get_or_create(name=name)[0]
    return n


def add_seat(room, seat_num, status, type):
    r = Seat.objects.get_or_create(
        room=room,
        seat_num=seat_num,
        status=status,
        type=type
    )[0]
    return r


def add_reservation(user, seat, start_time, end_time):
    r = Reservation.objects.get_or_create(
        user=user, seat=seat, start_time=start_time, end_time=end_time
    )
    return r



def add_extension_time(user, date, frequency):
    try:
        e = ExtensionTime.objects.get_or_create(
            user=user, date=date, frequency=frequency
        )
    except Exception as e:
        print(e)
        pass
    else:
        return e


def add_room(name):
    r = Room.objects.get_or_create(name=name)[0]
    return r


def add_status(status):
    s = Status.objects.get_or_create(status=status)[0]
    return s


def add_type(type):
    t = Type.objects.get_or_create(type=type)[0]
    return t

if __name__ == '__main__':
    print('Starting Library Management System population script...')
    populate()