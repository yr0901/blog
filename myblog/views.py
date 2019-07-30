from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    blogs= Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'home.html',{'blogs':blogs, 'posts' : posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def writing(request):
    return render(request, 'writing.html')

def submit(request):
    new = Blog()
    new.title = request.GET['title']
    new.body = request.GET['body']
    new.date = timezone.datetime.now()
    new.save()
    return redirect('detail', new.pk)

