from django.shortcuts import render
from .models import Project
from blog.models import Blog
from django.views.generic import ListView, DetailView


class HomepageDisplay(ListView):
    template_name = 'portfolio/home.html'
    model = Project
    context_object_name = 'projects'


# def home(request):
#     projects = Project.objects.all
#     return render(request, 'portfolio/home.html', {
#         'projects': projects,
#     })

class DitailProject(DetailView):
    template_name = 'portfolio/info_project.html'
    model = Project
    context_object_name = 'info'
