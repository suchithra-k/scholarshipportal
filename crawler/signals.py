from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Scholarship

@receiver(pre_save, sender=Scholarship)
def slugify_scholarship_title(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.title)
