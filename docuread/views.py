from django.shortcuts import render
from .models import UploadedImage
from PIL import Image
import pytesseract

# Install Tesseract-OCR and set the path if necessary
# For Windows, you might need to set the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def upload_image(request):
    text = ''
    image_url = ''

    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        obj = UploadedImage.objects.create(image=image)
        image_path = obj.image.path
        image_url = obj.image.url

        text = pytesseract.image_to_string(Image.open(image_path))

    return render(request, 'docuread/upload.html', {'text': text, 'image_url': image_url})
