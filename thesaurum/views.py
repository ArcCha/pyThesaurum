from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm, get_objects_for_user
from django.urls import reverse

from thesaurum.models import Application
from .forms import ApplicationForm, GradingForm


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
def grading_new(request, id_app):
    print(id_app)
    print(request.user.id)
    if request.method == 'POST':
        form = GradingForm(request.POST)
        if form.is_valid():
            grading_object = form.save(commit=False)
            grading_object.user = request.user
            grading_object.application = Application.objects.get( id = id_app)
            grading_object.save()
            return HttpResponseRedirect(reverse('application_list'))
        else:
            print(form.errors)
    else:
        form = GradingForm()

    return render(request, 'thesaurum/grading_new.haml', {
        'form': form,
        'first_question': 'Pytanie 1',
        'second_question': 'Pytanie 2',
        'third_question': 'Pytanie 3',
        'fourth_question': 'Pytanie 4'
    })

@login_required
def application_list(request):
    apps = get_objects_for_user(request.user, 'thesaurum.view_application')
    return render(request, 'thesaurum/application_list.haml', {'apps': apps})

@login_required
def simple_upload(request, id):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='uploads/'+id)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'file_name': myfile.name
        })
    return render(request, 'simple_upload.html')