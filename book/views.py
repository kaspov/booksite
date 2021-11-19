from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
from book.models import Author, Publisher, Book, Store

def home(request):
    return render(request, 'home.html')

class AuthorDetailView(DetailView):
    model = Author

class PublisherDetailView(DetailView):
    model = Publisher

class BookDetailView(DetailView):
    model = Book

class StoreDetailView(DetailView):
    model = Store 



class AuthorListView(ListView):
    model = Author

class PublisherListView(ListView):
    model = Publisher

class BookListView(ListView):
    model = Book

class StoreListView(ListView):
    model = Store 


