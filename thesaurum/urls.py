from django.conf.urls import url
from thesaurum import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^application/new$', views.application_new, name="application_new"),
    url(r'^upload/$', views.simple_upload, name="upload"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
