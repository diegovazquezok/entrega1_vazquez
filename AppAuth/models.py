from django.db import models
from django.contrib.auth.models import User

from PIL import Image

# Create your models here.

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='media/profile_pics')

    def __str__(self):
        return f'{self.user.username} Avatar'
    
    #  # Override the save method of the model
    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path) # Open image

    #     # resize image
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size) # Resize image
    #         img.save(self.image.path) # Save it again and override the larger image