from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from Membership.models import Person


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        p = Person()
        p.user = instance
        p.save()
