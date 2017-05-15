from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm, get_objects_for_user
from django.urls import reverse

from .forms import ApplicationForm
from .models import Application


def index(request):
    return render(request, 'thesaurum/index.haml')


@login_required
def userPage(request):
    form = ApplicationForm()
    return render(request, 'thesaurum/mypage.haml', {
                  'form': form,
                  })


@login_required
def application_edit(request, app_id=None):
    if app_id:
        app = Application.objects.get(pk=app_id)
    else:
        app = Application()
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=app)
        if form.is_valid():
            owner = request.user
            app = form.save()
            assign_perm('view_application', owner, app)
            return HttpResponseRedirect(reverse('application_list'))
    else:
        form = ApplicationForm(instance=app)
    return render(request, 'thesaurum/application_edit.haml', {'form': form})


@login_required
def application_list(request):
    apps = get_objects_for_user(request.user, 'thesaurum.view_application')
    return render(request, 'thesaurum/application_list.haml', {'apps': apps})


@login_required
def application_details(request, app_id):
    app = Application.objects.get(pk=app_id)
    form = ApplicationForm(instance=app)
    for b in form:
        b.field.widget.attrs['disabled'] = True
    return render(request, 'thesaurum/application_details.haml', {'form': form, 'app_id': app.id, 'state': app.state})


@login_required
def application_submit(request, app_id):
    app = Application.objects.get(pk=app_id)
    app.state = 'submitted'
    app.save()
    return HttpResponseRedirect(reverse('application_details', args=[app.id]))
