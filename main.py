from pyfirmata import Arduino , SERVO, util
from time import sleep
port = 'com5'
pin = 9
board = Arduino(port)
board.digital[pin].mode=SERVO
def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)

import cv2
import os
import pickle
import numpy as np

import face_recognition
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# to be modified
imgBackground = cv2.imread('Resources/vaporwave.jpg')
folderModePath='Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

for folder in modePathList:
   folderPath = os.path.join(folderModePath, folder)
   img = cv2.imread(folderPath)
   if img is not None:
        imgModeList.append(img)


        #.......................................
   else:
        print(f"Failed to load image from folder: {folderPath}")


#loading encodings
file = open('EncodeFile.p', 'rb')
encodeListKnownWiD = pickle.load(file)
file.close()
encodeListKnown, PersonnelId = encodeListKnownWiD


#------------------------------------------------------------------------------------
while True:
     success, img = cap.read()
     imgS = cv2.resize(img,(0, 0),None, 0.25, 0.25)
     imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB) #since opencv uses rgb while face-recognition uses bgr

     FaceCurrFrame = face_recognition.face_locations(imgS)
     encodeCurrFrame = face_recognition.face_encodings(imgS, FaceCurrFrame)


     imgBackground[162:162+480,55:55+640] = img
     imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[0] #can be modified

     for encodeFace, faceLoc in zip(encodeCurrFrame, FaceCurrFrame):
         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
         print("matches: ", matches)
         print("distances: ", faceDis)
         matchIndex = np.argmin(faceDis)
         if min(faceDis)<0.36:
                 y1, x2, y2, x1 = faceLoc
                 y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                 bbox = 55+x1, 162+y1, x2-x1, y2-y1
                 cvzone.cornerRect(imgBackground,bbox,rt=0)
                 print(PersonnelId[matchIndex])
                 imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[2]  #can be modified
                 for i in range(180):
                    rotateservo(pin, i)

                 sleep(1)

                 rotateservo(pin, 0)


     cv2.imshow("Webcam", img)
     cv2.imshow("Face Recognition", imgBackground)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()


# from pyfirmata import Arduino , SERVO, util
# from time import sleep
# port = 'com5'
# pin = 9
# board = Arduino(port)
# board.digital[pin].mode=SERVO
# def rotateservo(pin,angle):
#     board.digital[pin].write(angle)
#     sleep(0.015)
#

# import cv2
# import os
# import pickle
# import numpy as np
# import face_recognition
# import cvzone
# import serial
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# # arduinoSerial = serial.Serial('/dev/ttyACM0', 9600)
# imgBackground = cv2.imread('Resources/clouds.jpg')
# folderModePath = 'Resources/Modes'
# modePathList = os.listdir(folderModePath)
# imgModeList = []
#
# for folder in modePathList:
#     folderPath = os.path.join(folderModePath, folder)
#     img = cv2.imread(folderPath)
#     if img is not None:
#         imgModeList.append(img)
#     else:
#         print(f"Failed to load image from folder: {folderPath}")
#
# file = open('EncodeFile.p', 'rb')
# encodeListKnownWiD = pickle.load(file)
# file.close()
# encodeListKnown, PersonnelId = encodeListKnownWiD
#
# while True:
#     success, img = cap.read()
#     if not success:
#         continue
#
#     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
#
#     FaceCurrFrame = face_recognition.face_locations(imgS)
#     encodeCurrFrame = face_recognition.face_encodings(imgS, FaceCurrFrame)
#
#     imgBackground[162:162 + 480, 55:55 + 640] = img
#     imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[0]
#
#     for encodeFace, faceLoc in zip(encodeCurrFrame, FaceCurrFrame):
#         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
#         matchIndex = np.argmin(faceDis)
#         if min(faceDis) < 0.36:
#             y1, x2, y2, x1 = faceLoc
#             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#             bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
#             cvzone.cornerRect(imgBackground, bbox, rt=0)
#             print(PersonnelId[matchIndex])
#             imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[2]
#             for i in range(180):
#                 rotateservo(pin, i)
#             sleep(1)
#
#             rotateservo(pin, 0)
#
#
#     cv2.imshow("Webcam", img)
#     cv2.imshow("Face Recognition", imgBackground)
#     if cv2.waitKey(10) & 0xFF == ord('q'):  # Adjust waitKey delay
#         break
#
# cap.release()
# cv2.destroyAllWindows()
#
# import serial
#
# # Define serial port and baud rate (ensure they match Arduino settings)
# ser = serial.Serial('COM5', 9600)  # Replace '/dev/ttyUSB0' with your port name
#
# # Function to send servo position command
# def set_servo_angle(angle):
#   # Ensure angle is within valid range (0-180)
#   angle = max(0, min(angle, 180))
#   # Send the angle value as a string followed by a newline character
#   ser.write(str(angle).encode() + b'\n')
#
# # Example usage
# set_servo_angle(90)  # Set servo to 90 degrees
#
# # Close serial connection (optional)
# ser.close()
# from pyfirmata import Arduino , SERVO, util
# from time import sleep
# port = 'com5'
# pin = 9
# board = Arduino(port)
# board.digital[pin].mode=SERVO
# def rotateservo(pin,angle):
#     board.digital[pin].write(angle)
#     sleep(0.015)

