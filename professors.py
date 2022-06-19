from person import Person

class Professor(Person):
    def __init__(self, first, last, dob, phone, addresses,salary):
        super().__init__(first, last, dob, phone, addresses)
        self.salary=salary
        self.courses=[]

    def checkforraise(self):
        if len(self.courses)>=4:
            self.salary+=20000
        
    def add_course(self,course):
        if not(isinstance(course,Course)):
            raise Error('Invalid Object')
        self.courses.append(course)
        