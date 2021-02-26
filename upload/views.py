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
        # TODO: Write method, in a folder at this app (tools/, for instance),
        #  to validate the input file

        # TODO: Its important to keep this file during runtime only?
        # TODO: How long will take "runtime", there is, how long will
        #  the user be using the application?

        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        script.openImage(uploaded_file.name)

    return render(request, 'upload/upload.html')
