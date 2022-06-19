from course import Course
from students import Student
from datetime import datetime

class Enrol:
    def __init__(self,student,course,date,grade):
        if not(isinstance(student,Student) or not(isinstance(course,Course))):
            raise Error('Invalid object passed')
        self.student=student
        self.course=course
        self.grade=grade
        self.date=datetime().now()

    def set_grade(self,grade):
        self.grade=grade
