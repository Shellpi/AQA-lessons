"""Db orm model."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db_orm import Base


class Students(Base):
    """Table Students."""

    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

    enrollments = relationship('Enrollments', back_populates='student')


class Courses(Base):
    """Table Courses."""

    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    enrollments = relationship('Enrollments', back_populates='course')


class Enrollments(Base):
    """Table enrollments."""
    __tablename__ = 'enrollments'
    enrollment_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    course = relationship('Courses', back_populates='enrollments')
    student = relationship('Students', back_populates='enrollments')
