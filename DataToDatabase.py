import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://security-with-face-recognition-default-rtdb.firebaseio.com/"
})

ref = db.reference('Personnel')