from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm, get_objects_for_user
from django.urls import reverse


from thesaurum.models import Application, File
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

    app_to_grade = Application.objects.get(id = id_app)
    apps = get_objects_for_user(request.user, 'thesaurum.view_application')

    flag = True

    for app in apps:
        print(app.id)
        if app.id == app_to_grade.id:
            flag = False

    if(flag):
        return render(request, '403.html', status=403)

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
    return render(request, 'thesaurum/application_list.haml', {
        'apps': apps,
    })

@login_required
def simple_upload(request, app_id):
    files = File.objects.filter(application=Application.objects.get(id=app_id)).values()
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='uploads/' + app_id)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print("uploads/" + app_id + "/" + filename)
        file_ob = File()
        file_ob.application = Application.objects.get(id = app_id)
        file_ob.path = "uploads/" + app_id + "/" + filename
        file_ob.name = filename
        file_ob.save()
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'file_name': myfile.name,
            'files': files
        })
    return render(request, 'simple_upload.html', {'files': files})

@login_required
def show_all_uploaded_files_for_application(request, app_id):
    files = File.objects.filter(application = Application.objects.get(id = app_id)).values()
    print(files)
    return render(request, 'thesaurum/files_list.haml', {
        'files': files,
    })
