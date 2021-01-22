from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from . import script

class Home(TemplateView):
    template_name = 'upload/home.html'

def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        script.openImage(uploaded_file.name)
    return render(request, 'upload/upload.html')