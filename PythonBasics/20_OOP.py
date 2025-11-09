class Car:
    def __init__(self, year, make, model):
        self._year = year
        self._make = make
        self._model = model
    def get_info(self):
        return f"{self._year} {self._make} {self._model}"

cars = []

n = int(input("Input n = "))

for i in range(n):
    year = int(input("Year: "))
    make = input("Make: ")
    model = input("Model: ")
    cars.append(Car(year, make,model))

for i in cars:
    print(i.get_info())
        