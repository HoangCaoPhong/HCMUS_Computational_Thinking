# 9. **Composition – “Employee” và “Salary”**
#     Tạo lớp `Salary` chứa `pay` và `bonus`.
#     Tạo lớp `Employee` chứa `name` và một object `Salary`.
#     Viết phương thức `total_compensation()` trả về pay + bonus.

class Employee:
    def __init__(self, name, pay, bonus):
        self.name = name
        self.salary = Salary(pay, bonus)

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    def total_compensation(self):
        return self.pay + self.bonus

e1 = Employee("phong", 1000, 50)
print(e1.salary.total_compensation())