from pprint import pprint
import unittest
from modules.cars import Car, Manufacturer, BMW, Tesla
from modules.inv import Inventory


class InvTest(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        toyo = Manufacturer("Toyota", "Japan")
        car = Car(toyo, "5TDKZRBH4RS123456", "High Lander", 2024, "Red")
        self.inventory.add(car)

        bmw = BMW()
        car = Car(bmw, "WBA8E1C5XJY123456", "X5", 2023, "Blue")
        self.inventory.add(car)

        tesla = Tesla()
        car = Car(tesla, "5YJ3E1EA7JF123456", "Model S", 2022, "White")
        self.inventory.add(car)

    def tearDown(self):
        pass

    def testCreateInventory(self):
        print("----------- testCreateInventory  ------------")

        inv = self.inventory.query()
        self.assertEqual(len(inv), 3)
        self.assertEqual(inv[0].manufacturer().name(), "Toyota")
        self.assertEqual(inv[1].manufacturer().name(), "BMW")
        self.assertEqual(inv[2].manufacturer().name(), "Tesla")
        self.assertEqual(inv[0].vehicleIdNumber(), "5TDKZRBH4RS123456")
        self.assertEqual(inv[1].vehicleIdNumber(), "WBA8E1C5XJY123456")
        self.assertEqual(inv[2].vehicleIdNumber(), "5YJ3E1EA7JF123456")

    def testCreateInventoryDuplicate(self):
        print("----------- testCreateInventoryDuplicate  ---")

        car = self.inventory.query()[0]

        # test duplicate object
        with self.assertRaises(ValueError) as context:
            self.inventory.add(car)
        self.assertEqual('Car already exists in inventory.', str(context.exception))

        # test seperate object with duplicate attributes (enforces need for __eq__ method)
        toyo = Manufacturer("Toyota", "Japan")
        car = Car(toyo, "5TDKZRBH4RS123456", "High Lander", 2024, "Red")

        with self.assertRaises(ValueError) as context:
            self.inventory.add(car)
        self.assertEqual('Car already exists in inventory.', str(context.exception))

        inv = self.inventory.query()
        self.assertEqual(len(inv), 3)

    def testRemoveInventoryDuplicate(self):
        print("----------- testRemoveInventoryDuplicate  ---")

        car = self.inventory.query()[0]
        self.inventory.remove(car)
        inv = self.inventory.query()
        self.assertEqual(len(inv), 2)
        self.assertEqual(inv[0].manufacturer().name(), "BMW")
        self.assertEqual(inv[1].manufacturer().name(), "Tesla")
        self.assertEqual(inv[0].vehicleIdNumber(), "WBA8E1C5XJY123456")
        self.assertEqual(inv[1].vehicleIdNumber(), "5YJ3E1EA7JF123456")

        bmw = BMW()
        car = Car(bmw, "WBA8E1C5XJY123456", "X5", 2023, "Blue")
        self.inventory.remove(car)
        inv = self.inventory.query()
        self.assertEqual(len(inv), 1)
        self.assertEqual(inv[0].manufacturer().name(), "Tesla")
        self.assertEqual(inv[0].vehicleIdNumber(), "5YJ3E1EA7JF123456")

        with self.assertRaises(ValueError) as context:
            self.inventory.remove(car)
        self.assertEqual('Car not found in inventory.', str(context.exception))

    def testQueryInventory(self):
        print("----------- testQueryInventory  -------------")
        toyo = Manufacturer("Toyota", "Japan")
        car = Car(toyo, "5TDKZRBCMRS234561", "Camary", 2024, "Green")
        self.inventory.add(car)
        car = Car(toyo, "5TDKZRBCMRS345612", "Camary", 2023, "Yellow")
        self.inventory.add(car)
        car = Car(toyo, "5TDKZRBCMRS345612", "SR5", 2023, "Silver")
        self.inventory.add(car)

        bmw = BMW()
        car = Car(bmw, "WBA8E1C3XJY234561", "X3", 2023, "Silver")
        self.inventory.add(car)
        car = Car(bmw, "WBA8E1C3XJY345612", "X3", 2023, "Black")
        self.inventory.add(car)
        car = Car(bmw, "WBA8E1C5XJY345612", "X5", 2023, "Red")
        self.inventory.add(car)

        tesla = Tesla()
        car = Car(tesla, "5YJ3E1EA6JF123456", "Model S", 2023, "Black")
        self.inventory.add(car)
        car = Car(tesla, "5YJ3E1EA7JF234561", "Model S", 2023, "White")
        self.inventory.add(car)
        car = Car(tesla, "5YJ3E1EA7JF345612", "Model S", 2021, "Black")
        self.inventory.add(car)

        inv = self.inventory.query()
        self.assertEqual(len(inv), 12)

        inv = sorted(self.inventory.query(year=2023), key=lambda c: c.manufacturer().name())
        expected = [
            'Blue, 2023, BMW, X5, WBA8E1C5XJY123456 © BMW AG, Munich, Germany',
            'Silver, 2023, BMW, X3, WBA8E1C3XJY234561 © BMW AG, Munich, Germany',
            'Black, 2023, BMW, X3, WBA8E1C3XJY345612 © BMW AG, Munich, Germany',
            'Red, 2023, BMW, X5, WBA8E1C5XJY345612 © BMW AG, Munich, Germany',
            'Black, 2023, Tesla, Model S, 5YJ3E1EA6JF123456 (Batteries Included!)',
            'White, 2023, Tesla, Model S, 5YJ3E1EA7JF234561 (Batteries Included!)',
            'Yellow, 2023, Toyota, Camary, 5TDKZRBCMRS345612',
            'Silver, 2023, Toyota, SR5, 5TDKZRBCMRS345612',
        ]
        self.assertEqual([str(c) for c in inv], expected)

        inv = sorted(self.inventory.query(make="BMW"), key=lambda c: c.year())
        expected = [
            'Blue, 2023, BMW, X5, WBA8E1C5XJY123456 © BMW AG, Munich, Germany',
            'Silver, 2023, BMW, X3, WBA8E1C3XJY234561 © BMW AG, Munich, Germany',
            'Black, 2023, BMW, X3, WBA8E1C3XJY345612 © BMW AG, Munich, Germany',
            'Red, 2023, BMW, X5, WBA8E1C5XJY345612 © BMW AG, Munich, Germany'
        ]
        self.assertEqual([str(c) for c in inv], expected)

        inv = sorted(self.inventory.query(model='Model S'), key=lambda c: c.year())
        expected = [
            'Black, 2021, Tesla, Model S, 5YJ3E1EA7JF345612 (Batteries Included!)',
            'White, 2022, Tesla, Model S, 5YJ3E1EA7JF123456 (Batteries Included!)',
            'Black, 2023, Tesla, Model S, 5YJ3E1EA6JF123456 (Batteries Included!)',
            'White, 2023, Tesla, Model S, 5YJ3E1EA7JF234561 (Batteries Included!)'
        ]
        self.assertEqual([str(c) for c in inv], expected)
