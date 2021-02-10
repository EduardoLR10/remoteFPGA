from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from . import script

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def queue(request):
    return render(request, 'upload/queue.html')

@login_required(login_url='login')
def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        script.openImage(uploaded_file.name)
    return render(request, 'upload/upload.html')