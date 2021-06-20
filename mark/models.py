from django.db import models
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save

class Photo(models.Model) :
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    photo_width = models.IntegerField(blank=True, null=True)
    photo_height = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/')

#이미지 사이즈 조절, 워터마크 박기 기능
# sender(UploadPhoto)
@receiver(post_save, sender=Photo)
def overlay_watermark(instance, sender, **kwargs):
    photo = Image.open(instance.photo)
    width = instance.photo_width
    height = instance.photo_height
    print(width, height)
    watermark = Image.open('mark/mark.PNG')
    photo.paste(watermark, (0,0), watermark)
    photo = photo.resize((width, height), Image.ANTIALIAS)
    photo.save(instance.photo.path)

