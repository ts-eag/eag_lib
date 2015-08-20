# coding: utf-8
from django.db.models import signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Reservation, Seat, Status


@receiver(post_save, sender=Reservation)
def reservation_post_save(sender, instance, created, **kwargs):
    # print('sender', sender)
    # print('instance', instance)
    # print('created', created)
    # print('kwargs', kwargs)
    if created:
        status_using = Status.objects.get(status='Using')
        instance.seat.status = status_using
        instance.seat.save()


# 삭제될 때도 변경해 줘야지
@receiver(post_delete, sender=Reservation)
def reservation_post_delete(sender, instance, **kwargs):
    # print('sender', sender)
    # print('instance', instance)
    # print('kwargs', kwargs)

    status_available = Status.objects.get(status='Available')
    instance.seat.status = status_available
    instance.seat.save()