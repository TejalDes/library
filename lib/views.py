from codecs import lookup
from django.shortcuts import render
from django.views import View
from lib.models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class AuthorView(ListView):
    model = Author


class BookView(ListView):
    model = Books
    template_name = "lib/books.html"


# class BooksAuthorView(View):
#     def get(self, request):
#         au = request.GET.get("author")
#         print(au)
#         bk = Books.objects.get(author__author_name=au)
#         context = {"data": bk}
#         return render(request, "lib/booksauthor.html", context)


class BooksAuthorView(DetailView):
    model = Books
    template_name = "lib/booksauthor.html"

    # override get queryset to change query .....doesnt work for url params
    # def get_queryset(self, **kwargs):
    #     au = self.request.GET.get("author")
    #     print(au)
    #     bk = Books.objects.filter(author__author_name=au)
    #     return bk

    # override get_object of detailview to return an object instead of a queryset
    # after receiving info from url parameters....for more info look in detail.py
    # ctrl click on detail view to see detail.py
    def get_object(self):
        au = self.request.GET.get("author")
        print(au)
        bk = Books.objects.get(author__author_name=au)
        return bk
