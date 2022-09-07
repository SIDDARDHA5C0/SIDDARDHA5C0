# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 22:05:43 2022

@author: Siddardha
"""

import pyzbar as pb
import cv2
from pyzbar.pyzbar import decode
print(dir(pb))
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    for barcode in decode(frame):
        print(barcode.data)
        data1=barcode.data.decode('utf-8')
        print(data1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
