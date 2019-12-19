# For Class-based views we import.

from django.shortcuts import render

# For Class-based views we import.

from django.views.generic import TemplateView

class ClassView(TemplateView):
    template_name="index.html"


def FunctionViews(request):
    return render(request,"indextwo.html")