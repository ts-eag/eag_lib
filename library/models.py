# -*- coding: utf-8 -*-
from datetime import timedelta, datetime, date
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

RESERVATION_LIMIT_TIME = 0
DURATION = 4

class User(models.Model):
    '''사용자'''
    name = models.CharField(max_length=50, null=False, blank=False)
    # email = models.EmailField()

    def __str__(self):
        return self.name


class Room(models.Model):
    '''남자방, 여자방 같이'''
    name = models.CharField(max_length=50, null=False, blank=False,
                            help_text='방의 이름. 남자방, 여자방 같이 방을 구분하는데 사용한다.')

    def __str__(self):
        return self.name


class Status(models.Model):
    '''좌석 예약이 가능한지?
    Pass, Available
    Available이 아닌 상태의 좌석은 예약할 수 없다.
    '''
    status = models.CharField(max_length=50, null=False, blank=False,
                              help_text='좌석 예약이 가능한지? Pass, Available')

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.status

class Type(models.Model):
    '''좌석의 속성중 하나. 칸막이 여부'''
    type = models.CharField(max_length=50, null=False, blank=False,
                            help_text='현재 좌석의 타입. 칸막이 여부, 또?')

    def __str__(self):
        return self.type


class Seat(models.Model):
    '''좌석'''
    room = models.ForeignKey(Room)
    seat_num = models.PositiveIntegerField(null=False, blank=False, unique=True)

    # 사용불가, 사용가능은 여기에서 제어
    # STATUS_CHOICES = (
    #     ('Pass', 'Pass'),
    #     ('Available', 'Available'),
    # )
    # status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    status = models.ForeignKey(Status)

    # type: 칸막이, 비칸막이
    type = models.ForeignKey(Type)

    # 일단은 정석대로 모든 테이블 읽어와서 뿌려주기로 하자.
    # 그게 된 다음 모델에 Field 를 하나 추가해 보자.
    # 총 좌석. seat_num 이 하나씩 추가될 때마다 증가. 삭제될 때마다 감소
    # total = models.PositiveIntegerField()
    # 자리가 예약되면 +1 되게 하는 트리거
    # used_seat = models.PositiveIntegerField()
    # 사용되는 좌석
    # Reservation 모델에서 현재 시간 < end_time 일 경우 사용중.

    def __str__(self):
        return '{}:{}'.format(self.room, self.seat_num)


def get_end_time(hours=DURATION):
    '''시작시간 + 4시간 더해서 돌려주기
    종료 시간 수정하려면 이 함수에서
    '''
    return datetime.now() + timedelta(hours=hours)


def not_duplicate_at_same_time(value):
    '''종료시간 > now 보다 큰 것들 중에서 좌석번호 filtering'''
    now = datetime.now()
    last_time = Reservation.objects.filter(end_time__gte=now).filter(seat_id=value).count()
    duplicate = Reservation.objects.filter(end_time__gte=now).filter(seat_id=value).count()
    # name = Reservation.objects.get(seat_id=value).name
    if duplicate:
        raise ValidationError('This is booked time at seat={}'.format(value))


def validate_start_time(value):
    print(value, type(value))
    if value < timezone.now() + timedelta(hours=RESERVATION_LIMIT_TIME):
        raise ValidationError('+{}시간 이후로 설정해 주세요.'.format(RESERVATION_LIMIT_TIME))


class Reservation(models.Model):
    '''예약
    기본 4시간 예약'''
    user = models.ForeignKey(User)
    seat = models.ForeignKey(Seat)
    # validator
    # start_time은 현재 시간보다 이후여야 한다.
    # start_time = models.DateTimeField(default=datetime.now,
    #                                   validators=[validate_start_time])
    start_time = models.DateTimeField(default=datetime.now)
    # start_time = models.DateTimeField(default=datetime.now, null=False, blank=False)
    # start_time을 고정해 놔서 그렇네... 이걸 유동적으로 바꿀 수 있게 하자.
    end_time = models.DateTimeField(default=get_end_time)
    # end_time = models.DateTimeField(default=get_end_time, null=False, blank=False)
    # end_time은 사용자가 변경할 수 없도록. 무조건 start_time + 4시간
    # js로 입력 시간이 바뀌면 자동으로 end_time도 변경되서 보여주게끔 해야겠다.

    def __unicode__(self):
        return '{}:{} {}:{}'.format(self.user, self.seat, self.start_time, self.end_time)

    # def save(self):
    #     if self.seat_id in

    # timezone.datetime(2015, 8, 12, 16, 40, tzinfo=pytz.utc)
    # pytz.datetime.datetime(2015, 8, 12, 16, 40, tzinfo=pytz.utc)


    def save(self, *args, **kwargs):
        '''
        1. end_time = start_time + 4hours
        2. 동일 시간 중복 제거 Query
        '''
        self.end_time = self.start_time + timedelta(hours=4)

        status_pass = Status.objects.get(status='Pass')
        pass_filter = self.seat.status == status_pass
        if pass_filter:
            raise ValidationError('This seat:{} will not booked. Because pass seat.'.
                                  format(self.seat)
            )

        dup_filter = Reservation.objects.filter(
            end_time__gte=self.start_time).filter(
            start_time__lt=self.end_time).filter(
            seat_id=self.seat).exclude(
            pk=self.pk)
        if dup_filter:
            raise ValidationError('This seat:{} is booked at same time'.format(
                self.seat))
        super(Reservation, self).save(*args, **kwargs)

    def start_time_strftime(self):
        return timezone.localtime(self.start_time).strftime('%Y-%m-%d %H:%M:%S')

    def end_time_strftime(self):
        return timezone.localtime(self.end_time).strftime('%Y-%m-%d %H:%M:%S')

    def seat_status(self):
        return self.seat.status


def get_datetime_now():
    return datetime.now()


class ExtensionTime(models.Model):
    '''연장
    하루에 1번만 연장 가능
    모델을 조회해서 특정 user가 없으면 예약 가능
    특정 user의 today의 frequency가 1 이상이라면 예약할 수 없다.
    '''
    user = models.ForeignKey(User)
    # date = models.DateField(default=get_datetime_now)
    date = models.DateField(default=date.today, null=False, blank=False)
    frequency = models.PositiveIntegerField(default=0, null=False, blank=False)

    class Meta:
        unique_together = ('user', 'date',)

    def save(self, *args, **kwargs):
        self.frequency += 1
        super(ExtensionTime, self).save(*args, **kwargs)

    def __str__(self):
        return '{}:{}'.format(self.user, self.frequency)



