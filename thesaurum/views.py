from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm, get_objects_for_user
from django.urls import reverse

from .forms import ApplicationForm


def index(request):
    return render(request, 'thesaurum/index.haml')


@login_required
def userPage(request):
    form = ApplicationForm()
    return render(request, 'thesaurum/mypage.haml', {
                  'form': form,
                  })


@login_required
def application_new(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            owner = request.user
            app = form.save()
            assign_perm('view_application', owner, app)
            return HttpResponseRedirect(reverse('application_list'))
    else:
        form = ApplicationForm()

    return render(request, 'thesaurum/application_edit.haml', {'form': form})


@login_required
def application_list(request):
    apps = get_objects_for_user(request.user, 'thesaurum.view_application')
    return render(request, 'thesaurum/application_list.haml', {'apps': apps})
