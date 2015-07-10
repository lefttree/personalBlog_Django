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
    return render(request, 'home.html', dic)

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    dic = {
        'post': post
    }
    return render(request, 'post.html', {'post': post})

def test(request):
    dic = {
        'current_time': datetime.now()
    }
    return render(request, 'test.html', dic)
