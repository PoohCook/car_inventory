import unittest
from modules.cars import Manufacturer


class ManTest(unittest.TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer("Toyota", "Japan")

    def tearDown(self):
        # This method will run after each test
        pass

    def testCreateManufacturer(self):
        print("---------- testCreateManufacturer  ----------")
        self.assertEqual(str(self.manufacturer), "Toyota[made in Japan]")
