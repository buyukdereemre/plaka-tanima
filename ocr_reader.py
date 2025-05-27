import pytesseract
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\emreb\AppData\Local\Programs\Tesseract-OCR'

def read_plate_text(image_path):
    """
    OCR kullanarak plaka görselinden yazıyı okur.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Görsel bulunamadı: {image_path}")

    # Gri tonlama + threshold (okuma için ön işleme)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    # OCR işlemi
    custom_config = r'--oem 3 --psm 8'
    text = pytesseract.image_to_string(thresh, config=custom_config)

    text = ''.join(filter(str.isalnum, text)).upper()
    return text
