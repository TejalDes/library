from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=255)
    author_email = models.EmailField(max_length=255)

    def __str__(self):
        return self.author_name


# class Publisher(models.Model):
#     publisher_name = models.CharField(max_length=255)
#     publisher_email = models.EmailField(max_length=255)
#     publisher_site = models.URLField(max_length=255)

#     def __str__(self):
#         return self.publisher_name


class Books(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_price = models.IntegerField()
    book_isbn = models.CharField(max_length=255)
    book_published_date = models.DateField()
    # publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("book_name", "author", "book_isbn")

    def __str__(self):
        return self.book_name
