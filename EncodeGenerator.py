import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://security-with-face-recognition-default-rtdb.firebaseio.com/",
    'storageBucket': "security-with-face-recognition.appspot.com"
})

folderPath = 'Images'
PathList = os.listdir(folderPath)
imgList = []
PersonnelID = []

for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    PersonnelID.append(os.path.splitext(path)[0]) #getting ID from image name
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)




def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #since opencv uses rgb while face-recognition uses bgr
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(imgList)
encodeListKnownWiD =[encodeListKnown, PersonnelID]

file = open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownWiD,file)
file.close()

