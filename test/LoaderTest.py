from pprint import pprint
import unittest
from modules.inv import Inventory, Loader


class LoaderTest(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.loader = Loader(self.inventory)

    def tearDown(self):
        pass

    def testLoadInventory(self):
        print("----------- testLoadInventory  --------------")

        rejections = self.loader.load("test/scripts/inv_sample.json")
        self.assertEqual(rejections, [])

        inv = self.inventory.query()
        self.assertEqual(len(inv), 22)
