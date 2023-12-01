
class Person:
    def __init__(self, fullname: str):
        self.fullname = fullname


class Driver(Person):

    def __init__(self, fullname: str, experience: float):
        super().__init__(fullname)
        self.exp = experience


class Engine:

    def __init__(self, power: float, manufacturer: str):
        self.power = power
        self.manufacturer = manufacturer


class Car:
    def __init__(self, brand: str, car_class: str, driver: Driver, engine: Engine):
        self.brand = brand
        self.car_class = car_class
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turn_right(self):
        print("Поворот направо")

    def turn_left(self):
        print("Поворот налево")

    def __str__(self):
        return f"Car: {self.brand}, Class: {self.car_class}\n" \
               f"Driver: {self.driver.fullname}, Experience: {self.driver.exp} years\n" \
               f"Engine: Power: {self.engine.power}, Manufacturer: {self.engine.manufacturer}"


class Lorry(Car):
    def __init__(self, brand: str, car_class: str, driver: Driver, engine: Engine, cargo_capacity: int):
        super().__init__(brand, car_class, driver, engine)
        self.cargo_capacity = cargo_capacity

    def __str__(self):
        return super().__str__() + f"\nCargo Capacity: {self.cargo_capacity}kg"


class SportCar(Car):
    def __init__(self, brand: str, car_class: str, driver: Driver, engine: Engine, max_speed: int):
        super().__init__(brand, car_class, driver, engine)
        self.max_speed = max_speed

    def __str__(self):
        return super().__str__() + f"\nMax Speed: {self.max_speed}km/h"


