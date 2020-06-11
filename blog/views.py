from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def bloghome(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/bloghome.html',{'blogs':blogs})

def detail(request, blog_id):
    return render(request, 'blog/detail.html', {'id':blog_id})
