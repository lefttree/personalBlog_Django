from django.shortcuts import render
from django.http import HttpResponse
#import article
from article.models import Article
from datetime import datetime

# Create your views here.

def home(request):
    return HttpResponse("Hello world, django")

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)

def test(request):
    dic = {
        'current_time': datetime.now()
    }
    return render(request, 'test.html', dic)
