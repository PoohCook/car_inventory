from ..cars import Car


class Inventory:
    def __init__(self):
        self.__cars = []

    def add(self, car: Car):
        if car in self.__cars:
            raise ValueError("Car already exists in inventory.")
        if any(c.vehicleIdNumber() == car.vehicleIdNumber() for c in self.__cars):
            raise ValueError("Car with the same VIN already exists in inventory.")
        self.__cars.append(car)

    def remove(self, car: Car):
        if car not in self.__cars:
            raise ValueError("Car not found in inventory.")
        self.__cars.remove(car)

    def query(self, make: str = None, model: str = None, year: int = None, sort_by: str = None):
        cars = self.__cars.copy()

        if make:
            cars = [c for c in cars if c.manufacturer().name() == make]
        if model:
            cars = [c for c in cars if c.model() == model]
        if year:
            cars = [c for c in cars if c.year() == year]
        if sort_by:
            if sort_by == 'make':
                cars.sort(key=lambda c: c.manufacturer().name())
            elif sort_by == 'year':
                cars.sort(key=lambda c: c.year())
            elif sort_by == 'model':
                cars.sort(key=lambda c: c.model())
            else:
                raise ValueError(f"Invalid sort_by value: {sort_by}")

        return cars
