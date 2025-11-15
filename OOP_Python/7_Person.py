class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} year old."
    
p1 = Person("Phong", 19)
print(p1)