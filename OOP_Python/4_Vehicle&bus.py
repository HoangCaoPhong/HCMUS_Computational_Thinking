# 4. **Kế thừa đơn – “Vehicle” và “Bus”**
#     Tạo lớp cha `Vehicle` với thuộc tính: `max_speed`, `mileage`.
#     Tạo lớp con `Bus` kế thừa từ `Vehicle`, và thêm thuộc tính: `passengers`.
#     Tạo instance của `Bus` và in các thông số.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, passengers):
        super().__init__(max_speed, mileage)
        self.passengers = passengers

    def __str__(self):
        return ("Vehicle: BUS\n"
            f" Maxspeed: {self.max_speed} km\h\n" 
            f" Mileage:{self.mileage} km\n" 
            f" Passengers: {self.passengers}")
    
bus1 = Bus(80, 2000, 10)
bus2 = Bus(60, 1000, 10)

print(bus1)
print(bus2)