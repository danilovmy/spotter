from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Account(AbstractUser):

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')
        default_related_name = 'accounts'
