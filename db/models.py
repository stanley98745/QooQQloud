from sqlalchemy import Column, Integer, String, ForeignKey, text
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base


class Student(Base):
    """Model for students."""
    __tablename__ = "students"

    student_ID = Column(String, primary_key=True, index=True)
    student_name = Column(String, nullable=False, index=True)
    class_ID = Column(String, ForeignKey("classes.class_ID"))

    # Relationship with Class
    enrolled_class = relationship("Class", back_populates="students")

    def __repr__(self):
        return f"<Student(student_ID={self.student_ID}, student_name={self.student_name})>"


class Teacher(Base):
    """Model for teachers."""
    __tablename__ = "teachers"

    teacher_ID = Column(Integer, primary_key=True, index=True)
    teacher_name = Column(String, nullable=False)
    title = Column(String, nullable=True)

    # Relationship with OpenCourse
    open_courses = relationship("OpenCourse", back_populates="teacher_info")

    def __repr__(self):
        return f"<Teacher(teacher_ID={self.teacher_ID}, teacher_name={self.teacher_name}, title={self.title})>"


class Class(Base):
    """Model for classes."""
    __tablename__ = "classes"

    class_ID = Column(String, primary_key=True, index=True)
    class_name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    # Relationship with Students
    students = relationship("Student", back_populates="enrolled_class")

    # Relationship with OpenCourse
    open_courses = relationship("OpenCourse", back_populates="class_info")

    def __repr__(self):
        return f"<Class(class_ID={self.class_ID}, class_name={self.class_name}, year={self.year})>"


class OpenCourse(Base):
    """Model for open courses."""
    __tablename__ = "open_course"

    open_course_ID = Column(String, primary_key=True, index=True)
    class_ID = Column(String, ForeignKey("classes.class_ID"))
    course_ID = Column(String, ForeignKey("all_courses.course_ID"))
    teacher_ID = Column(Integer, ForeignKey("teachers.teacher_ID"))

    # Relationship with Class
    class_info = relationship("Class", back_populates="open_courses")

    # Relationship with AllCourses
    course_details = relationship("AllCourses", back_populates="open_courses")

    # Relationship with Teacher
    teacher_info = relationship("Teacher", back_populates="open_courses")

    def __repr__(self):
        return f"<OpenCourse(open_course_ID={self.open_course_ID})>"


class AllCourses(Base):
    """Model for all courses."""
    __tablename__ = "all_courses"

    course_ID = Column(String(255), primary_key=True, index=True)
    course_name = Column(String(255), nullable=False)

    # Relationship with OpenCourse
    open_courses = relationship("OpenCourse", back_populates="course_details")

    def __repr__(self):
        return f"<AllCourses(course_ID={self.course_ID}, course_name={self.course_name})>"

class User(Base):
    __tablename__ = "users"

    user_ID = Column(Integer, primary_key=True, nullable=False)
    account = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
