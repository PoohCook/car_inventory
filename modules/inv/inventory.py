

class Inventory:
    def __init__(self):
        self.__cars = []

    def add(self, car):
        if car in self.__cars:
            raise ValueError("Car already exists in inventory.")
        self.__cars.append(car)

    def remove(self, car):
        if car not in self.__cars:
            raise ValueError("Car not found in inventory.")
        self.__cars.remove(car)

    def get(self):
        return self.__cars.copy()
