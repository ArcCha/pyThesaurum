from django import forms


class ApplicationForm(forms.Form):
    SCOPES = [('international', 'International'),
              ('nationwide', 'Nationwide'),
              ('environmental', 'Environmental'),
              ('university', 'University')]

    name = forms.CharField(max_length=200)
    faculty = forms.CharField(max_length=200)
    coordinator = forms.CharField(max_length=200)
    coordinator_phone = forms.CharField(max_length=20)
    coordinator_email = forms.EmailField()
    recurring = forms.BooleanField()
    previous_subsidy = forms.DecimalField()
    previous_subsidy_date = forms.DateField()
    date = forms.DateField()
    place = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    uj_attendees = forms.IntegerField()
    other_attendees = forms.IntegerField()
    target_group_justification = forms.CharField(widget=forms.Textarea)
    project_goals = forms.CharField(widget=forms.Textarea)
    work_plan = forms.CharField(widget=forms.Textarea)
    project_value = forms.CharField(widget=forms.Textarea)
    support_visibility = forms.CharField(widget=forms.Textarea)
    cooperating_organizations = forms.CharField(widget=forms.Textarea)
    scope = forms.ChoiceField(choices=SCOPES, widget=forms.RadioSelect())
    programme = forms.CharField(widget=forms.Textarea)
    overall_cost = forms.DecimalField()
    requested_subsidy = forms.DecimalField()
