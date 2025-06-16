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

    def __eq__(self, other):
        if isinstance(other, Car):
            return (self.__manufacturer.name() == other.__manufacturer.name()
                    and self.__manufacturer.country() == other.__manufacturer.country()
                    and self.__vehicleIdNumber == other.__vehicleIdNumber
                    and self.__model == other.__model
                    and self.__year == other.__year
                    and self.__color == other.__color)
