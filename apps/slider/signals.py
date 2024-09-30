from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import (SliderItem)


@receiver(post_delete, sender=SliderItem)
def delete_picture(sender, instance, **kwargs):
    instance.picture.delete(False)

