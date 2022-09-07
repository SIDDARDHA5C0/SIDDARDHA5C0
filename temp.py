import cv2
import pytesseract
import pandas as pd
# Open the device at the ID 0
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
cap = cv2.VideoCapture(0)
# Check whether user selected camera is opened successfully.
if not (cap.isOpened()):
    print("Could not open video device")
# To set the resolution
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#screen width resolution
cap.set(3,500)
#screen height resolution
cap.set(4,500)
# authenication part 
df1=pd.read_excel("C:\\Users\\Siddardha\\OneDrive\\Documents\\Authentication_people_data_set.xlsx", sheet_name=0)
#df1['RNO'] = df1['RNO'].astype('string')
df1[['RNO',"NAME OF STUDENT"]] = df1[['RNO',"NAME OF STUDENT"]].astype('string')
list1=list((df1["RNO"]))
list2=list((df1["NAME OF STUDENT"]))
while(True):
# Capture frame-by-frame
    ret, frame = cap.read()
    #convert the image to grayscale
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#giving threshold values
    a_t=cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,91,11)

    cv2.imshow("threshold",a_t)
   # frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# Display the resulting frame
    cv2.imshow('Reader',frame)
    texts = pytesseract.image_to_string(frame)
    #print(texts)
    #print(type(texts))
    delimiters=texts.split(" ") 
    delimiters1=texts.split("\n")
    #print(delimiters1)
    for i in delimiters1:
        for j in list2:
            if(i==j):
                print("yes done")
                print(i)
   # if  delimiters in list2:
    #    print("Yes done")
   # boxes=pytesseract.image_to_boxes(frame)
    #for b in boxes.splitlines():
     #   b=b.split(' ')
      #  x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
       # cv2.rectangle(frame,(x,500-y),(w,500-h),(0,0,255),3)
# Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()