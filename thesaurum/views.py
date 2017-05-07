from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'thesaurum/index.haml')


@login_required
def userPage(request):
    return render(request, 'thesaurum/mypage.haml')
