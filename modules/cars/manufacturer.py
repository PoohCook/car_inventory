

class Manufacturer:
    """
    This class represents a car manufacturer.
    """
    def __init__(self, name: str, country: str):
        self.__name = name
        self.__country = country

    def name(self) -> str:
        return self.__name

    def country(self) -> str:
        return self.__country

    def __str__(self):
        return f"{self.__name}[made in {self.__country}]"

    def tradeMark(self) -> str:
        return f""


class BMW(Manufacturer):
    """
    This class represents a BMW manufacturer.
    """
    def __init__(self):
        super().__init__("BMW", "Germany")

    def tradeMark(self) -> str:
        return "© BMW AG, Munich, Germany"


class Tesla(Manufacturer):
    """
    This class represents a Tesla manufacturer.
    """
    def __init__(self):
        super().__init__("Tesla", "USA")

    def tradeMark(self) -> str:
        return "(Batteries Included!)"


class Toyota(Manufacturer):
    """
    This class represents a Toyota manufacturer.
    """
    def __init__(self):
        super().__init__("Toyota", "Japan")
