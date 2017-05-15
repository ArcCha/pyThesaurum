from django.contrib.auth.models import User
from django.db import models


class Application(models.Model):
    SCOPES = [('international', 'International'),
              ('nationwide', 'Nationwide'),
              ('environmental', 'Environmental'),
              ('university', 'University')]
    STATE = [('new', 'New'),
             ('submitted', 'Submitted')]

    name = models.CharField(max_length=200, null=True, blank=True)
    faculty = models.CharField(max_length=200, null=True, blank=True)
    coordinator = models.CharField(max_length=200, null=True, blank=True)
    coordinator_phone = models.CharField(max_length=20, null=True, blank=True)
    coordinator_email = models.EmailField(null=True, blank=True)
    recurring = models.BooleanField(default=True, blank=True)
    previous_subsidy = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    previous_subsidy_date = models.DateField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    place = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    uj_attendees = models.IntegerField(null=True, blank=True)
    other_attendees = models.IntegerField(null=True, blank=True)
    target_group_justification = models.TextField(null=True, blank=True)
    project_goals = models.TextField(null=True, blank=True)
    work_plan = models.TextField(null=True, blank=True)
    project_value = models.TextField(null=True, blank=True)
    support_visibility = models.TextField(null=True, blank=True)
    cooperating_organizations = models.TextField(null=True, blank=True)
    scope = models.CharField(max_length=50, choices=SCOPES, null=False,
                             default='university')
    programme = models.TextField(null=True, blank=True)
    overall_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    requested_subsidy = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    submitted = models.BooleanField(default=False, blank=True)
    state = models.CharField(max_length=20, choices=STATE, null=False,
                             default='new')

    class Meta:
        permissions = (
            ('view_application', 'View application'),
            ('edit_application', 'Edit application'),
        )

class Grading(models.Model):
    application = models.ForeignKey(Application)
    user = models.ForeignKey(User)
    first_question = models.BooleanField(default=False)
    second_question = models.BooleanField(default=False)
    third_question = models.BooleanField(default=False)
    fourth_question = models.BooleanField(default=False)

class File(models.Model):
    path = models.CharField(max_length=200, null=True, blank=True, default="")
    name = models.CharField(max_length=200, null=True, blank=True, default="")
    application = models.ForeignKey(Application, default= None)