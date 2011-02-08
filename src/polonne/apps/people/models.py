from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"))
    contacts = models.TextField(_("Contacts"), blank=True, null=True)

    class Meta:
        verbose_name=_("Profile")
        verbose_name_plural=_("Profiles")

    def __unicode__(self):
        return self.user.username
