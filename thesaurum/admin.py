from django.contrib import admin
from guardian.admin  import GuardedModelAdmin
from thesaurum.models import Application, Grading, File


@admin.register(Application)
class ApplicationAdmin(GuardedModelAdmin):
    pass


@admin.register(Grading)
class GradingAdmin(GuardedModelAdmin):
    pass
