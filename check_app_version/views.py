import os
from django.http import JsonResponse
from django.shortcuts import render
from check_app_version.models import AppVersion


def check_version(request, app_id):
    if app_id == 'MobiusPushTaesan001':
        app = AppVersion.objects.filter(app_id=app_id).order_by('-pk')[0]
        app.download_cnt += 1
        app.save()
        dic = {'app_id': app.app_id,
               'app_version': app.app_version,
               # 'file_name': app_dic.file_name,
               # 'file_path': app_dic.file_path,
               'apk_file': app.apk_file.url,
               'apk_size': app.apk_size,
               # 'ipa_file': app_dic.ipa_file,
               'register_date': app.register_date,
               'download_cnt': app.download_cnt}
        return JsonResponse(dic)

    # apk, ipa. file type field.
    # decide apk or ipa: other app
    else:
        dic = {'app_id': 'Check exact App id'}
        return JsonResponse(dic)