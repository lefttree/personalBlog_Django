from django.shortcuts import render
from django.http import HttpResponse
#import article
from article.models import Article
from datetime import datetime

from django.http import Http404

# Create your views here.

def home(request):
    post_list = Article.objects.all()
    dic = {
        'post_list': post_list
    }
    return render(request, 'bootstrap_home.html', dic)

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    dic = {
        'post': post
    }
    return render(request, 'post.html', dic)

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    dic = {
        'post_list': post_list,
        'error': False
    }
    return render(request, 'archives.html', dic)

def about_me(request):
    return render(request, "aboutme.html")

def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact = tag)
    except Article.DoesNotExist:
        raise Http404
    dic = {
        'post_list': post_list
    }
    return render(request, 'tag.html', dic)

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, "home.html")
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0:
                dic = {
                    'post_list': post_list,
                    'error': True
                }
                return render(request, 'archives.html', dic)
            else:
                dic = {
                    'post_list': post_list,
                    'error': False
                }
                return render(request,'archives.html', dic)

    return redirect('/')
