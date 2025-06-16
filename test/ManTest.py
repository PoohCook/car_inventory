import unittest
from modules.cars import Manufacturer


class ManTest(unittest.TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer("Toyota", "Japan")

    def tearDown(self):
        pass

    def testCreateManufacturer(self):
        print("---------- testCreateManufacturer  ----------")
        self.assertEqual(self.manufacturer.name(), "Toyota")
        self.assertEqual(self.manufacturer.country(), "Japan")
        self.assertEqual(str(self.manufacturer), "Toyota[made in Japan]")
