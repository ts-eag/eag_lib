# coding: utf-8
from django.utils import timezone
from django_cron import CronJobBase, Schedule
from eag_lib.settings import RESERVATION_PER_MINS
from .models import Status, Seat


class ChangeSeatStatus(CronJobBase):
    '''
    Seat Table의 status를 Using -> Available로 주기적으로 30분에 1번씩 돌면서 변경해 준다.
    status가 Using으로 되어 있는 seat만 불러온 다음 available로 변경해 준다.
    '''
    RUN_EVERY_MINS = RESERVATION_PER_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'library.change_seat_status'

    def do(self):
        now = timezone.now()
        status_available = Status.objects.get(status='Available')
        status_using = Status.objects.get(status='Using')

        using_seats = Seat.objects.filter(status=status_using)
        for seat in using_seats:
            # last()로 가장 마지막에 예약한 좌석만 변경해주면 된다.
            # 어차피 같은 자리는 동일한 시간에 예약할 수 없기 때문에
            if seat.reservation_set.last().end_time <= now:
                seat.status = status_available
                seat.save()