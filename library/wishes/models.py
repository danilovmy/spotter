from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Favorites(models.Model):
    class Meta:
        verbose_name = _('Favorite')
        verbose_name_plural = _('Favorites')
        default_related_name = 'favorites'

    user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} -> {self.book}'