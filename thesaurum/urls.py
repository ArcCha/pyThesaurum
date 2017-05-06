from django.conf.urls import url
from thesaurum import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^myPage/$', views.userPage, name="mypage"),
]
