from django.urls import path

from lib.views import *

urlpatterns = [
    path("authors/", AuthorView.as_view()),
    path("books/", BookView.as_view()),
    path("bksauth/", BooksAuthorView.as_view()),
]
