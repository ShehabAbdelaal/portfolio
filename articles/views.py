from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #The homepage for articles
    return render(request, 'articles/index.html')

@login_required
def articles(request):
    #Show all articles
    articles = Article.objects.order_by('-date_added')
    context = {'articles' : articles}
    return render(request, 'articles/articles.html', context)

@login_required
def article_detail(request, article_id):
    #Show article detail
    article = Article.objects.get(id=article_id)
    return render(request, 'articles/article_detail.html', {'article' : article})
