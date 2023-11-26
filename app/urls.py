from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='index'),
    path('<str:journal_title>', views.journal_page, name='journal'),
]
