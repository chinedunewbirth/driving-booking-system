
from . import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #phone = db.Column(db.String(20))   # <-- NEW COLUMN
    lessons_completed = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Student {self.name}>"
