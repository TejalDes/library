from django.shortcuts import render
from django.views import View
from lib.models import *


class AuthorView(View):
    def get(self, request):
        au = Author.objects.all()
        context = {"data": au}
        return render(request, "lib/authors.html", context)


class BookView(View):
    def get(self, request):
        bk = Books.objects.all()
        context = {"data": bk}
        return render(request, "lib/books.html", context)


class BooksAuthorView(View):
    def get(self, request):
        au = request.GET.get("author")
        print(au)
        bk = Books.objects.get(author__author_name=au)
        context = {"data": bk}
        return render(request, "lib/booksauthor.html", context)
