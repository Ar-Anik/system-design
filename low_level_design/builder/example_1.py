from abc import ABC, abstractmethod

# main product class
class Meal:
    def __init__(self):
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def show(self):
        print("Meal Includes : ", self.items)


# Builder Interface
class MealBuilder(ABC):
    @abstractmethod
    def add_main_course(self):
        pass

    @abstractmethod
    def add_drink(self):
        pass

    @abstractmethod
    def add_dessert(self):
        pass

    @abstractmethod
    def get_meal(self):
        pass


# concrete builder
class VeganMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def add_main_course(self):
        self.meal.add_items("Salad Bowl")

    def add_drink(self):
        self.meal.add_items("Fresh Juice")

    def add_dessert(self):
        self.meal.add_items("Fruit Salad")

    def get_meal(self):
        return self.meal

# concrete builder
class KidsMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def add_main_course(self):
        self.meal.add_items("Chicken Nuggets")

    def add_drink(self):
        self.meal.add_items("Chocolate Milk")

    def add_dessert(self):
        self.meal.add_items("Ice Cream")

    def get_meal(self):
        return self.meal

# Director
class Waiter:
    def __init__(self, builder):
        self.builder = builder

    def prepare_meal(self):
        self.builder.add_main_course()
        self.builder.add_drink()
        self.builder.add_dessert()
        return self.builder.get_meal()


if __name__ == '__main__':
    vegan_builder = VeganMealBuilder()
    waiter = Waiter(vegan_builder)
    vegan_meal = waiter.prepare_meal()
    vegan_meal.show()

    kids_builder = KidsMealBuilder()
    waiter = Waiter(kids_builder)
    kids_meal = waiter.prepare_meal()
    kids_meal.show()
