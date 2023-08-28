from django import forms
from .models import ImageBase64


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageBase64
        fields = ('image',)
