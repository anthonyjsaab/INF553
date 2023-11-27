from django.core.paginator import Paginator
from django.shortcuts import render

from app.models import *


# Create your views here.

def start_page(request):
    journal_list = PubmedArticle.objects.values('journal_title').distinct().order_by('journal_title')
    journal_list = [(i + 1, journal_list[i]['journal_title']) for i in range(len(journal_list))]
    paginator = Paginator(journal_list, request.GET.get("size", 200))
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "journals_list.html", {"page_obj": page_obj})


def journal_page(request, journal_title):
    relevant_article_ids = PubmedArticle.objects.filter(journal_title=journal_title).values('article_id')
    relevant_author_ids = ArticleAuthor.objects.filter(article_id__in=relevant_article_ids).values('author_id').distinct()
    authors_list = PubmedAuthor.objects.filter(author_id__in=relevant_author_ids).order_by('author_name').values('author_name')
    authors_list = [(i + 1, authors_list[i]['author_name']) for i in range(len(authors_list))]
    paginator = Paginator(authors_list, request.GET.get("size", 200))
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "authors_list.html", {"page_obj": page_obj, "journal_title": journal_title})


def author_page(request):
    return None