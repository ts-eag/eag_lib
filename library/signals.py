# coding: utf-8
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone
from .models import Reservation, Seat, Status, ExtensionTime


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


@receiver(post_save, sender=Reservation)
def extensiontime_post_save(sender, instance, created, **kwargs):
    if created:
        print(instance.user)
        # 여러개가 돌아온다: user, 날짜로 unique 하게 만드니, 다른 날짜에 예약하면 2개가 생김
        try:
            extensiontime = ExtensionTime.objects.get_or_create(user=instance.user)[0]
            extensiontime.frequency += 1
            extensiontime.save()
        except MultipleObjectsReturned:
            extensiontime = ExtensionTime.objects.filter(user=instance.user).last()
            extensiontime.frequency += 1
            extensiontime.save()

@receiver(post_delete, sender=Reservation)
def reservation_post_delete(sender, instance, **kwargs):
    if instance.start_time > timezone.now():
        extensiontime = ExtensionTime.objects.get(user=instance.user, date=instance.start_time)
        extensiontime.delete()