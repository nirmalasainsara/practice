from datetime import datetime, timezone
from django.db import models
from django.utils.translation import gettext as _
from django.utils.timezone import now
from datetime import timedelta

# Create your models here.
class Todo(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    done = models.BooleanField(_("Done"), default=False)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
