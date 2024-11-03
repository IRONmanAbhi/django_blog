from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
import uuid

def profile_image_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4().hex}.{ext}"
        return os.path.join('profile_pics', filename)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_image = Profile.objects.get(pk=self.pk).image
            except Profile.DoesNotExist:
                old_image = None
            if self.image and self.image != old_image:
                self.image.name = profile_image_path(self, self.image.name)
                super().save()
                img = Image.open(self.image.path)
                if(img.height > 200 or img.width > 200):
                    output_size = (200, 200)
                    img.thumbnail(output_size)
                    img.save(self.image.path)
                if old_image != 'default.jpg' and os.path.isfile(old_image.path):
                        os.remove(old_image.path)
        super().save()