from django.conf.urls import url
from thesaurum import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^applications/$', views.application_list, name="application_list"),
    url(r'^applications/new$', views.application_edit, name="application_new"),
    url(r'^applications/(?P<app_id>\d+)/edit$',
        views.application_edit, name="application_edit"),
    url(r'^applications/(?P<app_id>\d+)$',
        views.application_details, name="application_details"),
    url(r'^applications/(?P<app_id>\d+)/submit$',
        views.application_submit, name="application_submit"),
]
