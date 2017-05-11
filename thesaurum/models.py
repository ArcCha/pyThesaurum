from django.db import models


class Application(models.Model):
    SCOPES = [('international', 'International'),
              ('nationwide', 'Nationwide'),
              ('environmental', 'Environmental'),
              ('university', 'University')]

    name = models.CharField(max_length=200, blank=True)
    faculty = models.CharField(max_length=200, blank=True)
    coordinator = models.CharField(max_length=200, blank=True)
    coordinator_phone = models.CharField(max_length=20, blank=True)
    coordinator_email = models.EmailField(blank=True)
    recurring = models.BooleanField(blank=True)
    previous_subsidy = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    previous_subsidy_date = models.DateField(blank=True)
    date = models.DateField(blank=True)
    place = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    uj_attendees = models.IntegerField(blank=True)
    other_attendees = models.IntegerField(blank=True)
    target_group_justification = models.TextField(blank=True)
    project_goals = models.TextField(blank=True)
    work_plan = models.TextField(blank=True)
    project_value = models.TextField(blank=True)
    support_visibility = models.TextField(blank=True)
    cooperating_organizations = models.TextField(blank=True)
    scope = models.CharField(max_length=50, choices=SCOPES, blank=False,
                             default='university')
    programme = models.TextField(blank=True)
    overall_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    requested_subsidy = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    submitted = models.BooleanField(blank=True)
