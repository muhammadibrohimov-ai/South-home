from django.shortcuts import render
from .models import Blog, BlogCategory
from main.models import Home
from django.shortcuts import get_object_or_404

# Create your views here.


def blog_view(request):
    return render(request=request, template_name='blog/blog.html', context={'blogs':Blog.objects.all(), 'categories':BlogCategory.objects.all(), "homes":Home.objects.all()})


def blog_category_view(request, id):
    
    try:
        category = BlogCategory.objects.get(id = id)
        blogs = Blog.objects.filter(category = category)
    
    except:
        blogs = False
        
    return render(request=request, template_name='blog/blog.html', context={'blogs':blogs, 'categories':BlogCategory.objects.all(), "homes":Home.objects.all()})


def single_blog_view(request, id):
    
    
    return render(request=request, template_name='blog/single-blog.html', context={'blog':Blog.objects.get(id=id), 'categories':BlogCategory.objects.all()})