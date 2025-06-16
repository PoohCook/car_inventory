import unittest
from modules.cars import Car, Manufacturer, BMW, Tesla


class CarTest(unittest.TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer("Toyota", "Japan")
        self.car = Car(self.manufacturer, "5TDKZRBH4RS123456", "High Lander", 2024, "Red")

    def tearDown(self):
        pass

    def testCreateCar(self):
        print("----------- testCreateCar  ------------------")
        self.assertEqual(self.car.manufacturer.name, "Toyota")
        self.assertEqual(self.car.manufacturer.country, "Japan")
        self.assertEqual(str(self.car), "Red, 2024, Toyota, High Lander, 5TDKZRBH4RS123456")

    def testBMWCar(self):
        print("----------- testBMWCar  ---------------------")
        bmw = BMW()
        car = Car(bmw, "WBA8E1C5XJY123456", "X5", 2023, "Blue")
        self.assertEqual(car.manufacturer.name, "BMW")
        self.assertEqual(car.manufacturer.country, "Germany")
        self.assertEqual(str(car), "Blue, 2023, BMW, X5, WBA8E1C5XJY123456 © BMW AG, Munich, Germany")

    def testTeslaCar(self):
        print("----------- testTeslaCar  -------------------")
        tesla = Tesla()
        car = Car(tesla, "5YJ3E1EA7JF123456", "Model S", 2022, "White")
        self.assertEqual(car.manufacturer.name, "Tesla")
        self.assertEqual(car.manufacturer.country, "USA")
        self.assertEqual(str(car), "White, 2022, Tesla, Model S, 5YJ3E1EA7JF123456 (Batteries Included!)")
