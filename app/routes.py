
from flask import Blueprint, request, jsonify
from .models import Student
from . import db

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return {"message": "Driving School AI API running"}

@main.route("/students", methods=["POST"])
def add_student():
    data = request.json
    student = Student(
        name=data["name"],
        email=data["email"],
        phone=data["phone"]
    )
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": "Student added"}), 201

@main.route("/students", methods=["GET"])
def list_students():
    students = Student.query.all()
    return jsonify([
        {"id": s.id, "name": s.name, "email": s.email, "phone": s.phone, "lessons": s.lessons_completed}
        for s in students
    ])
    return home()
