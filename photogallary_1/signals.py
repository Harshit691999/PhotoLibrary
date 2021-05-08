from django.db.models.signals import pre_delete 
from .models import *
from django.dispatch import receiver

@receiver(pre_delete,sender=Photo)
def delete_file(sender, instance, **kwargs):
    photo_id = instance.id 
    p = Photo.objects.get(id = photo_id)
    p.image.delete()
    print("--------------pre_delete----------")
    print(photo_id)
    print(p.image)
