from professors import Professor
from enrol import Enrol

class Course:
    def __init__(self,name,code,max,min,professor):
        self.name=name
        self.code=code
        self.max=max
        self.min=min
        self.professors=[]
        self.enrollments=[]

        if isinstance(professor,Professor):
            self.professors.append(professor)
        elif isinstance(professor,list):
            for i in professor:
                if not(isinstance(i,professor)):
                    raise Error('Invalid Object passed in list')
                else:
                    self.professors.append(i)
        else:
            raise Error('Invalid object passed')
    
    def add_professor(self,professor):
        if not(isinstance(professor,Professor)):
            raise Error('Invalid object passed')
        self.professors.append(professor)
    
    def add_enrollment(self,enrol):
        if not(isinstance(enrol,Enrol)):
            raise Error('Invalid object passed')
        
        if len(self.enrollments)==self.max:
            raise Error('Cannot enroll, Course is full')
        self.enrollments.append(enrol)
    
    def is_cancelled(self):
        return len(self.enrollments)<self.min
    