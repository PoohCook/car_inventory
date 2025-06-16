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
        color = self.color
        year = self.year
        manuf = self.manufacturer.name
        model = self.model
        vin = self.vehicleIdNumber
        trademark = self.manufacturer.tradeMark()
        return f"{color}, {year}, {manuf}, {model}, {vin} {trademark}".strip()
