from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from files.models import *
from files.forms import *
from files import attach, manage, members

# Create your views here.

def is_admin(request):
    return request.user.is_authenticated()

@csrf_protect
def main_page(request):
    admin = is_admin(request)
    if request.method == 'POST' and admin:
        if request.POST['task'] == 'upload':
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                manage.upload(request.FILES['file'])
                return HttpResponseRedirect('/')
        elif request.POST['task'] == 'delete':
            manage.delete(int(request.POST['id']))
            return HttpResponseRedirect('/')
    else:
        form = UploadForm()
    file_list = File.objects.order_by('-date')
    var = {
        'admin': admin,
        'form': form,
        'file_list': file_list
    }
    return render(request, 'home.html', var)

def download(request, num):
    return attach.get_download_response(request, int(num))

@csrf_protect
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    return members.login(request)

def logout(request):
    return members.logout(request)
