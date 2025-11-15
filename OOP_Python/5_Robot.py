# 5. **Phương thức lớp & tĩnh – “Robot”**
#     Tạo lớp `Robot` với thuộc tính: `name`.
#     Theo dõi số lượng robot còn hoạt động (class attribute).
#     Viết class method `number_active()` để in ra số robot đang hoạt động. Phương thức `remove()` làm “dừng” robot và giảm count.

class Robot:
    __number_attribute_robot = 0
    
    def __init__(self, name):
        Robot.__number_attribute_robot += 1 
        self.name = name
        self.status = "active"

    @classmethod
    def number_active(cls):
        return cls.__number_attribute_robot

    def remove(self):
        self.status = "deactivate"        
        Robot.__number_attribute_robot -= 1

print("Number active: ", Robot.number_active())
r1 = Robot("Lina")
print("Number active: ", Robot.number_active())
r2 = Robot("Anna")
print("Number active: ", Robot.number_active())
r1.remove()
print("Number active: ", Robot.number_active())




    