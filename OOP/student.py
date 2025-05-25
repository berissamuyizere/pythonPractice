class Student:
    school = "Akirachix"
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.yaer = 2025 - age

    def greet_student(self):
        return f"Hello {self.name}, welcome to {self.school}"

    def initials(self):
        return f"{self.first_name[0] + self.last_name[0]}"  
    
    def record_marks(self, points):
        self.marks = []
        self.marks.append(points)
        total = 0
        for marks in self.marks:
          total+=marks
        return f"marks recorded Totals mark is {total}"
        
