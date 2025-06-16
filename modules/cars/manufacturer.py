

class Manufacturer:
    """
    This class represents a car manufacturer.
    """
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name}[made in {self.country}]"

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
