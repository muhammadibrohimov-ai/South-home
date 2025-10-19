from django.shortcuts import render

# Create your views here.

def blog_view(request):
    return render(request=request, template_name='blog/blog.html')

def single_blog_view(request, id):
    return render(request=request, template_name='blog/single-blog.html')