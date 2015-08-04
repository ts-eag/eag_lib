from django.contrib import admin

# Register your models here.
from library.models import Seat, Room, User, Reservation, Type, Status, ExtensionTime


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id']
    # list_display_links = ['id', 'title']
    search_fields = ['name']
    ordering = ['-id']


class ExtensionTimeAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'date', 'frequency']
    list_filter = ['user_id']
    # list_display_links = ['id', 'title']
    search_fields = ['user_id', 'date']
    ordering = ['-user_id']


admin.site.register(User)
admin.site.register(Seat)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(ExtensionTime, ExtensionTimeAdmin)
admin.site.register(Reservation)
admin.site.register(Room, RoomAdmin)

