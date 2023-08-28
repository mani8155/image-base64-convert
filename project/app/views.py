import os
from django.shortcuts import render, HttpResponse, redirect
from .forms import ImageUploadForm
from .models import ImageBase64
import base64

def image_to_base64(request):
    form = ImageUploadForm()
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            _img_md = form.save(commit=False)
            _img_md.save()
            return redirect('get-base64', _img_md.id)

    context = {'form': form}
    return render(request, 'upload_image.html', context)


def get_base64_link(request, pk):
    image = ImageBase64.objects.get(id=pk)
    # print(image.image.path)
    with open(image.image.path, "rb") as f:
        encoded_image = base64.b64encode(f.read())
        # print(encoded_image)

    context = {
        'base64_value': str(encoded_image)[2:-1],
        "image": image
    }
    # os.remove(image.image.path)

    return render(request, 'get_base64.html', context)


def delete_table(request, pk):
    image = ImageBase64.objects.get(id=pk)
    os.remove(image.image.path)
    image.delete()

    return redirect('base64')

