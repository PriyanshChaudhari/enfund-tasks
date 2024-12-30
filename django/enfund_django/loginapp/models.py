from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey relationship

    def __str__(self):
        return self.title

class Reader(models.Model):
    user = models.OneToOneField(Author, on_delete=models.CASCADE)  # OneToOneField relationship
    favorite_books = models.ManyToManyField(Book)  # ManyToManyField relationship

    def __str__(self):
        return self.user.name
