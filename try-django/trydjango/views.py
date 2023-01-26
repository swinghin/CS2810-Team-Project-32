"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


    
def home_view(request, *args, **kwargs):
    """
    Take in a request -> Return HTML as response
    """
    name = "Ethan" #hardcoded
    number = random.randint(10, 1000)
    
    #from the database
    article_obj = Article.objects.get(id=2)
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    #Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """
    # <h1>{article_obj.title} ({article_obj.id})!
    # <p>{article_obj.content}!
    # """.format(**context)
    
    return HttpResponse(HTML_STRING)