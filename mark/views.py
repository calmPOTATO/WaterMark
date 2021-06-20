from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo

def showPhoto(request):
    photo = Photo.objects.all()
    return render(request, 'mark/showPhoto.html', {'photo':photo})
