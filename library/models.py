# -*- coding: utf-8 -*-
from datetime import timedelta, datetime, date
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    # email = models.EmailField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

class Type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Seat(models.Model):
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

    def __str__(self):
        return '{}:{}'.format(self.room_id, self.seat_num)


def get_end_time(hours=4):
    return datetime.now() + timedelta(hours=hours)


class Reservation(models.Model):
    user_id = models.ForeignKey(User)
    seat_id = models.ForeignKey(Seat)
    start_time = models.DateTimeField(auto_now_add=True, auto_now=True)
    end_time = models.DateTimeField(default=get_end_time)

    def __str__(self):
        return '{}:{}'.format(self.user_id, self.seat_id)


def get_datetime_now():
    return datetime.now()


class ExtensionTime(models.Model):
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



