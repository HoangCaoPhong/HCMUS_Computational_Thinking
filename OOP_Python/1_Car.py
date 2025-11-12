# 1. **Lớp đơn giản – “Car”**   
#     Tạo lớp `Car` với các thuộc tính: `make` (hãng), `model`, `year`.
#     Viết phương thức `get_info()` trả về chuỗi dạng:
#     `"{year} {make} {model}"`.
#     Tạo vài đối tượng và in thông tin của chúng.


class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model 
        self.__year = year    

    def get_info(self):
        return f"{self.__year} {self.__make} {self.__model}"


cars = []

n = int(input("Input number of cars: "))
for i in range(1, n+ 1):
    print(f"Car #{i}:")
    make = input("Make: ")
    model = input("Model: ")
    year = input("Year: ")
    
    cars.append(Car(make, model, year))

i = 1
for car in cars:
    print(f"Car #{i}:")
    i = i + 1
    print(car.get_info())