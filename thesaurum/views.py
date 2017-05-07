from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ApplicationForm


def index(request):
    return render(request, 'thesaurum/index.haml')


@login_required
def userPage(request):
    form = ApplicationForm()
    return render(request, 'thesaurum/mypage.haml', {
                  'form': form,
                  })
