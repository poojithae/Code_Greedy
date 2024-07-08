from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    #international standard book number
    isbn = models.IntegerField(unique=True)
   

    def __str__(self):
        return self.title