import os
from django.db import models


class AppVersion(models.Model):
    app_id = models.CharField(max_length=20, null=False, blank=False)
    app_version = models.CharField(max_length=10, null=False, blank=False)
    # file_name = models.CharField(max_length=50, null=False, blank=False)
    # file_path = models.CharField(max_length=200, null=False, blank=False)
    apk_file = models.FileField(upload_to='apk/')
    apk_size = models.IntegerField(default=0)
    # ipa_file = models.FileField(upload_to='ipa/')
    # file_size = models.BigIntegerField(null=True)
    download_cnt = models.BigIntegerField(default=0, null=False, blank=False)
    register_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    def save(self, *args, **kwargs):
        self.apk_size = self.apk_file.size
        super(AppVersion, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{}:{}'.format(self.app_id, self.app_version)
