# 8. **Operator overloading – “Vector2D”**
#     Tạo lớp `Vector2D` với các thuộc tính `x`, `y`. Override toán tử cộng (`__add__`) để cộng vector.
#     Tạo vài vector và thử `v1 + v2`.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector2D(1, 2)
v2 = Vector2D(2, 3)
print(v1)
print(v2)
print(f"v1 + v2 = {v1 + v2}")

