"""Homework 22."""
import csv
import logging
import random

import db_model
from db_orm import Db
from sqlalchemy.exc import SQLAlchemyError

"""
Створення моделі даних: Створіть просту модель даних
для системи управління студентами. Модель може містити
таблиці для студентів, курсів та їх відношень.
Кожен студент може бути зареєстрований на декілька курсів.
Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.
Виконання базових операцій: Напишіть програму,
яка додає нового студента до бази даних та
додає його до певного курсу. Переконайтеся,
що ці зміни коректно відображаються у базі даних.
Запити до бази даних: Напишіть запити до
бази даних, які повертають інформацію про
студентів, зареєстрованих на певний курс, або курси,
на які зареєстрований певний студент.
Оновлення та видалення даних: Реалізуйте
можливість оновлення даних про студентів або курси,
а також видалення студентів з бази даних.
Можна використовувати будь яку ORM на Ваш вібир
"""

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def populate_db_from_csv(db, courses_file, students_file):
    """Populate the database with data from CSV files."""
    try:
        with open(courses_file, 'r') as course_file:
            reader = csv.DictReader(course_file)
            if 'name' not in reader.fieldnames:
                raise KeyError("Missing 'name' column in courses file.")
            courses = [db_model.Courses(title=row['name']) for row in reader]
            db.session.add_all(courses)

        with open(students_file, 'r') as stud_file:
            read = csv.DictReader(stud_file)
            if 'name' not in read.fieldnames or 'age' not in read.fieldnames:
                raise KeyError("Missing 'name' or 'age' column in the file.")
            students = [
                db_model.Students(
                    name=row['name'],
                    age=row['age'],
                ) for row in read
            ]
            db.session.add_all(students)

        db.session.commit()
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

        unique_enrollments = set()
        enrollments = []
        # 3 is a random value that is used for 3 cycles of enrollments
        for _ in range(len(students) * 3):
            student = random.choice(students)
            course = random.choice(courses)
            key = (student.student_id, course.course_id)

            if key not in unique_enrollments:
                unique_enrollments.add(key)
                enrollments.append(db_model.
                                   Enrollments(student_id=student.student_id,
                                               course_id=course.course_id))

        db.session.add_all(enrollments)
        db.session.commit()
        logging.info('Random enrollment assignments completed successfully!')
    except SQLAlchemyError as err:
        db.session.rollback()
        logging.error(f'Error : {err}')

    finally:
        db.session.close()


def add_new_student(db, name, age, course_ids):
    """Add new student and assign courses."""
    try:
        new_student = db_model.Students(name=name, age=age)
        db.session.add(new_student)
        db.session.commit()

        courses = (db.session.query(db_model.Courses).
                   filter(db_model.Courses.course_id.in_(course_ids)).all())
        if len(courses) != len(course_ids):
            raise ValueError(f'Some course IDs are invalid: {course_ids}')

        enrollments = [
            db_model.Enrollments(student_id=new_student.student_id,
                                 course_id=course_id) for course_id in course_ids
        ]

        db.session.add_all(enrollments)
        db.session.commit()
        logging.info(f'Student {name} added.')
    except SQLAlchemyError as err:
        db.session.rollback()
        logging.error(f'Error adding new student: {err}')

    finally:
        db.session.close()


def student_courses(db, student_id):
    """Return list of courses that the student enrolled."""
    try:
        courses = (
            db.session.query(db_model.Courses)
            .join(db_model.Enrollments,
                  db_model.Courses.course_id == db_model.Enrollments.course_id)
            .filter(db_model.Enrollments.student_id == student_id)
            .all()
        )
        logging.info(f'Student with {student_id} ID '
                     f'is enrolled for: '
                     f'{[course.title for course in courses]}')
    except SQLAlchemyError as err:
        db.session.rollback()
        logging.error(f'Error : {err}')

    finally:
        db.session.close()


def course_student_list(db, course_id):
    """Return list of students to the course."""
    try:
        students = (
            db.session.query(db_model.Students)
            .join(db_model.Enrollments,
                  db_model.Students.student_id == db_model.Enrollments.student_id)
            .filter(db_model.Enrollments.course_id == course_id)
            .all()
        )
        logging.info(f'Students enrolled in course '
                     f'"{course_id}" ID: '
                     f'{[student.name for student in students]}')
    except SQLAlchemyError as err:
        db.session.rollback()
        logging.error(f'Error : {err}')

    finally:
        db.session.close()


def enroll_student(db, student_id, course_id):
    """Enroll a student in a course."""
    try:
        # Duplicate checker
        existing_enrollment = (db.session.query(db_model.Enrollments).
                               filter_by(
            student_id=student_id,
            course_id=course_id).first())

        if existing_enrollment:
            logging.warning(f'Student with '
                            f'"{student_id}" ID is already '
                            f'enrolled in course "{course_id}".')
            return

        new_enrollment = db_model.Enrollments(
            student_id=student_id, course_id=course_id)
        db.session.add(new_enrollment)
        db.session.commit()
        logging.info(f'The student with ID '
                     f'"{student_id}" has been enrolled '
                     f'in course ID "{course_id}".')

    except SQLAlchemyError as err:
        db.session.rollback()
        logging.error(f'Error : {err}')

    finally:
        db.session.close()


def remove_student_from_course(db, student_id, course_id):
    """Remove student from the course."""
    try:
        enrollment = db.session.query(db_model.Enrollments).filter_by(
            student_id=student_id, course_id=course_id).first()
        if enrollment:
            db.session.delete(enrollment)
            db.session.commit()
            logging.info(f'Student with student id '
                         f'"{student_id}" is no more on the '
                         f'course with "{course_id}" ID.')

    except SQLAlchemyError as err:
        db.session.rollback()
        logging.error(f'Error : {err}')

    finally:
        db.session.close()


def remove_student(db, student_id):
    """Remove student from the DB."""
    try:
        with db.session.begin():
            db.session.query(db_model.Enrollments).filter_by(
                student_id=student_id).delete()
            student = db.session.query(db_model.Students).filter_by(
                student_id=student_id).first()
            if not student:
                logging.warning(f'Student with ID '
                                f'{student_id} does not exist.')
            else:
                db.session.delete(student)
                logging.info(f'The student '
                             f'"{student.name}" with '
                             f'"{student_id}" ID has been removed.')
    except SQLAlchemyError as err:
        db.session.rollback()
        logging.error(f'Error : {err}')


def remove_course(db, course_id):
    """Remove the course from the DB."""
    try:
        with db.session.begin():
            db.session.query(db_model.Enrollments).filter_by(
                course_id=course_id).delete()
            course = db.session.query(db_model.Courses).filter_by(
                course_id=course_id).first()
            if not course:
                logging.warning(f'Course with ID '
                                f'"{course_id}" does not exist.')
            else:
                db.session.delete(course)
                logging.info(f'The course '
                             f'"{course.title}" with "{course_id}"'
                             f' ID has been removed.')
    except SQLAlchemyError as err:
        db.session.rollback()
        logging.error(f'Error : {err}')


if __name__ == '__main__':
    db = Db()
    students_csv = 'students.csv'
    courses_csv = 'courses.csv'
    populate_db_from_csv(db, courses_csv, students_csv)
    random_enrollment_assignment(db)
    add_new_student(db, 'Vlad', 15, course_ids=[1, 2, 3])
    student_courses(db, 21)
    course_student_list(db, 1)
    enroll_student(db, 21, 6)
    remove_student_from_course(db, 21, 3)
    student_courses(db, 21)
    remove_student(db, 21)
    remove_course(db, 1)
