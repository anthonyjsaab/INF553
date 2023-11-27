from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='index'),
    path('journal/<str:journal_title>', views.journal_page, name='journal'),
    path('author/<str:author_id>', views.author_page, name='author'),
]
