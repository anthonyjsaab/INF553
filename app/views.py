from django.core.paginator import Paginator
from django.shortcuts import render

from app.models import PubmedArticle


# Create your views here.

def start_page(request):
    journal_list = PubmedArticle.objects.order_by('journal_title').values('journal_title').distinct()
    journal_list = [(i + 1, journal_list[i]['journal_title']) for i in range(len(journal_list))]
    paginator = Paginator(journal_list, 200)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj})
