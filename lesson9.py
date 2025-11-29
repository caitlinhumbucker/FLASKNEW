import sqlite3

db = sqlite3.connect("database/student_marks.db")
db.row_factory = sqlite3.Row  

students = db.execute("SELECT * FROM students").fetchall()

for person in students:
    print(f"Firstname: {person['firstname']}")
    print(f"Lastname : {person['lastname']}")
    print(f"DOB      : {person['dob']}")
