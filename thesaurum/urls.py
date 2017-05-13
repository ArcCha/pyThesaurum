from django.conf.urls import url
from thesaurum import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^applications/$', views.application_list, name="application_list"),
    url(r'^applications/new$', views.application_new, name="application_new"),
    url(r'^applications/(\d+)/upload/$', views.simple_upload, name="upload"),
    url(r'^applications/(\d+)/grade/$', views.grading_new, name="grading_new"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
