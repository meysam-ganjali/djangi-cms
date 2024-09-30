from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Category


@receiver(post_delete, sender=Category)
def delete_logo(sender, instance, **kwargs):
    instance.logo.delete(False)
