from django.shortcuts import render
from .models import AddImage
# Create your views here.

def index(request):
    slider_img=AddImage.objects.all()
    context = {

        'slider_img':slider_img
    }
    return render(request,'index.html',context)

