import unittest
from modules.cars import Car, Manufacturer


class CarTest(unittest.TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer("Toyota", "Japan")
        self.car = Car(self.manufacturer, "5TDKZRBH4RS123456", "High Lander", 2024, "Red")

    def tearDown(self):
        pass

    def testCreateCar(self):
        print("----------- testCreateCar  -------------------")
        self.assertEqual(str(self.car), "Red, 2024, Toyota, High Lander, 5TDKZRBH4RS123456")
