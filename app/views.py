from django.core.paginator import Paginator
from django.shortcuts import render

from app.models import *


# Create your views here.

def start_page(request):
    journal_list = PubmedArticle.objects.order_by('journal_title').values('journal_title').distinct()
    journal_list = [(i + 1, journal_list[i]['journal_title']) for i in range(len(journal_list))]
    paginator = Paginator(journal_list, request.GET.get("size", 200))
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "journals_list.html", {"page_obj": page_obj})


def journal_page(request, journal_title):
    authors_list = PubmedAuthor.objects.filter(articleauthor__article__journal_title=journal_title).distinct().order_by(
        'author_name')
    authors_list = [(i + 1, authors_list[i].author_name, authors_list[i].author_id) for i in
                    range(len(authors_list))]
    paginator = Paginator(authors_list, request.GET.get("size", 200))
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "authors_list.html", {"page_obj": page_obj, "journal_title": journal_title})


def author_page(request, author_id):
    author_name = PubmedAuthor.objects.filter(author_id=author_id)[0].author_name
    articles = PubmedArticle.objects.filter(articleauthor__author_id=author_id).order_by('-year', 'journal_title')
    return render(request, 'author_page.html', {'articles': articles, 'author_name': author_name})
