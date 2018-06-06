from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('NEW', 'New Site'),
    ('EX', 'Existing Site'),
)

PRIORITY_CHOICES = (
    ('U', 'Urgent - 1 week or less'),
    ('N', 'Normal - 2 to 4 weeks'),
    ('L', 'Low - Still Researching'),
)

class Quote(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=60, blank=True)
    company = models.CharField(max_length=60, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    web = models.URLField(blank=True)
    description = models.TextField()
    sitestatus = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=40, choices=PRIORITY_CHOICES)
    jobfile = models.FileField(upload_to='uploads/', blank=True)
    submitted = models.DateField(auto_now_add=True)
    quotedate = models.DateField(blank=True, null=True)
    quoteprice = models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0)
    # bob on_delete argument was missing causing:
    # TypeError: __init__() missing 1 required positional argument: 'on_delete'
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)
