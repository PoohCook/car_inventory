from .manufacturer import Manufacturer


class Car:
    """
    This class represents a car.
    """
    def __init__(self, manufacturer: Manufacturer, vehicleIdNumber: str, model: str, year: int, color: str):
        self.__manufacturer = manufacturer
        self.__vehicleIdNumber = vehicleIdNumber
        self.__model = model
        self.__year = year
        self.__color = color

    def manufacturer(self) -> Manufacturer:
        return self.__manufacturer

    def vehicleIdNumber(self) -> str:
        return self.__vehicleIdNumber

    def model(self) -> str:
        return self.__model

    def year(self) -> int:
        return self.__year

    def color(self) -> str:
        return self.__color

    def __str__(self):
        color = self.__color
        year = self.__year
        manuf = self.__manufacturer.name()
        model = self.__model
        vin = self.__vehicleIdNumber
        trademark = self.__manufacturer.tradeMark()
        return f"{color}, {year}, {manuf}, {model}, {vin} {trademark}".strip()
