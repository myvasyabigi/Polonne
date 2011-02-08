from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from articles.models import Article
from articles.models import Category

def main(request):
    articles = cache.get('articles')
    if not articles:
        articles = Article.objects.filter(is_published=True).order_by('-published')
        cache.set('articles', articles)
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.all()
        cache.set('categories', categories)

    data = {
        "articles":articles,
        "categories": categories,
    }

    return render_to_response("index.html", data, RequestContext(request))

def category_list(request, template="articles/category-list.html"):
    categoriest = Category.objects.all()

    categories = Category.objects.all()

    data = {
        "categories": categories,
    }
    return render_to_response(template, data, RequestContext(request))
    

def article_category(request, slug, *args, **kwargs):
    
    category = Category.objects.get(slug=slug)
    articles = category.article_set.all().filter(is_published=True)

    data = {
        "category": category,
        "articles": articles,
    }

    return render_to_response("articles/article-category.html", data,
        RequestContext(request))


def article_details(request, category_slug, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    articles = Article.objects.all()

    data = {
        "article": article,
        "articles": articles,
        }

    return render_to_response("articles/article-details.html",data,
        RequestContext(request))

