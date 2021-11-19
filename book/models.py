from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    slug = models.SlugField(
            default='',
            editable=False,
            max_length=100
            )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = { 
                'pk': self.id, 
                'slug': self.slug
                }
        return reverse('author-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = { 
                'pk': self.id, 
                'slug': self.slug
                }
        return reverse('publisher-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ManyToManyField(Publisher)
    pubdate = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = { 
                'pk': self.id, 
                'slug': self.slug
                }
        return reverse('book-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = { 
                'pk': self.id, 
                'slug': self.slug
                }
        return reverse('store-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
