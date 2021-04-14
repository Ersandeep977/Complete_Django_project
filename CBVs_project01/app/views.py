from django.shortcuts import render
from django.views.generic import ListView,DetailView
from app.models import Book
# Create your views here.r


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book