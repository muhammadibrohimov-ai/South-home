from django.shortcuts import render
from .models import Blog, BlogCategory

# Create your views here.

def blog_view(request):
    return render(request=request, template_name='blog/blog.html', context={'blogs':Blog.objects.all(), 'categories':BlogCategory.objects.all()})

def single_blog_view(request, id):
    return render(request=request, template_name='blog/single-blog.html', context={'blogs':Blog.objects.get(id=id), 'categories':BlogCategory.objects.all()})