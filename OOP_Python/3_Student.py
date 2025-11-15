class Student:
    def __init__(self, grade, name):
        self.__grade = grade
        self.name = name

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            raise ValueError("Grade must be between 0 and 100")

    def get_grade(self):
        return self.__grade

    def  __str__(self):
        return f"Student: {self.name}, Grade: {self.__grade}"
s1 = Student(100, "Phong")
s2 = Student(50, "Toan")

try: 
    s2.set_grade(-10)
except ValueError as e:
    print(f"Error: {e}")

print(s1)
print(s2)