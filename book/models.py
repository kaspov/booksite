from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class NameAndSlug(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
            default='',
            editable=False,
            max_length=100
            )

    class meta: 
        abstract=True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = { 
                'pk': self.id, 
                'slug': self.slug
                }
        cls = self.__class__.__name__.lower()

        return reverse(f'{cls}-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Reader(NameAndSlug):
    pass

class Author(NameAndSlug):
    age = models.IntegerField()

class Publisher(NameAndSlug):
    pass

class Book(NameAndSlug):
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ManyToManyField(Publisher)
    pubdate = models.DateField()

class Store(NameAndSlug):
    books = models.ManyToManyField(Book)



