# 🖼️ Image to Text Extractor (OCR) – Django App

This Django web app allows users to **upload an image** and returns the **extracted text** using **Tesseract OCR**.

---

## 🚀 Features

- Upload image from browser
- Extract text from image using OCR
- Show extracted text on result page
- Keeps history of uploads (optional)
- Built with Django, Pillow, pytesseract

---


## 📦 Requirements

- Python 3.8+
- pip
- Tesseract OCR (installed separately)
    -Install to default path:
    C:\Program Files\Tesseract-OCR

    Add this line in views.py:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


