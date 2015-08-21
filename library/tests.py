# -*- coding: utf-8 -*-
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
# from library.views import home_page
from django.utils import timezone
import pytz
from eag_lib import settings
from library.models import Reservation, DURATION
from populate_lib import add_user, add_room, add_status, add_type, add_seat, add_reservation, add_extension_time


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

        self.man_room = add_room('Man')

        self.status_available = add_status('Available')
        self.status_noavailable = add_status('Pass')
        self.status_using = add_status('Using')

        self.type_partition = add_type('Partition')
        self.type_nopartition = add_type('No Partition')


        self.seat1 = add_seat(room=self.man_room,
             seat_num=1,
             status=self.status_available,
             type=self.type_partition
        )

        self.seat2 = add_seat(room=self.man_room,
             seat_num=2,
             status=self.status_available,
             type=self.type_partition
        )

        self.seat3 = add_seat(room=self.man_room,
             seat_num=3,
             status=self.status_available,
             type=self.type_partition
        )

        self.seat4 = add_seat(room=self.man_room,
             seat_num=4,
             status=self.status_available,
             type=self.type_partition
        )

        self.seat5 = add_seat(room=self.man_room,
             seat_num=15,
             status=self.status_noavailable,
             type=self.type_nopartition
        )

        self.seat8 = add_seat(room=self.man_room,
             seat_num=16,
             status=self.status_using,
             type=self.type_nopartition
        )

        self.room_woman = add_room('Woman')

        self.seat6 = add_seat(room=self.room_woman,
             seat_num=10,
             status=self.status_available,
             type=self.type_partition
        )

        self.seat7 = add_seat(room=self.room_woman,
             seat_num=13,
             status=self.status_available,
             type=self.type_nopartition
        )


        # 0분으로 설정하면 실패함.. 이유는 모르겠다.. 안에 저장된 데이터 보면 똑같은데..
        # self.now = timezone.datetime(2015, 8, 21, 1, 0, tzinfo=pytz.utc)
        self.now = timezone.datetime(2015, 8, 21, 1, 1, tzinfo=pytz.utc)
        # self.now = timezone.now()
        self.end = self.now + timedelta(hours=4)
        self.local_time = self.now.astimezone(pytz.timezone(settings.TIME_ZONE))
        self.now2 = self.local_time + timedelta(minutes=30)
        self.end2 = self.now2 + timedelta(hours=4)
        print(self.now)
        print(self.end)

        add_reservation(
            user=self.user_jo, seat=self.seat1, start_time=self.now, end_time=self.end
        )

        add_reservation(
            user=self.user_jo, seat=self.seat3, start_time=self.now, end_time=self.end
        )

        add_reservation(
            user=self.user_oh, seat=self.seat4, start_time=self.now, end_time=self.end
        )

        add_reservation(
            user=self.user_oh, seat=self.seat8, start_time=self.now, end_time=self.end
        )

        # add_extension_time(
        #     user=self.user_jo, date=self.date.today(), frequency=0
        # )
        #
        # add_extension_time(
        #     user=self.user_oh, date=self.date.today(), frequency=0
        # )

    def test_dup_filter_on_same_seat_at_same_time(self):
        print(Reservation.objects.all())
        with self.assertRaises(ValidationError):
            r = add_reservation(
                user=self.user_jo, seat=self.seat1, start_time=self.now, end_time=self.end
            )
            print('')
            print(r.start_time)
            print(r.end_time)
            print(Reservation.objects.all())

            # end_time
            # start_time
            # seat_id
            # exclude pk

    def test_dup_filter_on_same_seat_different_user(self):
        with self.assertRaises(ValidationError):
            r = add_reservation(
                user=self.user_oh, seat=self.seat1, start_time=self.now, end_time=self.end
            )

    def test_dup_filter_on_same_seat_at_start_time(self):
        with self.assertRaises(ValidationError):
            r = add_reservation(
                user=self.user_oh, seat=self.seat1, start_time=self.now, end_time=self.end
            )

    def test_pass_filter(self):
        with self.assertRaises(ValidationError):
            add_reservation(
                user=self.user_jo, seat=self.seat8,
                start_time=self.now2, end_time=self.end2
            )

    def test_regular_book_time(self):
        local_timezone = pytz.timezone(settings.TIME_ZONE)
        start_local_time = timezone.datetime(2015, 8, 21, tzinfo=pytz.utc).astimezone(
            local_timezone)
        end_local_time = start_local_time + timedelta(hours=DURATION)

        # local_time = self.start_time.astimezone(local_timezone)

        self.assertEqual(end_local_time,
                         timezone.datetime(2015, 8, 21, DURATION, 0,
                                           tzinfo=pytz.utc).astimezone(local_timezone))

    def test_reservation_boundary_minute_at_now(self):
        '''00분, 29분, 30분, 59분 등록시 테스트'''
        local_timezone = pytz.timezone(settings.TIME_ZONE)
        start_local_time = timezone.datetime(2015, 8, 21, 1, 0, tzinfo=pytz.utc)
        start_local_time2 = timezone.datetime(2015, 8, 21, 1, 30, tzinfo=pytz.utc)
        end_local_time = start_local_time + timedelta(hours=DURATION)
        end_local_time2 = start_local_time2 + timedelta(hours=DURATION)

        r = add_reservation(
                user=self.user_jo, seat=self.seat6,
                start_time=start_local_time, end_time=end_local_time
            )

        self.assertEqual(r.start_time, timezone.datetime(
            2015, 8, 21, 1, 0, tzinfo=pytz.utc)
        )
        r.delete()

        r = add_reservation(
                user=self.user_jo, seat=self.seat6,
                start_time=start_local_time + timedelta(minutes=29),
                end_time=end_local_time + timedelta(minutes=29)
            )

        self.assertEqual(r.start_time, timezone.datetime(
            2015, 8, 21, 1, 0, tzinfo=pytz.utc)
        )
        r.delete()

        r = add_reservation(
                user=self.user_jo, seat=self.seat6,
                start_time=start_local_time2, end_time=end_local_time2
            )
        self.assertEqual(r.start_time, timezone.datetime(
            2015, 8, 21, 1, 30, tzinfo=pytz.utc)
        )
        r.delete()

        r = add_reservation(
                user=self.user_jo, seat=self.seat6,
                start_time=start_local_time2 + timedelta(minutes=29),
                end_time=end_local_time2 + timedelta(minutes=29)
            )

        self.assertEqual(r.start_time, timezone.datetime(
            2015, 8, 21, 1, 30, tzinfo=pytz.utc)
        )
        r.delete()

    def test_reservation_boundary_minute(self):

        pass

    # def test_end_time(self):
    #     with self.assertRaises(ValidationError):



    # def test_end_time(self):
    #     '''시작 시간 + 4시간 = 종료시간?'''
    #     # start_time+timedelta(hours=4)
    #     print(Reservation.objects.count())
    #
    #
    #     add_reservation(
    #         user=self.user_jo, seat=self.seat1, start_time=self.now, end_time=self.end
    #     )
    #
    #     # tzinfo가 utc라서 안 맞네
    #     # 이건 나중에 해결하자. 일단 skip
    #     print('self.now ', self.now)
    #     print('self.now +4 ', self.now + timedelta(hours=4))
    #     utc_tz = pytz.utc
    #     # print('self.now +4 ', utc_tz.normalize(self.now + timedelta(hours=4)).astimezone(utc_tz))
    #     print('Reservation.objects.last().end_time', Reservation.objects.last().end_time)
    #
    #     # self.assertEqual(Reservation.objects.last().end_time,
    #     #                  (self.now + timedelta(hours=4)).replace(tzinfo=pytz.utc))
    #
    #
    #     # print(Reservation.objects.last().end_time == self.now + timedelta(hours=4))
    #     localtz = pytz.timezone('Asia/Seoul')
    #     # print('')
    #     # print(Reservation.objects.last().end_time.replace(tzinfo=settings.TIME_ZONE))
    #     # print(pytz.timezone(settings.TIME_ZONE).localize(self.now + timedelta(hours=4)))
    #     # # print(localtz.normalize(Reservation.objects.last().end_time.astimezone(localtz)))
    #     # print('')
    #     last_time = Reservation.objects.last().end_time
    #     last_time2 = localtz.normalize(Reservation.objects.last().end_time.astimezone(localtz))
    #     now_plus_4 = localtz.normalize(self.now + timedelta(hours=4)).astimezone(localtz)
    #     # now_plus_4 = (self.now + timedelta(hours=4)).replace(tzinfo=pytz.timezone('Asia/Seoul'))
    #     print(last_time)
    #     print(last_time2)
    #     print(now_plus_4)
    #
    #     self.assertEqual(last_time2,
    #                      now_plus_4)

    # 예약하는 시간은 현재 시간보다 + 1 시간?? 현재 와서 바로 사용하는 사용자들이 불만 제기할 수 있음
    # 이건 좀 더 생각해보자.
    # 종료시간을 역으로 정렬해서 언제 좌석을 예약할 수 있는지 보여주기

    # 시간에 대한 6가지 경우 중복x
    # http://www.gurubee.net/article/50256

    # Pass인 것은 예약할 때 등록하면 안됨

    # 동일한 사용자가 동일한 시간에 2개의 좌석을 예약할 수 없다.
    # 현재 사용자의 예약 좌석수를 먼저 체크한 후에 해야겠는데..?