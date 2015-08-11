# -*- coding: utf-8 -*-
from datetime import timedelta, datetime, date
from django.core.validators import RegexValidator
from django.db import models


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
    room_id = models.ForeignKey(Room)
    seat_num = models.PositiveIntegerField(null=False, blank=False, unique=True)

    # 사용불가, 사용가능은 여기에서 제어
    # STATUS_CHOICES = (
    #     ('Pass', 'Pass'),
    #     ('Available', 'Available'),
    # )
    # status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    status_id = models.ForeignKey(Status)

    # type: 칸막이, 비칸막이
    type_id = models.ForeignKey(Type)

    # 일단은 정석대로 모든 테이블 읽어와서 뿌려주기로 하자.
    # 그게 된 다음 모델에 Field 를 하나 추가해 보자.
    # 총 좌석. seat_num 이 하나씩 추가될 때마다 증가. 삭제될 때마다 감소
    # total = models.PositiveIntegerField()
    # 자리가 예약되면 +1 되게 하는 트리거
    # used_seat = models.PositiveIntegerField()
    # 사용되는 좌석
    # Reservation 모델에서 현재 시간 < end_time 일 경우 사용중.

    def __str__(self):
        return '{}:{}'.format(self.room_id, self.seat_num)


def get_end_time(hours=4):
    '''시작시간 + 4시간 더해서 돌려주기
    종료 시간 수정하려면 이 함수에서
    '''
    return datetime.now() + timedelta(hours=hours)


class Reservation(models.Model):
    '''예약
    기본 4시간 예약'''
    user_id = models.ForeignKey(User)
    seat_id = models.ForeignKey(Seat)
    start_time = models.DateTimeField(auto_now_add=True, auto_now=True)
    end_time = models.DateTimeField(default=get_end_time)

    def __str__(self):
        return '{}:{}'.format(self.user_id, self.seat_id)


def get_datetime_now():
    return datetime.now()


class ExtensionTime(models.Model):
    '''연장
    하루에 1번만 연장 가능
    모델을 조회해서 특정 user가 없으면 예약 가능
    특정 user의 today의 frequency가 1 이상이라면 예약할 수 없다.
    '''
    user_id = models.ForeignKey(User)
    # date = models.DateField(default=get_datetime_now)
    date = models.DateField(default=date.today, null=False, blank=False)
    frequency = models.PositiveIntegerField(default=0, null=False, blank=False)

    class Meta:
        unique_together = ('user_id', 'date',)

    def save(self, *args, **kwargs):
        self.frequency += 1
        super(ExtensionTime, self).save(*args, **kwargs)

    def __str__(self):
        return '{}:{}'.format(self.user_id, self.frequency)



