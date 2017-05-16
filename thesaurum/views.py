from django.core.files.storage import FileSystemStorage
from django.forms import Form
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.static import serve
from guardian.shortcuts import assign_perm, get_objects_for_user
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from guardian.shortcuts import get_perms
from django.shortcuts import get_object_or_404


from pyThesaurum import settings
from thesaurum.models import Application, File, Grading
from .forms import ApplicationForm, GradingForm


def index(request):
    submitted_apps = Application.objects.filter(state='submitted')
    to_grade_apps = Application.objects.filter(state='accepted')
    graded_apps = Application.objects.filter(state='accepted')
    return render(request, 'thesaurum/index.haml', {
        'submitted_apps': submitted_apps,
        'to_grade_apps': to_grade_apps,
        'graded_apps': graded_apps,
    })


@login_required
def userPage(request):
    form = ApplicationForm()
    return render(request, 'thesaurum/mypage.haml', {
        'form': form,
    })


@login_required
def application_edit(request, app_id=None):
    if app_id:
        app = get_object_or_404(Application, pk=app_id)
        if 'change_application' not in get_perms(request.user, app):
            raise PermissionDenied
        if app.state is not 'new':
            raise PermissionDenied
    else:
        app = Application()
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=app)
        if form.is_valid():
            form.owner = request.user
            owner = request.user
            app = form.save(commit=False)
            app.owner = owner
            app.save()
            assign_perm('view_application', owner, app)
            assign_perm('change_application', owner, app)
            return HttpResponseRedirect(reverse('application_list'))
    else:
        form = ApplicationForm(instance=app)
    return render(request, 'thesaurum/application_edit.haml', {'form': form})


@login_required
def application_grade(request, app_id):
    app = get_object_or_404(Application, pk=app_id)
    if 'grade_application' in get_perms(request.user, app):
        raise PermissionDenied
    if app.state is not 'accepted':
        raise PermissionDenied
    if request.method == 'POST':
        form = GradingForm(request.POST)
        if form.is_valid():
            grading = form.save(commit=False)
            grading.user = request.user
            grading.application = app
            grading.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = GradingForm()

    return render(request, 'thesaurum/grading_new.haml', {
        'form': form,
        'project_rational': 'Pytanie 1',
        'project_justified': 'Pytanie 2',
        'cost_rational': 'Pytanie 3',
        'cost_justified': 'Pytanie 4'
    })


@login_required
def application_list(request):
    apps = get_objects_for_user(request.user, 'thesaurum.view_application')
    return render(request, 'thesaurum/application_list.haml', {
        'apps': apps,
    })


@login_required
def application_details(request, app_id):
    app = get_object_or_404(Application, pk=app_id)
    files = File.objects.filter(application=app).values()
    form = ApplicationForm(instance=app)
    can_grade = not Grading.objects.filter(user=request.user, application=app).exists()
    for b in form:
        b.field.widget.attrs['disabled'] = True
    return render(request, 'thesaurum/application_details.haml', {
        'form': form,
        'app': app,
        'can_grade': can_grade,
        'files': files,
    })


@login_required
def application_accept(request, app_id):
    app = get_object_or_404(Application, pk=app_id)
    if app.state is not 'submitted':
        raise PermissionDenied
    app.state = 'accepted'
    app.save()
    return HttpResponseRedirect(reverse('application_details', args=[app_id]))


@login_required
def application_return_back(request, app_id):
    app = get_object_or_404(Application, pk=app_id)
    if app.state is not 'submitted':
        return PermissionDenied
    app.state = 'new'
    app.save()
    return HttpResponseRedirect(reverse('application_details', args=[app_id]))


@login_required
def application_grades(request, app_id):
    grades = Grading.objects.filter(application__id=app_id)
    grades_count = grades.count()
    return render(request, 'thesaurum/grades.haml', {
        'grades': grades,
        'grades_count': grades_count,
        'project_rational': Grading.objects.filter(application__id=app_id, project_rational=True).count(),
        'project_justified': Grading.objects.filter(application__id=app_id, project_justified=True).count(),
        'cost_rational': Grading.objects.filter(application__id=app_id, cost_rational=True).count(),
        'cost_justified': Grading.objects.filter(application__id=app_id, cost_justified=True).count(),
    })


@login_required
def simple_upload(request, app_id):
    # form = Form(request.POST)
    app = get_object_or_404(Application, pk=app_id)
    if 'change_application' not in get_perms(request.user, app):
        raise PermissionDenied
    files = File.objects.filter(application=Application.objects.get(id=app_id)).values()
    if request.method == 'POST':
        if 'myfile' in request.FILES.keys() and Form(request.POST).is_valid():
            myfile = request.FILES['myfile']
            fs = FileSystemStorage(location='uploads/' + app_id)
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            print("uploads/" + app_id + "/" + filename)
            file_ob = File()
            file_ob.application = app
            file_ob.path = "uploads/" + app_id + "/" + filename
            file_ob.name = filename
            file_ob.save()
            return HttpResponseRedirect(reverse('application_details', args=[app_id]))
        else:
            return render(request, 'simple_upload.html', {
                'files': files,
                'errors': "Please choose a file"
            })
    return render(request, 'simple_upload.html', {'files': files})


@login_required
def application_submit(request, app_id):
    app = get_object_or_404(Application, pk=app_id)
    if app.state is not 'new':
        raise PermissionDenied
    app.state = 'submitted'
    app.save()
    return HttpResponseRedirect(reverse('application_details', args=[app.id]))


@login_required
def show_all_uploaded_files_for_application(request, app_id):
    files = File.objects.filter(application = Application.objects.get(id = app_id)).values()
    print(files)
    return render(request, 'thesaurum/files_list.haml', {
        'files': files,
    })


@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    id_from_url = path.split('/')[0]

    app_upload = Application.objects.get(id = id_from_url)
    apps = get_objects_for_user(request.user, 'thesaurum.view_application')

    flag = True

    for app in apps:
        if app == app_upload:
            flag = False

    if (flag):
        return render(request, '403.html', status=403)

    return serve(request, path, settings.MEDIA_URL[1:] , show_indexes)
