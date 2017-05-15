import django
from django.conf.urls import url
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
    url(r'^applications/(?P<app_id>\d+)/upload/$', views.simple_upload, name="upload"),
    url(r'^applications/(?P<app_id>\d+)/grade/$', views.grading_new, name="grading_new"),
    url(r'^applications/(?P<app_id>\d+)/files/$', views.show_all_uploaded_files_for_application, name="files"),
    url(r'^uploads/(?P<path>.*)$', views.protected_serve),
]
              # + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
