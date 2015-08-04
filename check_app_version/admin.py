from django.contrib import admin
from check_app_version.models import AppVersion


class AppVersionAdmin(admin.ModelAdmin):
    list_display = ['app_id', 'app_version', 'apk_file', 'apk_size', 'register_date', 'download_cnt']
    # ordering = ['-id']


admin.site.register(AppVersion, AppVersionAdmin)