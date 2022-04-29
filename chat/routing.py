# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    # 인스턴스를 인스턴스화할 ASGI 응용 프로그램을 얻기 위해 as_asgi() 클래스 메서드를 호출
    # Django 클래스 뷰의 인스턴스에 대해 동일한 역할을 하는 Django의 as_view()와 유사합니다.
    
]

# URL라우터
"""
HTTP 경로를 통해 http 또는 websocket 유형 연결을 라우팅합니다. 
단일 인수, Django URL 객체 목록(path() 또는 re_path())을 취합니다.
"""