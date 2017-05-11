from django.conf.urls import url
from thesaurum import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^application/new$', views.application_new, name="application_new"),
]
