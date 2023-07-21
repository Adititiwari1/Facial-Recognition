import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facial-attendance-70067-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2005,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
           "100000":
        {
            "name": "Kaibalya Jena",
            "major": "Physics",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
           "000001":
        {
            "name": "Aditi Tiwari",
            "major": "Physics",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
           "098765":
        {
            "name": "Yashraj singh",
            "major": "Physics",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
           "123456":
        {
            "name": "Anjali Tiwari",
            "major": "Physics",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
           "234567":
        {
            "name": "Vishwas dubey",
            "major": "Physics",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
           "345678":
        {
            "name": "Nikita Singh",
            "major": "Physics",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
           "567890":
        {
            "name": "Palwasha Fazeel Ahmed",
            "major": "Physics",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
            "654321":
        {
            "name": "Aditya Tiwari",
            "major": "Physics",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)