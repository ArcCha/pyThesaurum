from django.conf.urls import url
from thesaurum import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^applications/$', views.application_list, name="application_list"),
    url(r'^applications/new$', views.application_new, name="application_new"),
]
