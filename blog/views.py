from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.generic import ListView, DetailView


class ShowAllBlogs(ListView):
    template_name = 'blog/all_blogs.html'
    model = Blog
    context_object_name = 'blogs'


# def all_blogs(request):
#     blogs = Blog.objects.order_by('-date')[:5]
#     return render(request, 'blog/all_blogs.html', {
#         'blogs': blogs,
#     })

class ShowDetailBlog(DetailView):
    template_name = 'blog/detail.html'
    model = Blog
    context_object_name = 'blog'

# def detail(request, blog_slug: str):
#     blog = get_object_or_404(Blog, slug=blog_slug)
#     return render(request, 'blog/detail.html', {
#         'blog': blog,
#     })
