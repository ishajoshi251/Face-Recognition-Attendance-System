import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceattendancerealtime-6ac5a-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1124":
        {
            "name": "Mukesh Ambani",
            "major": "Business Studies",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-07-31 00:54:34"
        },
    "1174":
        {
            "name": "Narendra Modi",
            "major": "Political Studies",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2023-07-31 00:54:34"
        },
    "1179":
        {
            "name": "Isha Joshi",
            "major": "Engineering",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-07-31 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)