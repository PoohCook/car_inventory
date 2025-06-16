from ..cars import Car


class Inventory:
    def __init__(self):
        self.__cars = []

    def add(self, car: Car):
        if car in self.__cars:
            raise ValueError("Car already exists in inventory.")
        self.__cars.append(car)

    def remove(self, car: Car):
        if car not in self.__cars:
            raise ValueError("Car not found in inventory.")
        self.__cars.remove(car)

    def query(self, make: str = None, model: str = None, year: int = None):
        cars = self.__cars.copy()

        if make:
            cars = [c for c in cars if c.manufacturer().name() == make]
        if model:
            cars = [c for c in cars if c.model() == model]
        if year:
            cars = [c for c in cars if c.year() == year]

        return cars
