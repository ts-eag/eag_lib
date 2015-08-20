# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, tzinfo
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
# from library.views import home_page
import pytz
from eag_lib import settings
from library.models import Reservation
from populate_lib import add_user, add_room, add_status, add_type, add_seat, add_reservation


# class HomePageTest(TestCase):
#     def test_root_url_resolve_to_home_page_view(self):
#         found = resolve('/library/')
#         self.assertEqual(found.func, home_page)
#
#     def test_home_page_returns_correct_html(self):
#         request = HttpRequest()
#         response = home_page(request)
#         expected_html = render_to_string('library/index.html')
#         self.assertEqual(response.content.decode(), expected_html)



class ModelTest(TestCase):
    def setUp(self):
        self.user_jo = add_user('Jo')
        self.user_oh = add_user('Oh')

        self.room_man = add_room('Man')

        self.status_available = add_status('Available')
        self.status_noavailable = add_status('Pass')

        self.type_partition = add_type('Partition')
        self.type_nopartition = add_type('No Partition')

        self.seat1 = add_seat(room=self.room_man,
             seat_num=1,
             status=self.status_available,
             type=self.type_partition
        )
        self.now = datetime.utcnow()
        self.end = self.now + timedelta(hours=4)

        
        
        # populate_lib.populate()

    def test_end_time(self):
        '''시작 시간 + 4시간 = 종료시간?'''
        # start_time+timedelta(hours=4)
        print(Reservation.objects.count())


        add_reservation(
            user=self.user_jo, seat=self.seat1, start_time=self.now, end_time=self.end
        )

        # tzinfo가 utc라서 안 맞네
        # 이건 나중에 해결하자. 일단 skip
        print('self.now ', self.now)
        print('self.now +4 ', self.now + timedelta(hours=4))
        utc_tz = pytz.utc
        # print('self.now +4 ', utc_tz.normalize(self.now + timedelta(hours=4)).astimezone(utc_tz))
        print('Reservation.objects.last().end_time', Reservation.objects.last().end_time)

        # self.assertEqual(Reservation.objects.last().end_time,
        #                  (self.now + timedelta(hours=4)).replace(tzinfo=pytz.utc))


        # print(Reservation.objects.last().end_time == self.now + timedelta(hours=4))
        localtz = pytz.timezone('Asia/Seoul')
        # print('')
        # print(Reservation.objects.last().end_time.replace(tzinfo=settings.TIME_ZONE))
        # print(pytz.timezone(settings.TIME_ZONE).localize(self.now + timedelta(hours=4)))
        # # print(localtz.normalize(Reservation.objects.last().end_time.astimezone(localtz)))
        # print('')
        last_time = Reservation.objects.last().end_time
        last_time2 = localtz.normalize(Reservation.objects.last().end_time.astimezone(localtz))
        now_plus_4 = localtz.normalize(self.now + timedelta(hours=4)).astimezone(localtz)
        # now_plus_4 = (self.now + timedelta(hours=4)).replace(tzinfo=pytz.timezone('Asia/Seoul'))
        print(last_time)
        print(last_time2)
        print(now_plus_4)

        self.assertEqual(last_time2,
                         now_plus_4)

    # 예약하는 시간은 현재 시간보다 + 1 시간?? 현재 와서 바로 사용하는 사용자들이 불만 제기할 수 있음
    # 이건 좀 더 생각해보자.
    # 종료시간을 역으로 정렬해서 언제 좌석을 예약할 수 있는지 보여주기

    # 시간에 대한 6가지 경우 중복x
    # http://www.gurubee.net/article/50256

    # Pass인 것은 예약할 때 등록하면 안됨

    # 동일한 사용자가 동일한 시간에 2개의 좌석을 예약할 수 없다.
    # 현재 사용자의 예약 좌석수를 먼저 체크한 후에 해야겠는데..?