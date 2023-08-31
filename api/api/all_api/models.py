from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class actors(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    Agent_URL = models.CharField(max_length=255, null=True, blank=True)
    Agent_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=2550, null=True, blank=True)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    fax = models.CharField(max_length=255, null=True, blank=True)
    office_contact = models.TextField(max_length=255, null=True, blank=True)
    Mobile_no = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    Address = models.CharField(max_length=255, null=True, blank=True)
    StreetAddress = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=255, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    source = models.TextField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'agent'

