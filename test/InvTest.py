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

        inv = self.inventory.get()
        self.assertEqual(len(inv), 3)
        self.assertEqual(inv[0].manufacturer().name(), "Toyota")
        self.assertEqual(inv[1].manufacturer().name(), "BMW")
        self.assertEqual(inv[2].manufacturer().name(), "Tesla")
        self.assertEqual(inv[0].vehicleIdNumber(), "5TDKZRBH4RS123456")
        self.assertEqual(inv[1].vehicleIdNumber(), "WBA8E1C5XJY123456")
        self.assertEqual(inv[2].vehicleIdNumber(), "5YJ3E1EA7JF123456")

    def testCreateInventoryDuplicate(self):
        print("----------- testCreateInventoryDuplicate  ---")

        car = self.inventory.get()[0]

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

        inv = self.inventory.get()
        self.assertEqual(len(inv), 3)

    def testRemoveInventoryDuplicate(self):
        print("----------- testRemoveInventoryDuplicate  ---")

        car = self.inventory.get()[0]
        self.inventory.remove(car)
        inv = self.inventory.get()
        self.assertEqual(len(inv), 2)
        self.assertEqual(inv[0].manufacturer().name(), "BMW")
        self.assertEqual(inv[1].manufacturer().name(), "Tesla")
        self.assertEqual(inv[0].vehicleIdNumber(), "WBA8E1C5XJY123456")
        self.assertEqual(inv[1].vehicleIdNumber(), "5YJ3E1EA7JF123456")

        bmw = BMW()
        car = Car(bmw, "WBA8E1C5XJY123456", "X5", 2023, "Blue")
        self.inventory.remove(car)
        inv = self.inventory.get()
        self.assertEqual(len(inv), 1)
        self.assertEqual(inv[0].manufacturer().name(), "Tesla")
        self.assertEqual(inv[0].vehicleIdNumber(), "5YJ3E1EA7JF123456")

        with self.assertRaises(ValueError) as context:
            self.inventory.remove(car)
        self.assertEqual('Car not found in inventory.', str(context.exception))
