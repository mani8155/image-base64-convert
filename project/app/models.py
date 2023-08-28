import uuid

from django.db import models


class ImageBase64(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.id)







