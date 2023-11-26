from django.core.paginator import Paginator
from django.shortcuts import render

from app.models import PubmedArticle


# Create your views here.

def start_page(request):
    pubmedarticle_list = PubmedArticle.objects.all()
    journal_list = list(set([x.journal_title for x in pubmedarticle_list]))
    journal_list.sort()
    paginator = Paginator(journal_list, 200)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(page_obj.__dict__)
    return render(request, "list.html", {"page_obj": page_obj})
