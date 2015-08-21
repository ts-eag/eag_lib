# coding: utf-8
from .models import Status


# 이게 로딩될 때만 읽어오는지 아니면 함수가 쓰일때마다 Pass 값을 가져오는지 잘 모르겠네.
# status_pass = Status.objects.get(status='Pass')