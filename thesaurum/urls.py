import django
from django.conf.urls import url, include
from thesaurum import views
from django.conf import settings
from django.conf.urls.static import static

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
    url(r'^applications/(?P<app_id>\d+)/upload/$',
        views.simple_upload, name="upload"),
    url(r'^applications/(?P<app_id>\d+)/grade/$',
        views.application_grade, name="application_grade"),
    url(r'^applications/(?P<app_id>\d+)/accept$',
        views.application_accept, name="application_accept"),
    url(r'^applications/(?P<app_id>\d+)/return_back$',
        views.application_return_back, name="application_return_back"),
    url(r'^applications/(?P<app_id>\d+)/grades$',
        views.application_grades, name="application_grades"),
    url(r'^applications/(?P<app_id>\d+)/files/$',
        views.show_all_uploaded_files_for_application, name="files"),
    url(r'^uploads/(?P<path>.*)$', views.protected_serve),
    url(r'^delete/(?P<app_id>\d+)$',
        views.delete, name="delete"),
]

handler404 = 'thesaurum.views.handler404'