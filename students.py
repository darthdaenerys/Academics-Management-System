from person import Person
from enrol import Enrol

class Student(Person):
    def __init__(self, first, last, dob, phone, addresses,international=False):
        super().__init__(first, last, dob, phone, addresses)
        self.international=international
        self.enrolled=[]
    
    def enroll(self,enrol):
        if not(isinstance(enrol,Enrol)):
            raise Error('Invalid object')
        self.enrolled.append(enrol)
    
    def isParttime(self):
        return len(self.enrolled)<3
    