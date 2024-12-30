"""Homework 22."""
import csv
import random
import logging
from sqlalchemy.exc import SQLAlchemyError

import db_model
from db_orm import Db

# Логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)


def populate_db_from_csv(db, courses_file, students_file):
    """Populate the database with data from CSV files."""
    try:
        with db.session.begin():
            with open(courses_file, 'r') as course_file:
                reader = csv.DictReader(course_file)
                if 'name' not in reader.fieldnames:
                    raise KeyError("Missing 'name' column in courses file.")
                courses = [db_model.Courses(title=row['name']) for row in reader]
                db.session.add_all(courses)

            with open(students_file, 'r') as stud_file:
                reader = csv.DictReader(stud_file)
                if 'name' not in reader.fieldnames or 'age' not in reader.fieldnames:
                    raise KeyError("Missing 'name' or 'age' column in students file.")
                students = [db_model.Students(name=row['name'], age=int(row['age'])) for row in reader]
                db.session.add_all(students)

        logging.info('Database populated successfully from CSV files!')
    except (KeyError, FileNotFoundError) as err:
        logging.error(f'Error with CSV file: {err}')
    except SQLAlchemyError as err:
        logging.error(f'Error populating database: {err}')


def random_enrollment_assignment(db):
    """Random enrollment assignments."""
    try:
        students = db.session.query(db_model.Students).all()
        courses = db.session.query(db_model.Courses).all()

        if not students or not courses:
            logging.warning('No students or courses available for enrollment.')
            return

        enrollments = [
            db_model.Enrollments(student_id=student.student_id, course_id=course.course_id)
            for student in students
            for course in random.sample(courses, k=min(len(courses), 3))
        ]

        db.session.bulk_save_objects(enrollments)
        db.session.commit()
        logging.info('Random enrollment assignments completed successfully!')
    except SQLAlchemyError as err:
        db.session.rollback()
        logging.error(f'Error: {err}')


def add_new_student(db, name, age, course_ids):
    """Add new student and assign courses."""
    try:
        with db.session.begin():
            new_student = db_model.Students(name=name, age=age)
            db.session.add(new_student)
            db.session.flush()  # Получение student_id без коммита

            courses = db.session.query(db_model.Courses).filter(db_model.Courses.course_id.in_(course_ids)).all()
            if len(courses) != len(course_ids):
                raise ValueError(f'Some course IDs are invalid: {course_ids}')

            enrollments = [db_model.Enrollments(student_id=new_student.student_id, course_id=course.course_id) for course in courses]
            db.session.add_all(enrollments)

        logging.info(f'Student {name} added and enrolled in courses {course_ids}.')
    except (SQLAlchemyError, ValueError) as err:
        logging.error(f'Error adding new student: {err}')


def student_courses(db, student_id):
    """List courses for a given student."""
    try:
        courses = (
            db.session.query(db_model.Courses)
            .join(db_model.Enrollments, db_model.Courses.course_id == db_model.Enrollments.course_id)
            .filter(db_model.Enrollments.student_id == student_id)
            .all()
        )
        logging.info(f'Student {student_id} enrolled in courses: {[course.title for course in courses]}')
    except SQLAlchemyError as err:
        logging.error(f'Error: {err}')


def course_student_list(db, course_id):
    """List students for a given course."""
    try:
        students = (
            db.session.query(db_model.Students)
            .join(db_model.Enrollments, db_model.Students.student_id == db_model.Enrollments.student_id)
            .filter(db_model.Enrollments.course_id == course_id)
            .all()
        )
        logging.info(f'Students enrolled in course {course_id}: {[student.name for student in students]}')
    except SQLAlchemyError as err:
        logging.error(f'Error: {err}')


def enroll_student(db, student_id, course_id):
    """Enroll a student in a course."""
    try:
        with db.session.begin():
            existing_enrollment = db.session.query(db_model.Enrollments).filter_by(
                student_id=student_id, course_id=course_id
            ).first()

            if existing_enrollment:
                logging.warning(f'Student {student_id} is already enrolled in course {course_id}.')
                return

            new_enrollment = db_model.Enrollments(student_id=student_id, course_id=course_id)
            db.session.add(new_enrollment)

        logging.info(f'Student {student_id} enrolled in course {course_id}.')
    except SQLAlchemyError as err:
        logging.error(f'Error: {err}')


def remove_student(db, student_id):
    """Remove a student and their enrollments."""
    try:
        with db.session.begin():
            db.session.query(db_model.Enrollments).filter_by(student_id=student_id).delete()
            student = db.session.query(db_model.Students).filter_by(student_id=student_id).first()
            if not student:
                logging.warning(f'Student with ID {student_id} does not exist.')
                return
            db.session.delete(student)
        logging.info(f'Student {student_id} and their enrollments removed.')
    except SQLAlchemyError as err:
        logging.error(f'Error removing student: {err}')


def remove_course(db, course_id):
    """Remove a course and related enrollments."""
    try:
        with db.session.begin():
            db.session.query(db_model.Enrollments).filter_by(course_id=course_id).delete()
            course = db.session.query(db_model.Courses).filter_by(course_id=course_id).first()
            if not course:
                logging.warning(f'Course with ID {course_id} does not exist.')
                return
            db.session.delete(course)
        logging.info(f'Course {course_id} and related enrollments removed.')
    except SQLAlchemyError as err:
        logging.error(f'Error removing course: {err}')


if __name__ == '__main__':
    db = Db()
    students_csv = 'students.csv'
    courses_csv = 'courses.csv'

    # Заполнение базы данных
    populate_db_from_csv(db, courses_csv, students_csv)

    # Случайные записи
    random_enrollment_assignment(db)

    # Добавление нового студента
    add_new_student(db, 'Vlad', 15, course_ids=[1, 2, 3])

    # Курсы студента
    student_courses(db, 21)

    # Студенты курса
    course_student_list(db, 1)

    # Записать студента на курс
    enroll_student(db, 21, 6)

    # Удалить студента с курса
    remove_student(db, 21)

    # Удалить курс
    remove_course(db, 1)
