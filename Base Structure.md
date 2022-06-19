# System Design

### Objective: *To design a system to track all of its students professors and courses. It keeps track of what courses are offered, who teaches each course and which students are enrolled in those course.It would also be able to track yhe grades of each student across all courses. For each student and professors, the school needs to know their address, age, phone number and name*.

## Address
- Country: string
- State: string
- House Address: string
- city: string
- zipcode: string

## Person
- firstname: string
- lastname: string
- dob: date
- phone: string

## Students
- international: bool
- isParttime(): bool
- OnProation(): bool

## Professors
- salary: int

## Course
- name: string
- code: string
- minStudents: int
- maxStudents: int
- start: date
- end: date
- isCancelled(): bool

## Enrol
- date: date
- grade: float
