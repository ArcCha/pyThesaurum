from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

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
            return HttpResponseRedirect()
    else:
        form = ApplicationForm()

    return render(request, 'thesaurum/application_edit.haml', {'form': form})

@login_required
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='uploads/folder1')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'file_name': myfile.name
        })
    return render(request, 'simple_upload.html')