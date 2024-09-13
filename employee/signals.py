from .models import Employee
from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image

@receiver(pre_save, sender=Employee)
def resize_photo(sender, instance, **kwargs):
    if instance.photo:
        img = Image.open(instance.photo)
        img_size = (240, 240)
        img.thumbnail(img_size, Image.LANCZOS)
        img.save(instance.photo.path)