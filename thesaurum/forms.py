from registration.forms import RegistrationForm
from django import forms
from .models import Application, Grading


class ExtendedRegistrationForm(RegistrationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'label': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'label': 'last_name'}))


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['name', 'faculty', 'coordinator', 'coordinator_phone',
                  'coordinator_email', 'recurring', 'previous_subsidy',
                  'previous_subsidy_date', 'date', 'place', 'description',
                  'uj_attendees', 'other_attendees',
                  'target_group_justification', 'project_goals', 'work_plan',
                  'project_value', 'support_visibility',
                  'cooperating_organizations', 'scope', 'programme',
                  'overall_cost', 'requested_subsidy']
        widgets = {
            'scope': forms.RadioSelect,
        }


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class GradingForm(forms.ModelForm):

    class Meta:
        model = Grading
        fields = ['project_rational', 'project_justified', 'cost_rational', 'cost_justified', 'comment']