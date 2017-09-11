from django.shortcuts import render
from django.http import HttpResponse
from .models import TutorialModel
from .models import ArticleModel


'''AUTHOR : PAKISARUS'''


def index(request):
    #get_list_or_404()
    tutorials = TutorialModel.objects.all()  #.order_by('-pub_date')[:5]
    context = {
        'tutorials': tutorials,
    }
    return render(request, 'tutorials/index.html', context)


def detail(request, tutname = 'python', articlename = 'introduction'):
    tut =tutname
    article = articlename
    return render(request, 'tutorials/' + tut + '/' + article + '.html')

