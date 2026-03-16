
from . import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    lessons_completed = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Student {self.name}>"


class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<Instructor {self.name}>"
    
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey("instructor.id"), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    student = db.relationship("Student", backref=db.backref("lessons", lazy=True))
    instructor = db.relationship("Instructor", backref=db.backref("lessons", lazy=True))

    def __repr__(self):
        return f"<Lesson {self.student.name} with {self.instructor.name} on {self.date}>"
