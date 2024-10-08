from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class BookQuerySet(models.QuerySet):

    def similar(self):
        exclude = self.values_list('id', flat=True)
        # TODO here should be implement similarity algorithm to get similar books
        # it is not defined, what should be done, what is similar for nothing
        return self.exclude(id__in=exclude).order_by('?')[:5]

# Create your models here.
class Book(models.Model):

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
        default_related_name = 'books'

    title = models.CharField(max_length=1000)
    authors = models.ManyToManyField('Author')
    year = models.IntegerField(validators=[MinValueValidator(1970), MaxValueValidator(9999)], blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)], blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    book_format = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="books/", blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)

    objects = BookQuerySet.as_manager()

    def __str__(self):
        return f'{self.title} - {self.authors.to_title()}'


class AuthorQuerySet(models.QuerySet):

    def to_title(self):
        return ', '.join(self.values_list('name', flat=True))


class Author(models.Model):

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')
        default_related_name = 'authors'

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    image = models.ImageField(upload_to="authors/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    objects = AuthorQuerySet.as_manager()

    def __str__(self):
        return self.name
