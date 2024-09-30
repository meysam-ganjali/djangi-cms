from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Blog


@receiver(pre_save, sender=Blog)
def delete_old_cover_image(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_cover_image = Blog.objects.get(pk=instance.pk).cover_image
    except Blog.DoesNotExist:
        return False

    new_cover_image = instance.image
    if not old_cover_image == new_cover_image:
        old_cover_image.delete(False)


@receiver(post_delete, sender=Blog)
def delete_cover_image(sender, instance, **kwargs):
    instance.cover_image.delete(False)
