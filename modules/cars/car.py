from .manufacturer import Manufacturer


class Car:
    """
    This class represents a car.
    """
    def __init__(self, manufacturer: Manufacturer, vehicleIdNumber: str, model: str, year: int, color: str):
        self.manufacturer = manufacturer
        self.vehicleIdNumber = vehicleIdNumber
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"{self.color}, {self.year}, {self.manufacturer.name}, {self.model}, {self.vehicleIdNumber}"
