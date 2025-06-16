

class Manufacturer:
    """
    This class represents a car manufacturer.
    """
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name}[made in {self.country}]"
