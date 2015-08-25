# coding:utf-8
from django.contrib import admin

# Register your models here.
from library.models import Seat, Room, Reservation, Type, Status, ExtensionTime, UserProfile


class UserProfileAdmin(admin.ModelAdmin):

    list_display = ("username", "phone")

    search_fields = ["user__username"]


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id']
    # list_display_links = ['id', 'title']
    search_fields = ['name']
    ordering = ['-id']


class ExtensionTimeAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'frequency']
    list_filter = ['user']
    # list_display_links = ['id', 'title']
    search_fields = ['user', 'date']
    ordering = ['-user']


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'seat', 'added_time_strftime',
                    'start_time_strftime', 'end_time_strftime', 'seat_status']
    # list_editable = ['user',]
    # seat 테이블 inline??


class SeatAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'seat_num', 'status', 'type']
    list_filter = ['room', 'status', 'type']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(ExtensionTime, ExtensionTimeAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Room, RoomAdmin)

