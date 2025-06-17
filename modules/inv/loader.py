import json
from typing import List
from ..cars import *


class Loader:
    """ Loader class to read inventory data from a file and populate the Inventory object."""
    def __init__(self, inv):
        self.inv = inv

    def load(self, path) -> List[str]:
        """Load inventory from a file."""
        rejections = []
        with open(path, 'r') as source:
            data = json.load(source)
            for line_no, line in enumerate(data):
                line = line.strip()
                try:
                    car = self.__parse_line(line)
                except Exception as e:
                    rejections.append(f"Error loading line[{line_no + 2}]: {e}")

        return rejections

    def __parse_line(self, line):
        """Parse a line from the file and create a Car object."""
        parts = line.split(',')
        if len(parts) != 5:
            raise ValueError(f"Invalid line format: {line}")

        # Example line format:
        # Blue, 2023, BMW, X5, WBA8E1C5XJY123456
        color, year, manufacturer, model, vin = parts
        year = int(year.strip())
        color = color.strip()
        manufacturer = manufacturer.strip()
        model = model.strip()
        vin = vin.strip()

        manufacturer = globals()[manufacturer]()
        car = Car(manufacturer, vin, model, year, color)
        self.inv.add(car)
