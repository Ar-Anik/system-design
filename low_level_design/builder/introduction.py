"""
Link : https://refactoring.guru/design-patterns/builder

Q: What is the Builder Pattern?
-> The Builder Pattern is a creational design pattern. Its main purpose is to separate the construction of a
complex object from its representation, so the same construction process can create different representations.

It’s useful when creating an object involves many steps or configurations. It avoids telescoping constructors
(constructors with many parameters) and makes code readable and maintainable.


Q: When do we use the Builder Pattern?
1. Object construction is complex – the object has many optional parts.
2. Different representations – we want to create multiple types of products using the same building process.
3. Avoid constructor explosion – instead of one constructor with many parameters, use step-by-step building.
4. Control the construction process – sometimes, the order of steps matters.


Q: How do we construct a Builder Pattern?
- The Builder Pattern has four main components:
1. Product – The complex object to be built.
2. Builder – Abstract interface/class defining building steps.
3. Concrete Builder – Implements the builder interface and constructs the product.
4. Director (optional) – Controls the construction sequence.

"""

"""
Builder Pattern : Extracts the construction logic from the main product class. Moves it into a separate Builder 
class. Builds the product step by step.
"""

from abc import ABC, abstractmethod

class Car:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = None
        self.gps = None

    def __str__(self):
        return (f"Car with {self.seats} seats, Engine: {self.engine}\n"
                f"Trip Computer: {self.trip_computer}, GPS: {self.gps}")

class Manual:
    def __init__(self):
        self.content = []

    def add_section(self, text):
        self.content.append(text)

    def __str__(self):
        return "Car Manual:\n" + "\n".join(self.content)

class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_seats(self, number):
        pass

    @abstractmethod
    def set_engine(self, engine):
        pass

    @abstractmethod
    def set_trip_computer(self, has_tc):
        pass

    @abstractmethod
    def set_gps(self, has_gps):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def set_seats(self, number):
        self.car.seats = number

    def set_engine(self, engine):
        self.car.engine = engine

    def set_trip_computer(self, has_tc):
        self.car.trip_computer = has_tc

    def set_gps(self, has_gps):
        self.car.gps = has_gps

    def get_product(self):
        product = self.car
        self.reset()
        return product

class CarManualBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.manual = Manual()

    def set_seats(self, number):
        self.manual.add_section(f"Car has {number} seats")

    def set_engine(self, engine):
        self.manual.add_section(f"Car is equipped with {engine} engine.")

    def set_trip_computer(self, has_tc):
        if has_tc:
            self.manual.add_section("Car has a trip computer")
        else:
            self.manual.add_section("Car has no trip computer")

    def set_gps(self, has_gps):
        if has_gps:
            self.manual.add_section("Car has GPS system.")
        else:
            self.manual.add_section("Car has no GPS system.")

    def get_product(self):
        product = self.manual
        self.reset()
        return product


class Director:
    def construct_sports_car(self, builder:Builder):
        builder.reset()
        builder.set_seats(2)
        builder.set_engine("SportEngine")
        builder.set_trip_computer(True)
        builder.set_gps(True)

    def construct_suv(self, builder:Builder):
        builder.reset()
        builder.set_seats(5)
        builder.set_engine("SUBEngine")
        builder.set_trip_computer(True)
        builder.set_gps(False)


if __name__ == '__main__':
    director = Director()

    car_builder = CarBuilder()
    director.construct_sports_car(car_builder)
    car = car_builder.get_product()
    print(car)

    manual_builder = CarManualBuilder()
    director.construct_sports_car(manual_builder)
    manual = manual_builder.get_product()
    print(manual)


"""
Real life uses of Builder Pattern:
1. SQLAlchemy / Django ORM → building queries.
2. Requests library → constructing HTTP requests.
3. Report/Document generation (ReportLab, python-docx).
"""