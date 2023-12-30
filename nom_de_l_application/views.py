import cv2
import numpy as np
import pytesseract
from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile
import cv2

import numpy as np
 # Assurez-vous d'installer pytesseract et d'avoir Tesseract-OCR installé sur votre système
from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO




import cv2
import numpy as np
import pytesseract  # Assurez-vous d'installer pytesseract et d'avoir Tesseract-OCR installé sur votre système
from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image

import pytesseract

import pytesseract
from PIL import Image
from django.shortcuts import render

from gold_card.forms import ImageProcessingForm


def process_identity_card(request):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    result = pytesseract.image_to_string(Image.open(r'D:\nom_du_projet\gold_card\nom_de_l_application\test.png'))

    return render(request, 'traitement_image.html', {'result': result})


def showDemoPage(request):
    return render(request, 'index.html', )