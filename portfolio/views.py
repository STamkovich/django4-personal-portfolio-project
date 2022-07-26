from django.shortcuts import render
from .models import Project
from django.views.generic import ListView


class HomepageDisplay(ListView):
    template_name = 'portfolio/home.html'
    model = Project
    context_object_name = 'projects'


# def home(request):
#     projects = Project.objects.all
#     return render(request, 'portfolio/home.html', {
#         'projects': projects,
#     })
