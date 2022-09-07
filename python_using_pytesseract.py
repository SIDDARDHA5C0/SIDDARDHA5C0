# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 12:33:09 2022

@author: Siddardha
"""

import cv2
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe'
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# Reading image
img = cv2.imread("greenscreen_photo.jpg")

# Convert to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


cv2.imshow("Output", img)
cv2.waitKey(0)
# Detect texts from image
texts = pytesseract.image_to_string(img)

print(texts)