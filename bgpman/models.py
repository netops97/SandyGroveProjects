from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


BGP_CHOICES = (
    ('NORMAL', 'Normalized'),
    ('ISOLATE', 'Isolated'),
)

VENDOR_CHOICES = (
    ('CTL','CenturyLink'),
    ('VZB', 'Verizon'),
)

#
# Router transactions use the following schema:
#
class Router(models.Model):
    hostname = models.CharField(max_length=100)
    address = models.GenericIPAddressField()
    vendor = models.CharField(max_length=20, choices=VENDOR_CHOICES, default=True)
    state = models.CharField(max_length=20, choices=BGP_CHOICES)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20, blank=True)
    ticketnumber = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    #changedate = models.CharField(max_length=40)
    #changedate = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.id)
