# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.db import models


def validate_file_extension(value):
    if not value.name.endswith('.apk'):
        raise ValidationError('apk file만 올려주세요.')


class AppVersion(models.Model):
    app_id = models.CharField(max_length=20, null=False, blank=False, help_text='MobiusPushTaesan001 로 고정합니다. App id가 달라지면 안됩니다.')
    app_version = models.CharField(max_length=10, null=False, blank=False, help_text='App의 버전을 입력합니다. 모바일 어플은 이 정보로 새로운 App인지 비교하기 때문에 중요합니다.')
    # file_name = models.CharField(max_length=50, null=False, blank=False)
    # file_path = models.CharField(max_length=200, null=False, blank=False)
    apk_file = models.FileField(upload_to='apk/',
                                validators=[validate_file_extension],
                                help_text='apk 파일만 올립니다.')
    apk_size = models.IntegerField(default=0, help_text='자동 계산 됩니다. 입력 생략')
    # ipa_file = models.FileField(upload_to='ipa/')
    # file_size = models.BigIntegerField(null=True)
    download_cnt = models.BigIntegerField(default=0, null=False, blank=False, help_text='자동 계산 됩니다. 입력 생략')
    register_date = models.DateTimeField(auto_now_add=True, auto_now=True)

    def save(self, *args, **kwargs):
        self.apk_size = self.apk_file.size
        super(AppVersion, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{}:{}'.format(self.app_id, self.app_version)
