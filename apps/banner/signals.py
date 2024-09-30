from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Banner


@receiver(pre_save, sender=Banner)
def delete_old_picture(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_picture = Banner.objects.get(pk=instance.pk).picture
    except Banner.DoesNotExist:
        return False

    new_picture = instance.image
    if not old_picture == new_picture:
        old_picture.delete(False)


@receiver(post_delete, sender=Banner)
def delete_picture(sender, instance, **kwargs):
    instance.picture.delete(False)
