from abc import ABC, abstractmethod

class TransportationStrategy(ABC):
    @abstractmethod
    def travel(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_time(self):
        pass

class BicycleStrategy(TransportationStrategy):
    def travel(self):
        return "Riding a bicycle. It's free but very slow."

    def get_cost(self):
        return 0

    def get_time(self):
        return 120

class BusStrategy(TransportationStrategy):
    def travel(self):
        return "Taking the bus. It's cost-effective but takes longer."

    def get_cost(self):
        return 10

    def get_time(self):
        return 60

class CabStrategy(TransportationStrategy):
    def travel(self):
        return "Taking a cab. It's faster but more expensive."

    def get_cost(self):
        return 50

    def get_time(self):
        return 20

class TravelContext:
    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy: TransportationStrategy):
        self._strategy = strategy

    def execute_travel(self):
        return self._strategy.travel()

    def get_travel_cost(self):
        return self._strategy.get_cost()

    def get_travel_time(self):
        return self._strategy.get_time()

def choose_transportation(budget, max_time):
    strategies = [CabStrategy(), BusStrategy(), BicycleStrategy()]

    for strategy in strategies:
        if strategy.get_cost() <= budget and strategy.get_time() <= max_time:
            return strategy
    return None

class Client:
    def main(self):
        strategy = choose_transportation(15, 70)
        if strategy:
            context = TravelContext()
            context.set_strategy(strategy)
            print(context.execute_travel())
            print(f"Cost: ${context.get_travel_cost()}, Time: {context.get_travel_time()}")
        else:
            print("No suitable transportation option found.")

        strategy = choose_transportation(60, 30)
        if strategy:
            context = TravelContext()
            context.set_strategy(strategy)
            print(context.execute_travel())
            print(f"Cost: ${context.get_travel_cost()}, Time: {context.get_travel_time()} minutes")
        else:
            print("No suitable transportation option found.")

        strategy = choose_transportation(0, 150)
        if strategy:
            context = TravelContext()
            context.set_strategy(strategy)
            print(context.execute_travel())
            print(f"Cost: ${context.get_travel_cost()}, Time: {context.get_travel_time()} minutes")
        else:
            print("No suitable transportation option found.")

if __name__ == '__main__':
    Client().main()
