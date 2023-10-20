import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://facerecognitionattendanc-2de97-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')
data = {
    "105222":
        {
            "name": "Lipika K S",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 5,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-08-30 09:00:00"
        },
    "852741":
        {
            "name": "Emily",
            "major": "Chemical",
            "starting_year": 2021,
            "total_attendance": 10,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-08-30 09:00:00"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 4,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2023-08-30 09:00:00"
        }

}
for key, value in data.items():
    ref.child(key).set(value)
